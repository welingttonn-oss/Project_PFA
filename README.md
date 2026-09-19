Projeto iniciado em 29/08 

Personal Finance Automation (PFA)

Objetivo geral:
    Criar um sistema desktop que, de forma automática ou manual, coleta cotações de ativos financeiros (ações, moedas, criptomoedas) a partir de uma API pública gratuita, armazena os dados em um banco de dados local, gera planilhas e gráficos com indicadores (média, variação, máximos/mínimos) e envia um resumo por e-mail periodicamente.

Por que este projeto atende a todos os seus interesses?

    Automação web/API: coleta de dados financeiros via API gratuita (ex.: AwesomeAPI, Yahoo Finance, Alpha Vantage).
    Planilhas/relatórios: geração de Excel com pandas/openpyxl.
    E-mail: envio programado de relatório diário/semanal.
    Arquivos locais: organização de relatórios em pastas.
    Integração entre sistemas: API + banco SQLite.
    Agendamento: execução automática com biblioteca schedule ou Agendador de Tarefas do Windows.
    Interface gráfica: janela com Tkinter para configuração e acionamento manual.
    Executável: transformar em .exe com PyInstaller.
    Dashboard/relatório: gráficos gerados com matplotlib e planilhas formatadas.

Diário/Cronograma de aprendizado:
29/08/2026:
    Aprendizado:
    Aprendi o que é git e github, aprendi usar o desktop github
    Relembrei sobre funções, aprendi a estruturar pastas, aprendi sobre o main.py
        main:
            utilizo para executar as funções criadas e salvas no src/uteis, passando os parametros e recebendo os resultado. Já na src/uteis, devem estar só a função em si, não deve executa-las lá, caso contrario dará erro.
    Vnev eu já sabia, mas, de fato aprendi a importar se pesquisar nas IA.
    Gitignore serve para avisar o git o que não versionar.
    requeriments serve para salvar as versões dos PIPs instalados no venv
        script para uso: pip freeze > requirements
    Dificuldades:
    Maior dificuldade foi o git hub, porém, consegui me adaptar com o desktop e agora consigo fazer os commit tranquilamente.
30/08/2026:
    Iniciando no aprendizado sobre API que estão uma forma de integrar com outros sistemas usando um json.
    aprendi que precisamos iniciar a URL e fazer uma função que traga retornos expecificos, caso necessários.
    Dificuldades:
    no exercicio tanto a URL quando a chave principal era nomes parecidos, isso ocorreu um erro que demorei a entender. além disso, também entendi que necesses casos usar o replace ajuda a tirar o caracter que não seria necessário. além de usar os metodos upper e split para tratar o retorno do usuário. poderia utilizar o try/except mais como é uma exercicio para o futuro achei melhor deixa-lo para depois.

10/09/2026:
    Tratamento de erros em chamadas de API:
    Quando necessário fazer um teste de API se está respondendo:
        Devemos fazer um try/except:
	        Primeiro no response
            Se der erro usar o requestis.exceptions
        Se e a moeda der erro
	    except KeyError
    Outro ponto:
	    Quando a função devolve duas variaveis, e a chamada de função  usar no excpet o None None e sempre validar se o resultado das duas não são None.
    .ENV dando segurança a dados sensiveis.
        Aprendi que o .env serve para esconder dados sensiveis, nas quais não podem ser vazados.
        Como usar:
            criar um arquivo .env
            criar suas variaveis que devem ser escondidas
                como:
                    dados=a,b,c
                    note que esses dados estão sem espaço separados por virgulas.
        Como chamar no projeto?
            Importar 
                import os
                from dotenv import load_dotenv - criar o acionamento
                load_dotenv() - acionar o acionamento.

                Dados = os.getenv('dados')
    **BÁSCICO**:
        pronto importante, basico mas, as vezes esqueço:
        para separar uma string por um caracter especifico, usa-se split e o replace serve para substituir um por outro.

11/09/2026
    Trabalhando com API:
    Tive de criar uma função que busca o valor de um ATIVO, especifico. já havia feito algo parecido com a da moeda, então foi mais tranquilo.
    Dificuldades:
        Yahoofinance bloquea acessos de bot, então tive de usar:
             headers: User-Agent -> simula um navegador
    Aprendi:
        que não basta você passar a chave que você quer acessar para imprimr, se quero acessar a C4, preciso chegar até ela:
        c1,c2,c3,"Nome da chave";

12/09/2026:
    Trabalhando com modulariação e chamadas sob chamadas de funções:

    Aprendi: quando a API está demorando usar um timeout, para não ficar muito tempo esperando um retorno da API
    Sempre usar as melhores praticas de nomes de variaveis.
    usar dicionário para retornos multiplos da url

    Criar DEFs que chamam DEVS
    fazer validação do retorn com is not, pois fizemos um tratamento de dados nas def, daí ela retorna sempre None caso erro.
    Relembrei:
    utilizar as dotenv, tinha esquecido como, mas sempre:
    from dotenv import load_dotenv e import OS usar o OS para chamar o arquivo getenv
