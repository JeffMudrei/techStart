class Produto:

    def __init__(self, nome, categoria, descricao, preco):
        self.__nome = nome
        self.__categoria = categoria
        self.__descricao = descricao
        self.__preco = preco

    def set_nome(self, nome) -> None:
        self.__nome = nome

    def set_categoria(self, categoria) -> None:
        self.__categoria = categoria

    def set_descricao(self, descricao) -> None:
        self.__descricao = descricao

    def set_preco(self, preco) -> None:
        self.__preco = preco

    def get_nome(self) -> str:
        return self.__nome

    def get_descricao(self) -> str:
        return self.__descricao

    def get_categoria(self) -> str:
        return self.__categoria

    def get_preco(self) -> str:
        return self.__preco


def cria_produto():
    nome = input("Informe o nome do produto: ")
    categoria = input("Informe a categoria do produto: ")
    descricao = input("Informe a descrição do produto: ")
    preco = float(input("Informe o preco do produto: "))
    prod = Produto(nome, categoria, descricao, preco)
    return prod


def maior_indice(lista_de_produtos_index):
    var_aux = 1
    for i in range(len(lista_de_produtos_index)):
        if lista_de_produtos_index[i][0] >= var_aux:
            var_aux = lista_de_produtos_index[i][0] + 1
    return var_aux


def salva_produto(Produto, lista_de_produtos):
    p = Produto
    lista_aux = [maior_indice(lista_de_produtos)]
    desc_produto = {
        'Nome': p.get_nome(),
        'Categoria': p.get_categoria(),
        'Descrição': p.get_descricao(),
        'Preço': p.get_preco()}
    lista_aux.append(desc_produto)
    return lista_de_produtos.append(lista_aux)


def listando_produtos(lista_de_produtos):
    lista_ordenada = sorted(lista_de_produtos)
    for produto in lista_ordenada:
        print(produto)


def remove_produto(indice, lista):
    for i in range(len(lista)):
        if lista[i][0] == indice:
            lista.pop(i)
            break
    return lista_de_produtos


def atualiza_produto(indice, lista):
    remove_produto(indice, lista)
    produto_atualizado = cria_produto()
    desc_produto = {
        'Nome': produto_atualizado.get_nome(),
        'Categoria': produto_atualizado.get_categoria(),
        'Descrição': produto_atualizado.get_descricao(),
        'Preço': produto_atualizado.get_preco()
    }
    lista_aux = [indice, desc_produto]
    return lista.append(lista_aux)


def menu_inicial():
    print("""
            +-----------------------------------+
            |	olist - Cadastro de produtos	|
            +-----------------------------------+						
            |	1 - Cadastrar produtos			|
            |	2 - Listar produtos				|
            |	3 - Atualizar produtos			|
            |	4 - Excluir produtos			|
            |	5 - Encerrar					|
            +-----------------------------------+""")
    opcao = int(input("             >>> "))
    return opcao


def controle():
    op = menu_inicial()
    while op != 5:
        if op == 1:
            salva_produto(cria_produto(), lista_de_produtos)
            op = menu_inicial()
        elif op == 2:
            listando_produtos(lista_de_produtos)
            op = menu_inicial()
        elif op == 3:
            listando_produtos(lista_de_produtos)
            indice = int(input("Informe o id do produto: "))
            atualiza_produto(indice, lista_de_produtos)
            op = menu_inicial()
        elif op == 4:
            listando_produtos(lista_de_produtos)
            indice = int(input("Informe o id do produto: "))
            remove_produto(indice, lista_de_produtos)
            op = menu_inicial()
    print("Até logo!")


lista_de_produtos = []
controle()
