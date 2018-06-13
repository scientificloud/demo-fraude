###Interface de fraudes

Interface de fraudes
====================

Funcionamento do programa
-------------------------

A interface contém 4 telas, sendo elas divididas em: Tela 1: Tela de login Tela 2: Usuário Tela 3: Triagem analista Tela 4: Descrição do caso

Ao iniciar o programa, o usuário digita suas credenciais na tela de login, caso seu perfil seja de call center será redirecionado para tela 2, se o perfil for de analista, ele irá para tela 3 e terá acesso a tela 4.

Arquitetura
-----------

O lado do servido(backend), da interface foi construído na linguagem Python na sua versão 3, utilizando o micro framework Flask na sua última versão, além das suas bibliotecas padrões.

Para o lado cliente(frontend) da aplicação utilizamos o framework materialize para cronstuirmos a tela 2 juntamente com o Bootstrap, Jquery e JavaScript, sendo esses últimos 3 utilizados também na criação das demais telas da aplicação.

URL'S
-----

A aplicação possuí 3 rotas padrões para exibição do HTML para o usuárioz são elas:
> **'/'** Redireciona para tela 1 
> **'/usuario'** Redireciona para tela 2 '/analista' --> redireciona para tela 3
**'/descricao' + parametro** base64json que contém todos os dados do usuário encodados base64

Além dessas rotas, a interfaces possuí outras rotas que são responsáveis por receber dados do cadastro do novo sinistro e enviar para a API Rest da intersystems e definir o veredito do analista inserindo essa informação na API Rest da intersystems. Essas URLs são:
>**'/cadastrar_dados'**
>**'/decisao_analista'**
>**'/receber_dados_intersystems/<int:tipo>'**

Banco de dados
--------------
Para fins de teste, estou usando o SQLITE nativo do Python3.
O arquivo que contém alguns dados é o **database.db**


Estrutura de pastas
-------------------
**| Flask**
&nbsp;&nbsp;&nbsp;&nbsp;**|-static** Contem os arquivos *.css, *.js e imagens
&nbsp;&nbsp;&nbsp;&nbsp;**|-templates** Contem os arquivos *.HTML

Dependencias
------------
Python 3
FLASK(latest)


Como executar
------------
####Localhost
Dentri da pasta Flask, abra o terminal/powershell/cmd e digite:
**python main.py**
Acesse a URL:

localhost:5000/<:rota padrao:>
127.0.0.1:5000/<:rota padrao:>