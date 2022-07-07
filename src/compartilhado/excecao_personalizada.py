from typing import Iterable


class ExcecaoPersonalizada(Exception):
    def __init__(self, mensagem: str) -> None:
        super().__init__(f'\n\n{mensagem}')

    @staticmethod
    def formatar_valores_de_enum(enum: Iterable) -> str:
        return ''.join([f'- {tipo_de_imovel.value}\n' for tipo_de_imovel in enum])
