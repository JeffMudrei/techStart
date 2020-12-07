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


