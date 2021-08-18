# MINERACAO-DE-BASE-DE-DADOS-E-CLASSIFICACAO-DE-TEXTO

 Universidade de Brasília Faculdade de Comunicação Benedito Medeiros Neto Caio Fonseca – 12/0027691
Projeto de Mineração de Base de Dados e Classificação de Texto
Brasília, DF 2018
1

 Resumo: Mineração das bases de dados Google Scholar e SciELO, partindo de termo de busca e número de resultados definidos; classificação de texto tendo como base a frequência de palavras em conjunto de artigos contidos em uma pasta definida.
Palavras-Chave: Procom, Python, Comunicação, Mineração de Bases de Dados, Classificação de Texto.
1. Introdução
Python é uma linguagem de programação poderosa e que se destaca por sua limpeza na apresentação do código. Algumas de suas características notáveis são: sintaxe de fácil compreensão, que permite a criação de programas com códigos de leitura mais acessível; simplicidade no uso e funcionamento, uma vez que é uma linguagem ideal para o desenvolvimento de protótipos, por exemplo; vasta biblioteca que permite um grande número de funcionalidades; compatível com a maioria das plataformas; é de livre acesso, com licença aberta e gratuita.
Além disso, é uma linguagem que dispõe de diversas ferramentas para análise e manipulação de dados. Oferece, também, suporte para programação object-oriented, com as classes, bem como o agrupamento do código em módulo e pacotes.
A ideia proposta neste trabalho é justamente voltada para a otimização do trabalho de pesquisa em base de dados, tendo em vista a dificuldade de lidar com uma grande quantidade de informações. A linguagem Python permitiu que essa tarefa fosse realizada com facilidade e velocidade impressionantes.
O objetivo aqui é descrever como se deu o processo de desenvolvimento do artefato, até chegar à sua versão atual. No momento, tem-se duas abordagens que, no futuro, pretende-se que sejam unificadas como um só processo. A primeira abordagem é voltada para a mineração das bases de dados Google Scholar e SciELO; a segunda abordagem é a classificação de textos, partindo da frequência de palavras nos artigos em uma pasta definida.
2. Metodologia e Desenvolvimento
O código teve inúmeras versões, e a sua versão atual é a 3.2. Desde o início, a questão que
guiou o trabalho foi a seguinte: “Como posso otimizar meu tempo de estudo para minha
Monografia de Conclusão de Curso, tendo em vista que tenho centenas de artigos acadêmicos para
2

 ler e não tenho ideia de por onde começar?”. Portanto, o projeto surgiu como uma necessidade pessoal que, logo se percebeu, era uma necessidade de um grande número de pessoas que têm que fazer pesquisa em bases de dados e não sabem por onde começar. Então, a primeira versão foi criada a partir dessa necessidade, bem como as outras que vieram em seguida.
O foco aqui será justamente o funcionamento de cada versão, a evolução entre uma versão e outra.
3. Códigos
Código – versão 1.0
A princípio, importamos as seguintes bibliotecas:
- Counter:seráutilizadaparafazermosacontagemdafrequênciadepalavrasnosartigos;
- pprint: será utilizada para podermos fazer o print de maneira mais limpa visualmente;
- nltk: será utilizada para termos acesso a funcionalidades voltadas para linguagem natural;
- pandas: será utilizada na criação de dataframes a partir dos dados coletados;
- os: será utilizada ao acessar os arquivos de uma pasta pré-definida;
- csv: será utilizada na criação de um arquivo com extensão .csv com os dados das frequências de
palavras;
- pprint(novamente): é perceptível a falta de atenção aqui, pois não é necessário importar duas
vezes esta biblioteca.
Logo de início, pode-se perceber algumas falhas nesta versão. A primeira falha é a dupla
importação da biblioteca pprint, certamente uma falta de atenção. A segunda falha é a redundância em algumas bibliotecas e suas funcionalidades, como Counter e nltk, ou pandas e csv.
 3

  Em seguida, temos a função clean, que serve para, inicialmente, ler um arquivo de texto e, em seguida, fazer uma limpeza nas palavras: elimina caracteres que não sejam letras, e elimina as palavras “comuns” presentes na lista stopwords. Por fim, é criada a variável global text_doc, e a função statistic é ativada. É bom perceber que, na função clean, deve-se definir uma pasta dir, que será utilizada mais à frente, e um arquivo de texto doc.
