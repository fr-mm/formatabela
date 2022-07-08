from src.dominio.matricula.enums import EnumTipoDeImovel
from src.dominio.matricula.excecoes import ExcecaoDeDominio


class ExcecaoTipoDeImovelDeMatricula(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_valores_de_enum(EnumTipoDeImovel)
        mensagem = f'Tipo de imóvel inválido: {valor}' \
                   f'\ndeve ser uma das opções:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
