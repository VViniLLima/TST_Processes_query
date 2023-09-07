# TST_Processes_query
Script to query tst processes information

Esse script visa facilitar a consulta de um grande número de processos no site: https://www.tst.jus.br/.

## Sobre a busca: 
A página do tst recebe um número de processo dividido em 6 campos: numeroTst,digitoTst,anoTst,orgaoTst,tribunalTst,varaTst.

Na data de criação deste script, o arquivo robots.txt da página não disponibilizava informações sobre rate limit, e não haviam páginas não autorizadas.

Após realizar alguns testes, estabeleci um intervalo de 10 segundos entre requisições a fim de minimizar os redirecionamentos para a pagina de recaptcha.
___
## Bibliotecas utilizadas
**requests_html:** Biblioteca utilizada para realizar as requisições e coletar os dados.

- Confira a documentação [aqui](https://requests-html.kennethreitz.org/)
- Confira o GitHub [aqui](https://github.com/psf/requests-html)

## Composição

O script atualmente é composto por 6 arquivos:

- process_number.py
- connection.py
- data_scrape.py
- data_treatment.py
- routine.py
- main.py



### process_number.py
```
class Process:
```
Responsável por realizar as transformações necessárias na lista de processos recebida como input.

- `process_input_to_list`: Recebe uma string com os números dos processos separados por vírgula e retorna uma lista.

- `process_number_to_parts`: Recebe um numero de processo da lista criada pela função `process_input_to_list` e o divide nos campos necessários para realizar a busca;


### connection.py
```
class Connection:
```
Responsável por gerenciar a conexão com a página a ser consultada. Possui as seguintes funções:

- `create_session_object`: Responsável por criar o objeto `HTMLSession`; Não recebe parâmetros.

- `create_request_object`: Responsável por criar o objeto da requisição; Recebe um número de processo como parâmetro e o submete a função `process_number_to_parts` para obter os campos necessário para a busca.

- `check_page_availability`: Utilizada pela função `create_request_object`, é responsável por checar se a requisição feita acessou a página corretamente ou foi redirecionada para um Recaptcha.


### data_scrape.py
```
class DataScrape:
```

Responsável por buscar as informações contidas na página do processo.

- `extract_data`: Recebe a requisição como parâmetro e retorna a data e as informações da última movimentação do processo.


### data_treatment.py
```
class DataTreatment:
```
Responsável por tratar os dados extraídos.

- `last_update_data`: Recebe como parâmetro as informações do processo retornadas pela função `extract_data` e retorna um dicionário com ambas informações.


### routine.py
Responsável por concentrar a lógica da consulta

- `routine`: Recebe como parâmetro a lista de processos retornada por `process_input_to_list`, inicia os objetos necessários e o dicionário que será retornado ao final de sua execução, então, itera por todos os itens da lista recebida da seguinte forma: 

- Cria o objeto da conexão;
- Realiza a requisição;
- Obtém os dados do processo como um dicionário;
- Insere esses dados no dicionário já inicializado, utilizando o número do processo como chave.
- Encerra a conexão
- Espera 10 segundos
- Caso haja outro item na lista, repete a operação;

Após o fim do loop, exporta o dicionário obtido no formato json.


### main.py
Responsável por inicializar a consulta.

- `main`: Recebe uma string com os números dos processos separados por vírgula, os submete a função `process_input_to_list` e retorna a chamada da função `routine` passando como parâmetro a lista obtida.