A função statistic serve justamente para fazermos a contagem da frequência de palavras, bem como salvarmos as informações em um arquivo .csv, por meio das funções data e all_csv.
 4

  Por fim, a função parser serve para acessarmos as palavras do texto em uma pasta definida, extrairmos suas frequências e a pontuarmos por meio de uma fórmula. Então, utilizamos pprint para retornar o nome do arquivo (file) e sua pontuação (percent).
Código – versão 1.1
Pode-se perceber já algumas mudanças nas bibliotecas importadas. Aqui, o objetivo foi tentar implementar uma interface visual, que facilitasse a visualização das informações e tornasse todo o funcionamento mais acessível, por meio da biblioteca tkinter.
  5

 Na função clean, foram removidas a necessidade de definição da variável dir e a variável text_doc. Porém, sua função continua basicamente a mesma em relação à versão 1.0.
6

 A função statistic continua com a mesma funcionalidade. Porém, agora ela contém a função disp, que serve para abrir uma nova janela com as diversas informações obtidas por meio das fórmulas, a partir das variáveis count, total_percent, dict_common_spec e dict_common_spec_total.
A função data continua salvando as informações em um arquivo .csv.
A função gen serve para obter a informação digitada no espaço dedicado na interface e vinculá-la à variável doc e, a partir dela, ativar a função clean.
Esta é a parte final do código, na qual ficam determinadas as características da interface, como os botões, o texto, o espaço dedicado à inserção de informação, etc.
Código – versão 2.0a
A partir desta versão, o programa inicial foi desmembrado para facilitar o trabalho. A versão 2.0a serve para a leitura de arquivos .pdf, e sua conversão em arquivo .txt.
A biblioteca PyPDF2 será utilizada para extrair a informação dos arquivos .pdf. Já a biblioteca os será utilizada para listar os arquivos em uma pasta definida.
    7

 A função read_pdf serve para extrair o texto de todas as páginas de um arquivo .pdf, definido pela variável file, página por página. No final, é ativada a função print_pdf.
A função print_pdf cria um arquivo de texto .txt com as informações extraídas de um arquivo .pdf definido pela variável file.
  A função pdf_to_txt tenta ativar a função read_pdf para cada arquivo na pasta src indicada, indicando as exceções.
Código – versão 2.1a
Esta versão já é mais complexa, pois além de extrair a informação dos arquivos .pdf contidos em uma pasta indicada, faz a contagem da frequência de palavras em cada arquivo e sua eventual pontuação.
Além das bibliotecas encontradas na versão 2.0a, nesta versão utiliza-se as bibliotecas: Counter, para fazer a contagem de frequência de palavras; math e numpy, para serem feitas as contas necessárias para as fórmulas de pontuação.
  8

 Estas serão as variáveis utilizadas nas funções, sendo d e PTS dicionários, e sub_dir e files listas.
 A função prep funciona como preparação dos arquivos .pdf para a extração de suas informações. Para utilizá-la, é necessário definir uma variável dir, que indicará justamente a pasta com a qual trabalharemos. A partir desta pasta, serão encontradas suas subpastas e, em cada subpasta, serão encontrados os arquivos. Por algum motivo, aparece o item .DS_Store, o qual não sei para que serve, mas, de qualquer modo, consegui evitar que ele fosse lido, pois estava fazendo o programa dar um erro. Por fim, a função pdf_txt é ativada para cada arquivo (definido como variável file) existente na lista files, bem como um print indicando que o arquivo foi lido. As exceções de erro são indicadas também.
 A função pdf_txt extrai o texto do arquivo .pdf, definido como file, página por página, e em seguida fazendo a contagem da frequência de palavras, bem como atualizando o dicionário d com as informações de frequência contidas em count.
9

  A função cont, a partir da variável d, que indica um dicionário contendo as frequências das palavras, primeiro faz uma limpeza, eliminando todas as palavras muito pequenas e todos os caracteres que não sejam letras. depois, faz uma pontuação com base na frequência de palavras e, por fim, atualiza o dicionário PTS.
