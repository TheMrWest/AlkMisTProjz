import projz
import aiohttp
import aiofiles
import asyncio
import csv
import sys
import os

async def login_account(email, password):
    client = projz.Client()
    try:
        r = await client.login_email(email, password)
        print(f"Logado: {email}")
        return client

    except (projz.error.ApiException, projz.error.InvalidEmail) as err:
        print(f"Erro ao logar {email}: {err}")
        return None

async def logout(client):
    await client.logout()

async def _parseLink(parseLink):
    session = aiohttp.ClientSession()
    try:
        async with session.post("https://www.projz.com/api/f/v1/parse-share-link", json={
            "link": parseLink
        }) as r:
            info = await r.json()
            await session.close()

            if info.get("apiCode"):
                return None
            return info
        
    except Exception as e:
        await session.close()
        return None

async def send_qi(client, chat: int):
    try:
        await client.send_qi(object_id=chat, count=10)
        print(f"QI doado: {client.account.email} - {chat}")
    except Exception as err:
        print(f"Erro ao doar QI para {client.account.email}: {err}")

async def send_qi_list(client, chat: list):
  for chat_id in chat:
    await send_qi(client, chat_id)

async def ler_arquivo(caminho):
    try:
        async with aiofiles.open(caminho, mode='r', encoding="utf-8") as arquivo:
            conteudo = await arquivo.readlines()
            if not (conteudo):
               return None
            return conteudo

    except FileNotFoundError:
        return None

async def get_chat_id():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, input, "Link do chat: ")

async def run(condition: bool = False):
    accounts_projz = await ler_arquivo('acc.txt') # Armazena as contas em uma variável
    chats_id = []

    if(accounts_projz):
        tasks = [login_account(account[0], account[1]) for acc in accounts_projz if (account := acc.strip().split(',')) and len(account) == 2 or print(f"Linha incorreta: {acc.strip()}")]
        clients = await asyncio.gather(*tasks)
        logged_clients = {client.account.email: client for client in clients if client}

        if(condition):
            chats = await ler_arquivo('chats.txt')
            if(chats):
                lchats = [_parseLink(c.strip()) for c in chats if(c.strip())]
                chats_id = await asyncio.gather(*lchats)
                chats_id = [chat.get('objectId') for chat in chats_id if chat and chat.get('objectType') == 1]
                print("- Doando QI em chats que estão listados em um arquivo de chats")
                await asyncio.gather(*[send_qi_list(qiC, chats_id) for qiC  in logged_clients.values()])
        else:
            print("Archivo 'chats.txt não será lido")
        
        while True:
            print("---")
            chat_link = await get_chat_id()

            if str(chat_link) == '0':
                logou = [logout(client) for client in logged_clients.values()]
                await asyncio.gather(*logou)
                break

            chat_info = await _parseLink(chat_link)

            if chat_info and chat_info.get('objectType') == 1:
                object_id = chat_info["objectId"]
                qi_tasks = [send_qi(client, object_id) for client in logged_clients.values()]
                await asyncio.gather(*qi_tasks)
            else:
                print("Link inválido.")
    else:
        print("Não há contas")

if __name__ == '__main__':
    print("Iniciando")
    value: bool = False
    try:
        if(sys.argv[1] == '-chatList'):
            value = True
        else:
            value = False
    except:
        value = False

    asyncio.get_event_loop().run_until_complete(run(value))