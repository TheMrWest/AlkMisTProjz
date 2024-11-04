# AlkMisTProjz
- Script (Não oficial) para doar QI em chats públicos do ProjectZ

## 1° Passo
Existem dependências que você necessita instalar para poder utilizar o algorimo.

### Distribuições Linux e também para o Termux é necessário instalar essas dependências

```
python3 
python3-venv 
git
```
## 2° Passo
Após a instalação, é necessário que você extraia esse repositório para usar o código. Você irá extrair, com seu terminal, usando o git
```
$ git clone https://github.com/TheMrWest/NewAlkemistProjz
```

## 3° Passo
Depois que extrair, você deverá fazer algumas coisas para poder conseguir utilizar o Script. Como esse algoritmo usar ambiente virtual, você ativará esse ambiente através desse comando:
```
source bin/activate
```
Esse comando ativará o ambiente virtual que o algoritmo usa.


## Alguns Ajustes
- Depois que concluir esses passos, você precisará estarm atento a algumas coisas

## acc.txt
- O 'acc.txt' é um arquivo onde ele estará armazenando todas as suas contas necessárias para qi ser doado.
Segue o exemplo abaixo de como você deve adicionar as contas
```
seuemail1@gmail.com,suasenha2
seuemail2@hotmail.com,senha3904902390
seuemail3@conta.com,senahbalbalbla
```

Todos os seus emails e suas senhas seguem uma ordem: EMAIL,SENHA
Dentro do arquivo 'acc.txt', você irá listar suas contas dessa forma.

### ALERTA
Vale ressaltar que: Se caso não tiver nenhuma conta, o script não será executado

## chats.txt
- O 'chats.txt' é onde você irá armazenar os seus chats. Ele também segue uma ordem. E sempre será o link do seu chat
```
SeuChat1
SeuChat2
SeuChat2
```

## Execução do Script
Para executar o script, existem duas formas


### Executar sem o uso do arquivo chats.txt
```
$ python main.py
```

### Executar e fazer a leitura do arquivo chats.txt
```
$ python main.py -chatList
```