class Categoria:
    def __init__(self, nome, id_categoria):
        self.__nome: str = nome
        self.__id_categoria: int = id_categoria

    def set_nome_categoria(self, nome) -> None:
        self.__nome = nome

    def set_id_categoria(self, id_categoria) -> None:
        self.__id_categoria = id_categoria

    def get_id_categoria(self) -> int:
        return self.__id_categoria

    def get_nome_categoria(self) -> str:
        return self.__nome


class Produto:
    def __init__(self, nome, categoria, subcategoria, descricao, preco, peso, largura, altura, profundidade):
        self.__nome: str = nome
        self.__categoria: str = categoria
        self.__subcategoria: str = subcategoria
        self.__descricao: str = descricao
        self.__preco: float = preco
        self.__peso: float = peso
        self.__altura: float = altura
        self.__largura: float = largura
        self.__profundidade: float = profundidade

    def set_largura(self, largura) -> None:
        self.__largura = largura

    def get_largura(self) -> float:
        return self.__largura

    def set_profundidade(self, profundidade) -> None:
        self.__profundidade = profundidade

    def get_profundidade(self) -> float:
        return self.__profundidade

    def set_altura(self, altura) -> None:
        self.__altura = altura

    def get_altura(self) -> float:
        return self.__altura

    def set_subcategoria(self, subcategoria) -> None:
        self.__subcategoria = subcategoria

    def get_subcategoria(self) -> str:
        return self.__subcategoria

    def set_peso(self, peso) -> None:
        self.__peso = peso

    def get_peso(self) -> float:
        return self.__peso

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

    def get_preco(self) -> float:
        return self.__preco


def cria_categoria(lista) -> Categoria:
    """
    Solicita nome e id de categoria, valida como categoria ou subcategoria
    :return: objeto categoria.
    """
    print("Categorias já cadastradas: ")
    imprime_categoria(0, lista)
    while True:
        nome = input("Informe o nome da categoria:").capitalize()
        try:
            id_cat = int(input("[1] - Categoria\n[2] - Subcategoria \n>>> "))
            if id_cat == 1 or id_cat == 2:
                print('Cadastrando...')
                break
        except ValueError:
            print("Informe um valor válido")

    c = Categoria(nome, id_cat)
    return c


def salva_categoria(Categoria, lista_categorias):
    c = Categoria
    nome = c.get_nome_categoria().capitalize()
    id = c.get_id_categoria()
    return lista_categorias.append([id, nome])


def verifica_categoria_existente(nome, lista_categorias) -> bool:
    for i in range(len(lista_categorias)):
        if lista_categorias[i][1] == nome:
            return False
        else:
            return True


def atualiza_categoria():
    # todo
    pass


def exclui_categoria():
    # todo
    pass


def imprime_categoria(opcao, lista_categorias):
    lista_ordenada = sorted(lista_categorias)
    if opcao == 1:
        for i in range(len(lista_ordenada)):
            if lista_ordenada[i][0] == 1:
                print(f'id: {lista_ordenada[i][0]} - Nome {lista_ordenada[i][1]}')
    elif opcao == 2:
        for i in range(len(lista_ordenada)):
            if lista_ordenada[i][0] == 2:
                print(f'id: {lista_ordenada[i][0]} - Nome {lista_ordenada[i][1]}')
    else:
        for i in range(len(lista_ordenada)):
            print(f'id: {lista_ordenada[i][0]} - Nome {lista_ordenada[i][1]}')


