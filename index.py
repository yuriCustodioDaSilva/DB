import os

def createDB():
    name_db = input("Digite o nome do seu DB: ")
    dir = "./" + name_db       
    os.makedirs(dir)
    print(f"Banco de dados '{name_db}' criado com sucesso!")

def createTable(dbName):
    name_table = input("Digite o nome da sua tabela: ")
    arquivo = open("./" + dbName + "/" + name_table + ".csv", "w")
    name_colunns = input("Digite o nome das colunas separadas por vírgula (ex: nome,idade...):\n")
    arquivo.write("id," + name_colunns)  
    arquivo.close()
    print(f"Tabela '{name_table}' criada com sucesso no banco '{dbName}'!")

def viewTable(dbName):
    name_table = input("Digite o nome da tabela que deseja consultar: ")
    file_path = "./" + dbName + "/" + name_table + ".csv"
    
    if os.path.exists(file_path):
        with open(file_path, "r") as arquivo:
            content = arquivo.read()
            print(f"Conteúdo da tabela '{name_table}':\n{content}")
    else:
        print(f"A tabela '{name_table}' não existe no banco '{dbName}'.")

def addItem(dbName):
    name_table = input("Digite o nome da tabela onde deseja adicionar itens: ")
    file_path = "./" + dbName + "/" + name_table + ".csv"

    if os.path.exists(file_path):
        with open(file_path, "r") as arquivo:
            linhas = arquivo.readlines()

        colunas = linhas[0].strip().split(",")
        data = linhas[1:]
   
        if data:
            ultimo_id = int(data[-1].split(",")[0])  
        else:
            ultimo_id = 0
        
        novo_id = ultimo_id + 1  
        
        valores = []
        for coluna in colunas[1:]:  
            valor = input(f"Digite o valor para {coluna}: ")
            valores.append(valor)
        
        nova_linha = f"{novo_id}," + ",".join(valores) + "\n"  
        with open(file_path, "a") as arquivo:
            arquivo.write(nova_linha)

        print(f"Item adicionado à tabela '{name_table}' com sucesso!")
    else:
        print(f"A tabela '{name_table}' não existe no banco '{dbName}'.")


while True:
    acao = input("Olá, o que faremos hoje?\n1 - Criar um banco\n2 - Criar uma tabela\n3 - Consultar uma tabela\n4 - Adicionar itens à tabela\n5 - Sair\nEscolha uma opção: ")

    if acao == '1':
        createDB()
    elif acao == '2':
        dbName = input("Digite o nome do banco de dados onde deseja criar a tabela: ")
        if os.path.exists("./" + dbName):
            createTable(dbName)
        else:
            print(f"O banco de dados '{dbName}' não existe!")
    elif acao == '3':
        dbName = input("Digite o nome do banco de dados para consultar a tabela: ")
        if os.path.exists("./" + dbName):
            viewTable(dbName)
        else:
            print(f"O banco de dados '{dbName}' não existe!")
    elif acao == '4':
        dbName = input("Digite o nome do banco de dados onde deseja adicionar itens: ")
        if os.path.exists("./" + dbName):
            addItem(dbName)
        else:
            print(f"O banco de dados '{dbName}' não existe!")
    elif acao == '5':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
