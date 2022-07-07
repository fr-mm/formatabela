from src.dominio.enums import EnumTipoDeImovel
from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoTipoDeImovelDeMatriculaInvalido(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_valores_de_enum(EnumTipoDeImovel)
        mensagem = f'Tipo de imóvel inválido: {valor}' \
                   f'\ndeve ser uma das opções:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