def cria_produto(lista_categorias) -> Produto:
    """
    Solicita dados do produto, a classe Produto com os dados
    :return: objeto prod
    """
    nome = input("Informe o nome do produto: ")
    print("Categorias cadastradas:")
    imprime_categoria(1, lista_categorias)
    while True:
        categoria = input("Informe uma categoria existente:")
        if verifica_categoria_existente(categoria, lista_categorias):
            break
    imprime_categoria(2, lista_categorias)
    while True:
        subcategoria = input("Informe uma subcategoria existente:")
        if verifica_categoria_existente(subcategoria, lista_categorias):
            break
    while True:
        descricao = input("Informe a descrição do produto com pelo menos 20 caracteres: ")
        if len(descricao) >= 20:
            break
    while True:
        try:
            preco = float(input("Informe o preco válido do produto: "))
            if preco > 0:
                break
        except ValueError:
            print("O preço deve ser um numero decimal usando ponto como separador,\ninforme novamente... ")
    while True:
        try:
            peso = float(input("Informe o peso válido do produto em kg: "))
            if peso > 0:
                break
        except ValueError:
            print("Informe um valor valido para o peso\ninforme novamente... ")
    while True:
        try:
            largura = float(input("Informe a largura do produto em cm: "))
            if largura > 0:
                break
        except ValueError:
            print("Informe um valor valido para a largura\ninforme novamente... ")
    while True:
        try:
            altura = float(input("Informe a altura do produto em cm: "))
            if altura > 0:
                break
        except ValueError:
            print("Informe um valor valido para a altura\ninforme novamente... ")
    while True:
        try:
            profundidade = float(input("Informe a profundidade do produto em cm: "))
            if profundidade > 0:
                break
        except ValueError:
            print("Informe um valor valido para a profundidade\ninforme novamente... ")

    prod = Produto(nome, categoria, subcategoria, descricao, preco, peso, largura, altura, profundidade)
    return prod


def maior_indice(lista_de_produtos_index) -> int:
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
        'Subcategoria': p.get_subcategoria().capitalize(),
        'Descrição': p.get_descricao().capitalize(),
        'Preço': p.get_preco(),
        'Peso': p.get_peso(),
        'Largura': p.get_largura(),
        'Altura': p.get_altura(),
        'Profundidade': p.get_profundidade()

    }

    lista_aux.append(desc_produto)
    return lista_de_produtos.append(lista_aux)


# todo calcular volume?
def listando_produtos(lista_de_produtos):
    """
    Ordena e imprime lista de produtos.
    :param lista_de_produtos
    """
    lista_ordenada = sorted(lista_de_produtos)
    for produto in range(len(lista_ordenada)):
        id = lista_ordenada[produto][0]
        produto = lista_ordenada[produto][1]
        print(f"id: {id}\nNome: {produto['Nome']}\nCategoria: {produto['Categoria']}"
              f"\nSubcategoria: {produto['Subcategoria']}"
              f"\nDescrição: {produto['Descrição']}"
              f"\nPreço: {produto['Preço']}"
              f"\nPeso:{produto['Peso']}kg"
              f"\nDimensões: {produto['Largura']}cm x {produto['Altura']}cm x {produto['Profundidade']}cm ")
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
    p = cria_produto()
    desc_produto = {
        'Nome': p.get_nome().capitalize(),
        'Categoria': p.get_categoria().capitalize(),
        'Subcategoria': p.get_subcategoria().capitalize(),
        'Descrição': p.get_descricao().capitalize(),
        'Preço': p.get_preco(),
        'Peso': p.get_peso(),
        'Largura': p.get_largura(),
        'Altura': p.get_altura(),
        'Profundidade': p.get_profundidade()

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
            |   5 - Listar categorias           |
            |   6 - Cadastrar categorias        |
            |	7 - Encerrar					|
            +-----------------------------------+""")
            opcao = int(input("             >>> "))
            if opcao not in (1, 2, 3, 4, 5, 6, 7):
                print("Opção inexistente, escolha entre 1 e 7...")
                pass
            else:
                break
        except ValueError:
            print("Ooops! Valor inválido! Digite novamente um número entre 1 e 7...")
    return opcao


def controle():
    op = menu_inicial()
    while op != 7:
        if op == 1:
            salva_produto(cria_produto(categorias), lista_de_produtos)
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
        elif op == 5:
            imprime_categoria(0, categorias)
            op = menu_inicial()
        elif op == 6:
            salva_categoria(cria_categoria(categorias), categorias)
            op = menu_inicial()
    print("Até logo!")


categorias = [[1, 'Eletronicos'], [1, 'Moveis']]
lista_de_produtos = []
controle()
