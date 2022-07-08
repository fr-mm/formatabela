from src.dominio.enums import EnumMedidaDaArea
from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoMedidaDaArea(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_valores_de_enum(EnumMedidaDaArea)
        mensagem = f'Medida da área inválida: {valor}' \
                   f'\nDeve ser uma das opções:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
