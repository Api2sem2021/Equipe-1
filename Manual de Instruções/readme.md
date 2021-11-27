<h1 align="center">

 📖 Manual de instruções 📖

</h1>

## Índice

* [Clonagem do repositório](#Clonagem-do-repositório)
* [Criação do ambiente virtual](#Criação-do-ambiente-virtual)
* [Iniciando Flask](#Iniciando-Flask)
* [Referências](#Referências)
* [Iniciando o BackEnd](#Iniciando-o-BackEnd)


<h4>

Esse documento tem como objetivo auxiliar qualquer usuário que tenha interesse em acessar a
página descrita no repositório armazenado e disponível em:
"https://github.com/Api2sem2021/Equipe-1".

A página estará disponível para acesso geral entre os dias 28/11/2021 e 25/12/2021 no endereço
"http://20.106.157.191:5000" para acessá-la, basta digitar o endereço em seu navegador de
preferência, o uso de AdBlock pode causar mal funcionamento em algumas páginas (Por ser parte
do projeto integrador a mesma não possui anúncios).

Caso o período de hospedagem já tenha se excedido, seguem as instruções necessárias para fazer
uso da página localmente (os comandos utilizados podem variar entre sistemas operacionais, as
instruções a seguir foram feitas com o usuário do SO Windows em mente) adiantamos que o
primeiro passo é ter em sua máquina a linguagem de programação Python e o pacote Pip.

</h4>


## Clonagem do repositório

<h4>
Para iniciar a página localmente o usuário precisa baixar o arquivo zip do repositório ou
cloná-lo a partir do Prompt de comando de seu computador, nesse documento cobre
apenas o método de download com o intuito de facilitar a experiência do usuário:
</h4>

![baixando-zip](https://user-images.githubusercontent.com/90697929/143706529-66bc88a1-07ae-4fdd-9c7f-fef8993011f4.gif)

## Criação do ambiente virtual 

<h4>

Criação do ambiente virtual para instalação dos requisitos:
Já com o repositório clonado, o usuário deve encontrar a pasta “Frontend” e copiar o
caminho até ela, no SO Win10, a maneira mais simples é entrando em propriedades e
copiando o local onde a pasta está armazenada, a seguir adicionando “\FrontEnd" (sem
as aspas) em frente ao caminho para especificar a pasta desejada para a criação do
ambiente virtual:

Como será demonstrado, o usuário deve acessar seu Prompt de comando (cmd) e digitar o
seguinte comando (RETIRAR ASPAS SIMPLES PARA UTILIZAR OS COMANDOS):

* ‘Cd "Path\FrontEnd""’

 * Checar se o cmd reconheceu o caminho para a pasta Frontend

* ‘py -3 -m venv venv’ (criando um ambiente virtual com o nome venv)

* Ao criar o ambiente virtual o usuário deve ativá-lo
‘venv\scripts\activate’ (tente barras comuns caso não consiga)

* E então instalar o arquivo requirements
‘pip install -r requirements.txt’


## Iniciando Flask

<h4>
Após cumprir o ultimo passo, basta escrever ‘flask run’ em seu cmd, isso irá iniciar o
flask e hospedar a página de forma local na porta padrão do 5000, basta copiar o endereço
que será impresso com o comando Ctrl+Shift+C (Ctrl+C irá finalizar a hospedagem) e
colar em seu navegador de preferência!
Ao finalizar basta voltar ao cmd e digitar Deactivate ou Ctrl+C
</h4>

![comandos](https://user-images.githubusercontent.com/90697929/143710153-883d58ed-e204-4a87-881d-18501ae04fb1.gif)

 
 ## Iniciando o BackEnd
 
 <h4>
  Para fazer uso do código na pasta BackEnd basta seguir os mesmos passos, até a instalação do arquivo requirements e então abrir e rodar o código em seu editor de preferência.
 </h4>
  
## Referências 

* <https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>
* <https://flask-ptbr.readthedocs.io/en/latest/>
* <https://www.docker.com/get-started>