A função pts_files, partindo do dicionário PTS, ordena os valores em ordem crescente e então retorna cada item, pontuação e porcentagem em relação à pontuação média.
 10

 Código – versão 2.0b
Esta versão está focada nas funcionalidades da biblioteca nltk.
A biblioteca nltk servirá para fazer a análise e classificação de texto. Já a biblioteca urllib.request foi equivocadamente importada, provavelmente tendo em vista já a mineração de bases de dados.
  A função dados, a partir de um arquivo doc e uma língua natural language definidos, faz a classificação de texto.
A função percentage avalia a porcentagem relacionada à frequência de um termo em um texto.
Código – versão 2.0.1.1c
Esta versão já está voltada para a mineração no Google Scholar, buscando um termo definido em uma quantidade também definida de resultados.
A biblioteca BeautifulSoup serve para formatar a informação html extraída. A biblioteca requests servirá justamente para extrair a informação html a partir de um link (que, no caso, é um link já definido como sendo do Google Scholar).
  11

  Aqui é criada a lista l, na qual serão armazenados os links obtidos.
Analisando a url de busca do Google Scholar, foi possível observar que uma parte era relacionada ao termo de busca, e outra à quantidade de resultados. A partir daí, foi desenvolvida a função Query, que, uma vez definidas as variáveis query (indicando o termo a ser buscado) e results (indicando o número de resultados pretendido), fará a extração dos links contidos na página. Uma dificuldade, porém, foi selecionar somente os links relacionados aos artigos acadêmicos.
Código – versão 2.0.1.2c
  12

 Nesta versão, a única diferença em relação à versão anterior é uma otimização da função Query, na qual a busca pelos links ficou mais refinada.
Código – versão 2.0.1.3c
Nesta versão, também houve somente uma otimização da função Query. Código – versão 2.0.2.1c
  13

 Esta versão é dedicada à busca na plataforma SciELO, mas o princípio é o mesmo da versão dedicada ao Google Scholar, apenas com leves alterações na função Query para se adaptar à url e ao html, que são diferentes.
Código – versão 2.0.2.2c
Esta versão é similar à anterior, mas com otimização da função Query. Código – versão 2.0.2.3c
  14

 Esta versão novamente traz apenas algumas melhorias na função Query. Código – versão 2.1c
Aqui já começou a haver uma maior integração entre as versões anteriores. A classe Query contém a função parse, que nas versões anteriores funcionava como a função Query. O funcionamento do código se dá da seguinte forma: primeiro, define-se o termo de busca query e o número de resultados results; então, criamos um objeto a partir da classe Query; por fim, acionamos a função parse. Esta função traz as mesmas funcionalidades dos códigos anteriores, com a diferença de buscar simultaneamente no Google Scholar e no SciELO. É importante ressaltar que o número de resultados definidos em results serve para as duas bases, ou seja, se definimos results = 10, então teremos 10 resultados do Google Scholar e 10 resultados do SciELO.
 15

 Código – versão 2.2c
 Esta versão é muito similar à anterior, apenas com alguns ajustes e otimizações na função parse.
Código – versão 3.0
Nesta versão já encontramos algo mais próximo do que se buscava no início, que é a união do que foi visto nas últimas versões citadas. Aqui já se encontra duas classes, que definirão justamente as duas abordagens previstas: a classe Query, e a classe PdfText.
A classe Query serve para fazer a busca nas bases Google Scholar e SciELO. Ela é muito similar à versão 2.2c do código.
 16

 Primeiro, importamos as bibliotecas acima, as quais continuam as mesmas até a versão atual do código.
Em seguida, a classe Query. Nesta classe, temos três variáveis, das quais duas são previamente definidas. A primeira variável é a lista self.l, que está vazia e será onde os links dos artigos serão armazenados. A segunda variável é a variável query, que será definida previamente tendo em vista o termo a ser buscado. A terceira variável é a variável results, que será definida previamente tendo em vista o número de resultados pretendidos em cada base. Portanto, a criação do objeto com base nesta classe se dá da seguinte maneira:
>>> query = ‘termo_de_busca_exemplo’
>>> results = n #sendo que type(n) == int >>> q = Query(query, results)
  A função links_to_txt tem o objetivo de ler o arquivo de texto links.txt, verificando se os itens da lista self.l já se encontram no arquivo. Caso não se encontrem no arquivo, serão salvos nele.
