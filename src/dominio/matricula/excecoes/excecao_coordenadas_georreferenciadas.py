from src.dominio.matricula.enums import EnumCoordenadasGeorreferenciadas
from src.dominio.matricula.excecoes import ExcecaoDeDominio


class ExcecaoCoordenadasGeorreferenciadas(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_valores_de_enum(EnumCoordenadasGeorreferenciadas)
        mensagem = f'Valor de coordenadas georreferenciadas iválido: {valor}' \
                   f'\n\nOpções válidas:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
