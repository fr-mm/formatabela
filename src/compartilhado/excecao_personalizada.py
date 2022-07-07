from typing import Iterable, List


class ExcecaoPersonalizada(Exception):
    def __init__(self, mensagem: str) -> None:
        super().__init__(f'\n\n{mensagem}')

    @staticmethod
    def formatar_valores_de_enum(enum: Iterable) -> str:
        valores = [opcao.value for opcao in enum]
        return ExcecaoPersonalizada.formatar_lista(valores)

    @staticmethod
    def formatar_lista(lista: List[str]) -> str:
        return ''.join([f'- {item}\n' for item in lista])

