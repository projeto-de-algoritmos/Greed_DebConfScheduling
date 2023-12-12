# **DebConfScheduling** 

**Conteúdo da Disciplina**: Interval Scheduling <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0078224  |  Thaís Rebouças de Araujo |

## Sobre 
Todo ano em algum lugar do mundo acontece a DebConf, com vários dias de atividades e palestras.
Esse ano o evento aconteceu na Índia, e para facilitar a escolha de quais atividades participar, esse projeto irá ajudar a montar um cronograma de atividades de acordo com o dia que você gostaria de participar.

Os dados da agenda do evento foram retirados do [site oficial](https://debconf23.debconf.org/schedule/) através de raspagem dos dados, com o objetivo de ter os dados atualizados sempre que for utilizado.
O cronograma é feito utilizando o algoritmo ambicioso, interval scheduling, e foi pensado para preencher os dias com o menor tempo de ócio possível.

## Screenshots
![image](https://github.com/Thais-ra/thais-ra/assets/35047444/d91fc9d8-c56b-4b7c-959f-1a8c7caba632)

## Instalação 
**Linguagem**: python<br>

## Uso

Para instalar as dependências é recomendado utilizar uma venv.
Na pasta raiz instale as dependências utilizando o comando:

``` pip3 install -r requirements.txt```

Execute o shell script que fará a raspagem de dados:

```./execute_crawler.sh```

Se tiver problema para executar, adicione a permissão de execução ao script:

```chmod +x execute_crawler.sh```

Ao rodar o script, o programa fará a raspagem de dados para atualizar o arquivo "schedule.json".
Não é necessário rodá-lo sempre que for usar, só na primeira vez ou quando quiser atualizar a agenda.

Para executar o programa, basta executar o arquivo **main.py** na raíz:

```python3 main.py```

## Vídeo

[Vídeo de apresentação](https://unbbr.sharepoint.com/:v:/s/ok632/EQdvEVvUESxIqg_KwbODSjABjrkVc5YsHIAN8kIze-fbDw?e=0PjY8U&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)



