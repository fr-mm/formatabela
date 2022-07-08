from src.dominio.enums import EnumCNSDeRegistroAnterior
from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoCNSDeRegistroAnterior(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_valores_de_enum(EnumCNSDeRegistroAnterior)
        mensagem = f'CNS de Registro Anterior inválido: {valor}' \
                   f'\n\nOpções disponíveis:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
