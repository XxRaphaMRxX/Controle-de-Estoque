import csv
import os

# Nome do arquivo de armazenamento
ARQUIVO_ESTOQUE = 'estoque.csv'

# Função para inicializar o arquivo de estoque
def inicializar_arquivo():
    if not os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nome', 'Quantidade', 'Preço'])  # Cabeçalhos

# Função para listar todos os produtos
def listar_produtos():
    with open(ARQUIVO_ESTOQUE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        print(f'{"ID":<5} {"Nome":<20} {"Quantidade":<10} {"Preço":<10}')
        for linha in reader:
            print(f'{linha[0]:<5} {linha[1]:<20} {linha[2]:<10} {linha[3]:<10}')

# Função para gerar automaticamente o próximo ID
def gerar_novo_id():
    ultimo_id = 0
    with open(ARQUIVO_ESTOQUE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for linha in reader:
            ultimo_id = int(linha[0])
    return ultimo_id + 1

# Função para adicionar um produto ao estoque com ID automático
def adicionar_produto():
    with open(ARQUIVO_ESTOQUE, mode='a', newline='') as file:
        writer = csv.writer(file)
        id_produto = gerar_novo_id()
        nome_produto = input("Nome do produto: ")
        quantidade_produto = input("Quantidade: ")
        preco_produto = input("Preço: ")
        writer.writerow([id_produto, nome_produto, quantidade_produto, preco_produto])
    print("Produto adicionado com sucesso!")

# Função para buscar um produto por ID
def buscar_produto(id_produto):
    with open(ARQUIVO_ESTOQUE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for linha in reader:
            if linha[0] == id_produto:
                return linha
    return None

# Função para atualizar as informações de um produto
def atualizar_produto():
    id_produto = input("Digite o ID do produto a ser atualizado: ")
    produto = buscar_produto(id_produto)
    if produto:
        print(f'Produto encontrado: {produto[1]} - Quantidade: {produto[2]}, Preço: {produto[3]}')
        nova_quantidade = input("Nova quantidade: ")
        novo_preco = input("Novo preço: ")
        atualizar_arquivo(id_produto, nova_quantidade, novo_preco)
    else:
        print("Produto não encontrado.")

# Função para atualizar o arquivo com as novas informações
def atualizar_arquivo(id_produto, nova_quantidade, novo_preco):
    linhas = []
    with open(ARQUIVO_ESTOQUE, mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] == id_produto:
                linha[2] = nova_quantidade
                linha[3] = novo_preco
            linhas.append(linha)
    with open(ARQUIVO_ESTOQUE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(linhas)
    print("Produto atualizado com sucesso!")

# Função para remover um produto do estoque
def remover_produto():
    id_produto = input("Digite o ID do produto a ser removido: ")
    linhas = []
    produto_encontrado = False
    with open(ARQUIVO_ESTOQUE, mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] != id_produto:
                linhas.append(linha)
            else:
                produto_encontrado = True
    if produto_encontrado:
        with open(ARQUIVO_ESTOQUE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(linhas)
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")

# Função para exibir o valor total do estoque
def valor_total_estoque():
    total = 0
    with open(ARQUIVO_ESTOQUE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for linha in reader:
            quantidade = int(linha[2])
            preco = float(linha[3])
            total += quantidade * preco
    print(f"Valor total do estoque: R${total:.2f}")

# Função principal do menu
def menu():
    inicializar_arquivo()
    while True:
        print("\n--- Controle de Estoque ---")
        print("1. Listar todos os produtos")
        print("2. Adicionar um produto")
        print("3. Atualizar um produto")
        print("4. Remover um produto")
        print("5. Exibir valor total do estoque")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            adicionar_produto()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            remover_produto()
        elif opcao == '5':
            valor_total_estoque()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
1