13/09/2026:
    Trabalhando com  Loggings:
        Loggins serve para criar o "print" funcinal, que é muito mais util, pois, ele guarda a execução, possiveis problemas em um local que armazenaremos para entender a execução do sistema.
        Loggins temos os estudados: DEBUG, INFO, WARNNING, ERROR E CRITICAL
            Cada um deles tem uma finalidade, devemos sempre analisar.
        a formatação do arquivo de logging deve ser apenas no main.py e não duplicado nos arquivos, uma vez criado, seguirá desta forma.
    Introdução ao SQLite3
        Aprendi a criar um banco, uma tabela e acrescentar dados. carece de se aprofundar mais.
15/09/2026:
	Aprendizado: 3 funções de manipulação no SQL (Criar, alimentar e retornar dados). 
	Novamente: logging só configura uma vez. Ainda estou apanhando com os códigos de SQL, estou precisando focar sem pedir tanta ajuda da IA, mas a ideia primária é entender o conceito e ir treinando até melhorar.
	O mais importante: estava apanhando pra ver os dados sendo alimentado na tabela e o código não quebrava, mas não aparecia nada, depois o Seek me explicou e batata: SEMPRE OLHE O LOGGING, afinal, ele é criado para isso mesmo.
	Try, except e finnaly, foi introduzido o finnaly, que serve para certificar que será finalizado. No conceito de SQL é super importante a necessidade de fechar o banco.
    
18/09/2026:
    Aprendizado:
        Conecação com o banco e chamada de API salvando automatico no banco. Usei a função criar tabela, depois, peguei as funções de buscar os dados na API e salvar em um dicionario, depois peguei a função de salvar no banco de dados e passei esse dicionário para lá.
        Melhorar o looging para rastrear tudo, ficar de olho nos erros de digitação e diferença entre '' e "", possiveis erros.
    Dificuldade:
        Estava pegando o nome do ativo e tentando salvar no banco, acontece que não era o correto, e sim o resultado que a função de buscar os dados devolvia uma tabela padronizada.

/// DOCUMENTAÇÃO DE FUNCIONAMENTO ATUAL F1-E13 ///
Como iniciar:
    python main.py
    Pra que serve:
    Programa para obter dados de Moedas ou Ativos financeiros:
    Como funciona:
    Função de Obter dados consulta item a item nas APIs, valida qual buscar se ativo ou moeda, retorna um dicionario que é salvo no SQLite.
    Documentos:
        coleta.py: Funções necessárias para coletar os dados.
        db.py: Funções de criar e alimentar os dados
        coleta.log: gravações de logs de acompanhamento.
    Resultados:
        financas.db: todas cotações pesquisadas salvas

19/09/2026:
/// DOCUMENTAÇÃO DE FUNCIONAMENTO F1-E14/// 
    Personal Finance Automation (PFA)
        Sistema desktop que coleta cotações de moedas e ações de APIs públicas gratuitas, armazena em banco de dados local e (futuramente) gerará relatórios e envios por e-mail.

    🚀 Como iniciar
        Ative o ambiente virtual:

    text
        venv\Scripts\activate
        Execute o programa:

    text
    python main.py
        ⚙️ Como funciona
        O programa percorre a lista de ativos definida no .env, consulta cada um nas APIs (AwesomeAPI para moedas, Yahoo Finance para ações), padroniza o retorno em um dicionário e salva no banco SQLite.

    Fluxo resumido:

        text
        .env → coleta (API) → dicionário padronizado → banco (SQLite) → log
    📂 Estrutura do projeto
        Arquivo/Pasta	Descrição
        main.py	Arquivo principal (maestro). Orquestra tudo.
        src/coleta.py	Funções de coleta nas APIs.
        src/db.py	Funções de banco de dados (criar, salvar, listar).
        dados/financas.db	Banco de dados com as cotações coletadas.
        logs/coleta.log	Registro de execução (sucessos, falhas, erros).
        .env	Configurações sensíveis (ativos, e-mail).
        requirements.txt	Dependências do projeto.
    📋 Configuração (.env)
        Crie um arquivo .env na raiz com:

        text
        ATIVOS=USD-BRL,EUR-BRL,BTC-BRL,PETR4.SA,VALE3.SA
        EMAIL_DESTINATARIO=seuemail@exemplo.com
        ⚠️ O .env está no .gitignore e não deve ser versionado.

    📊 Resultados
        Banco de dados: dados/financas.db (abra com SQLite Viewer para inspecionar).

        Log de execução: logs/coleta.log.

    🛠️ Tecnologias usadas
        Python 3.12+

        requests (requisições HTTP)

        sqlite3 (banco de dados)

        python-dotenv (variáveis de ambiente)

        logging (registro de execução)

    📌 Status do projeto
        Fase 1 – Módulo de Coleta em andamento (reta final).
        Próximas fases: processamento/relatórios (pandas + Excel), envio por e-mail, agendamento, interface gráfica e empacotamento em .exe.