17

  A função parse fará a busca do termo nas bases, adicionará cada link à lista self.l e, por fim, acionará a função self.links_to_txt.
Portanto, esta classe funcionará da seguinte forma:
>>> query = ‘termo_de_busca_exemplo’
>>> results = n #sendo que type(n) == int >>> q = Query(query, results)
>>> q.parse()
Sendo que, com isso, retornarão todos os links encontrados, além de serem salvos no arquivo de texto links.txt.
 18

 A segunda classe se chama PdfText. Esta classe deverá ser utilizada uma vez que os artigos acadêmicos estejam salvos em uma pasta. Aqui, temos seis variáveis. A primeira é a variável self.d, que é um dicionário no qual ficarão armazenadas as frequências de palavras de todos os artigos. A segunda é a variável self.sub_dir, uma lista das subpastas (presentes na pasta previamente definida pela variável dir). A terceira é a variável self.files, que é uma lista de todos os arquivos com os quais trabalharemos. A quarta é a variável self.PTS, dicionário contendo a pontuação de cada artigo. A quinta é a variável self.pageObj, que será atualizada com o texto extraído de cada artigo.
A sexta e última é a variável self.fim, um dicionário já organizado em ordem crescente de pontuação, com as informações finais relacionadas a cada artigo.
A função prep serve primeiro para encontrar os arquivos .pdf em uma pasta dir anteriormente definida. Em seguida, para cada arquivo file encontrado na lista self.files, será acionada a função pdf_txt.
A função pdf_txt, a partir de um arquivo vinculado à variável file, serve para extrair o conteúdo de um arquivo .pdf, em seguida criar um dicionário count contendo as frequências de palavras e, por fim, atualizar o dicionário self.d com as informações do dicionário count.
  19

  A função cont será útil para: (1) tornar o conteúdo de texto extraído mais limpo, e (2) calcular a pontuação de cada artigo. É preciso, para utilizá-la, definir a pasta com a qual se quer trabalhar, por meio da variável dir. Em seguida, a função prep é acionada e o conteúdo dos arquivos .pdf, extraído. Por fim, é calculada a pontuação de cada artigo, atualizando de um em um o dicionário self.PTS.
 20

 Por fim, a função pts_files, com uma pasta dir definida, será utilizada para organizar os artigos com base na pontuação. Primeiro, a função cont é acionada. A partir daí, com toda a informação obtida, os artigos são ordenados em ordem crescente de pontuação.
Portanto, o uso da classe se dá da seguinte forma: >>> dir = ‘Pasta/‘
>>> pdf = PdfText() >>> pdf.pts_files(dir)
Código – versão 3.1
A única mudança em relação à versão 3.0 é que, agora, na função pts_files, foi adicionado no fim do processo a criação de um arquivo .csv com os dados de pontuação de cada artigo em ordem crescente.
Código – versão 3.2 (atual)
Esta versão, em relação à versão anterior, teve somente uma atualização: a classe Query foi atualizada para realizar uma busca mais refinada e precisa. É a versão atual, mas que ainda pode ser melhorada no futuro próximo.
Abaixo, segue o código da versão 3.2 completo:
 21

  A primeira imagem consiste nos imports e na classe Query. Já a segunda imagem consiste somente na classe PdfText.
22

 23

 4. Usos e funcionamento
Agora é o momento de nos debruçarmos sobre o funcionamento do código e sua utilização, na versão 3.2. É necessária a versão 3.7 do Python, bem como algumas bibliotecas específicas instaladas.
Primeiro, abrimos o Terminal e entramos no Python:
Em seguida, importamos o programa:
Dessa forma, tornamos possível a utilização das classes Query e PdfText, bem como habilitamos o uso das seguintes bibliotecas:
É preciso entender o que cada uma faz:
- BeautifulSoup: é uma biblioteca que funciona com o objetivo de extrair e formatar dados de
html e xml; será utilizado em conjunto com a biblioteca requests para que seja possível fazer a
busca de termos nas bases de dados;
- requetss: esta biblioteca tem a função de requisitar o acesso a uma página da internet e, a partir
daí, possibilita a extração do material bruto contido na página, o que torna necessária a utilização
da biblioteca BeautifulSoup para tornar este material compreensível;
- os:estaéumabibliotecaquejáéautomaticamenteinstaladacomoPython;elaservirá,aqui,para
acessarmos o conteúdo de uma pasta definida;
   24

 - PyPDF2: é uma biblioteca que permite extrair dados de arquivos .pdf; será útil para que se possa obter a informação dos arquivos .pdf referentes aos artigos acadêmicos;
