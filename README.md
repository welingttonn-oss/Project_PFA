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