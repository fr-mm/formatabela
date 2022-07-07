from src.dominio.enums import EnumMedidaDaArea
from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoMedidaDaAreaInvalida(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = '\n'.join([f'- {medida_da_area.value}' for medida_da_area in EnumMedidaDaArea])
        mensagem = f'Medida da área inválida: {valor}' \
                   f'\nDeve ser uma das opções:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