- Counter: é uma subclasse que permitirá fazer a contagem da frequência de palavras de cada artigo acadêmico;
- math: esta biblioteca será útil para, em conjunto com a biblioteca numpy, ser feita a pontuação de cada artigo acadêmico;
- numpy: é uma biblioteca que tem a funcionalidade de trabalhar com números em Python, e servirá para, em conjunto com a biblioteca math, fazer a pontuação de cada artigo acadêmico.
Estas são as bibliotecas habilitadas ao se importar o programa. Em seguida, recomenda-se começar trabalhando com a classe Query, para obter os links dos artigos acadêmicos. Para se utilizar esta classe, é necessário primeiro definir um termo de busca vinculado à variável query, e o número de resultados encontrados em cada uma das bases, vinculado à variável results. Como exemplo, buscaremos o termo ‘Bakhtin’, autor com o qual estou trabalhando em meu Trabalho de Conclusão de Curso, com 10 resultados para cada base:
Aqui, definimos as variáveis e estamos prontos para buscarmos os resultados do Google Scholar e SciELO. Criamos o objeto q, que aciona a função __init__ dentro da classe Query e define as variáveis com as quais trabalharemos.
Por fim, para retornar todos os resultados encontrados, um por um, basta fazer da seguinte maneira:
Desse modo acionamos a função parse da classe Query:
   25

  Esta função age do seguinte modo: enquanto self.results for maior que 0, continuará buscando nas páginas os links para os artigos acadêmicos. A variável url_a e a variável url_b estão vinculadas, respectivamente, às urls de busca do Google Scholar e do SciELO. Em seguida, extrai-se os dados html das páginas em busca dos links para os artigos em .pdf. Depois, são retornados os links na tela, bem como salvos em um documento de texto .txt, como se segue:
26

 a) item por item aparecem na tela:
27

 b) Documento de texto:
 Agora, uma vez que já foram baixados os arquivos .pdf referentes a cada artigo acadêmico e, em seguida, foram salvos em uma pasta, vamos trabalhar com a classe PdfText para fazer a classificação de texto. Primeiro, é necessário vincular a classe a um objeto pdf:
 
Aqui, criamos o objeto pdf, acionando a função __init__ da classe PdfText:
  28

 Então, buscamos a pasta na qual estão salvos os artigos. No exemplo, a pasta escolhida na realidade será a subpasta ‘2009:1/‘, presente na pasta ‘Bakhtiniana/' (é importante notar que, caso haja o caractere “/“ no nome do arquivo, deve ser substituído pelo caractere “:”, uma vez que o caractere “/“ serve para indicar a existência de uma pasta). Por sua vez, a pasta ‘Bakhtiniana/‘ já se encontra no diretório no qual estamos trabalhando, então basta definir a variável dir do seguinte modo:
É importante lembrar que o programa irá buscar primeiramente por subpastas na pasta indicada, e somente depois fará a busca por arquivos .pdf. Caso não encontre subpastas, seguirá direto para o segundo passo, buscando os arquivos .pdf na pasta indicada.
Agora, é um pouco complexo o funcionamento da classe PdfText. Primeiro, utilizamos a função pts_files, que acionará a função cont para realizar todos os processos (descritos mais à frente) e, com os resultados, ordenar os artigos em ordem crescente de pontuação e, por fim, vai criar um arquivo .csv com a relação artigo/pontuação, em ordem crescente. A função é a seguinte:
  Como já criamos o objeto pdf a partir da classe PdfText, bem como criamos a variável dir para indicar a pasta com a qual trabalharemos, basta agora fazer como se segue:
O resultado, então, será o seguinte:
 29

  Além de ser criado o arquivo .csv com as informações acima:
