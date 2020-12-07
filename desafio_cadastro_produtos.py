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
    """
    Solicita dados do produto, a classe Produto com os dados
    :return: objeto prod
    """
    nome = input("Informe o nome do produto: ")
    categoria = input("Informe a categoria do produto: ")
    descricao = input("Informe a descrição do produto: ")
    while True:
        try:
            preco = float(input("Informe o preco do produto: "))
            break
        except ValueError:
            print("O preço deve ser um numero decimal usando ponto como separador,\ninforme novamente... ")
    prod = Produto(nome, categoria, descricao, preco)
    return prod


def maior_indice(lista_de_produtos_index):
    """
    Busca por maior indice na lista para que cada produto tenha um id unico
    :param lista_de_produtos_index: lista de produtos existentes
    return: var_aux que é o maior indice unico da lista
    """
    var_aux = 1
    for i in range(len(lista_de_produtos_index)):
        if lista_de_produtos_index[i][0] >= var_aux:
            var_aux = lista_de_produtos_index[i][0] + 1
    return var_aux


def salva_produto(Produto, lista_de_produtos):
    """
    Recebe o objeto produto e a lista com os produtos
    :param Produto: objeto produto
    :param lista_de_produtos: lista com produtos salvos
    :return: lista_de_produtos que é a lista atualizada
    """
    p = Produto
    lista_aux = [maior_indice(lista_de_produtos)]
    desc_produto = {
        'Nome': p.get_nome().capitalize(),
        'Categoria': p.get_categoria().capitalize(),
        'Descrição': p.get_descricao().capitalize(),
        'Preço': p.get_preco()}
    lista_aux.append(desc_produto)
    return lista_de_produtos.append(lista_aux)


def listando_produtos(lista_de_produtos):
    """
    Ordena e imprime lista de produtos.
    :param lista_de_produtos
    """
    lista_ordenada = sorted(lista_de_produtos)
    for produto in range(len(lista_ordenada)):
        id = lista_ordenada[produto][0]
        produto = lista_ordenada[produto][1]
        print(f"id: {id}\nNome: {produto['Nome']}\nCategoria: {produto['Categoria']}\nDescrição: {produto['Descrição']}"
              f"\nPreço: {produto['Preço']}")
        print('-----------------------------')


def remove_produto(indice, lista):
    """
    Exclui o produto com id informado pelo usuário
    :param indice: inteiro informado pelo usuário
    :param lista: lista com produtos cadastrados
    :return: lista atualizada
    """
    for i in range(len(lista)):
        if lista[i][0] == indice:
            lista.pop(i)
            break
    return lista_de_produtos


def atualiza_produto(indice, lista):
    """
    Atualiza o produto com id informado pelo usuário
    :param indice: inteiro informado pelo usuário
    :param lista: lista com produtos cadastrados
    :return: lista atualizada
    """
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
    """
    Fica em loop até que uma opção válida seja escolhida
    :return:opção escolhida
    """
    while True:
        try:
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
            if opcao not in(1, 2, 3, 4, 5):
                print("Opção inexistente, escolha entre 1 e 5...")
                pass
            else:
                break
        except ValueError:
            print("Ooops! Valor inválido! Digite novamente um número entre 1 e 5...")
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
