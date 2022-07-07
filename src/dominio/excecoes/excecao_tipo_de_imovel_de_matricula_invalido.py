from src.dominio.enums import EnumTipoDeImovel
from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoTipoDeImovelDeMatriculaInvalido(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = ''.join([f'- {tipo_de_imovel.value}\n' for tipo_de_imovel in EnumTipoDeImovel])
        mensagem = f'Tipo de imóvel inválido: {valor}' \
                   f'\ndeve ser uma das opções:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