É preciso observar que, no prompt de comando do terminal, os nomes dos arquivos são acompanhados de um “OK”. Isso se dá por causa das outras funções presentes na classe PdfText, que estão extraindo as informações e, então, confirmando a realização do processo. Como foi observado, a primeira ação da função pts_files é acionar a função cont, aguardar a obtenção dos dados e, então, realizar os processos subsequentes.
A função cont, ao ser acionada, primeiro , aciona a função prep. Então, elimina as palavras curtas do dicionário self.d. Depois, lê todos os arquivos file na lista self.files e elimina palavras e caracteres desnecessários, calcula a frequência de palavras em cada arquivo e por fim pontua cada arquivo a partir de uma fórmula.
 30

  A função prep, primeiro, cria uma lista com todos os arquivos .pdf na pasta indicada dir. Caso no lugar de arquivos .pdf haja subpastas, será acessada cada pasta em busca de arquivos .pdf. Por fim, para cada arquivo file na lista self.files, será acionada a função pdf_txt.
31

  A função pdf_txt, então, serve para ler os arquivos .pdf, página por página, e então fazer a contagem de frequência por meio da função Counter. Então, o dicionário self.d é atualizado com as informações. Este dicionário será utilizado para relacionar a frequência de palavras dos arquivos individuais à frequência de palavras do conjunto de arquivos com os quais estivermos trabalhando.
É importante chamar atenção para um detalhe. A fórmula que se encontra na função cont serve para calcular a pontuação de cada artigo com base na frequência de palavras. Ela funciona tendo em vista, também, a frequência total de palavras do conjunto de artigos. Então, a pontuação de um artigo se dá com base na frequência de palavras do artigo em relação à frequência de palavras do conjunto de artigos.
 32

  Além disso, a fórmula que se encontra na função pts_files serve para calcular a pontuação média de todos os artigos. Com isso, juntamente com a pontuação de cada artigo, haverá uma porcentagem relativa à comparação entre a pontuação de cada artigo e a média de pontuação geral.
5. Conclusão
A partir do que foi exposto, pode-se perceber que o código em sua versão 3.2 ainda não está finalizado. Muitos aspectos ainda podem ser otimizados para torná-lo mais leve e eficiente, além de ser necessária a implementação de uma ponte entre as duas classes, que a partir dos links extraídos com a classe Query se possa fazer a classificação de texto dos artigos acadêmicos por meio da classe PdfText.
O presente trabalho, portanto, é a demonstração do início de um projeto que deve ter continuidade no futuro, tendo em vista estas melhorias, dentre outras. Sua função original, de auxiliar no estudo para o Trabalho de Conclusão de Curso do curso de Comunicação Social da Universidade de Brasília, cumpriu com seu objetivo. Porém, o processo mostrou que, por um lado, seria um projeto maior e mais trabalhoso do que se esperava e, por outro, mostrou ser de maior abrangência do que inicialmente previsto. Este último ponto foi a motivação para escrever este trabalho, visto que a intenção para este projeto no futuro é difundi-lo o mais possível, uma vez que pode ser utilizado por qualquer estudioso ou acadêmico, não se limitando ao curso de Comunicação Social, muito menos a um Trabalho de Conclusão de Curso.
 33

 6. Anexo
Aqui temos o algoritmo do código:
REFERÊNCIAS BIBLIOGRÁFICAS
LUTZ, Mark. Learning Python. 5 ed. O’Reilly Media, 2013.
SITE CRUMMY. Beautiful Soup Documentation. Disponível em: <https://www.crummy.com/ software/BeautifulSoup/bs4/doc/> Acesso em: 6 de Dezembro de 2018.
SITE NUMPY. NumPy. Disponível em: <http://www.numpy.org> Acesso em: 6 de Dezembro de 2018.
SITE PYTHON. python.org. Disponível em: <https://www.python.org> Acesso em: 6 de Dezembro de 2018.
SITE PYTHONHOSTED. PyPDF Documentation. Disponível em <https://pythonhosted.org/ PyPDF2/> Acesso em 6 de Dezembro de 2018.
SITE REQUESTS. Requests: HTTP for Humans. Disponível em <http://docs.python- requests.org/en/master/> Acesso em: 6 de Dezembro de 2018.
          34
