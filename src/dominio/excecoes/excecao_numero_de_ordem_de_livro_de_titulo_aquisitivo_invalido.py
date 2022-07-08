from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoNumeroDeOrdemDeLivroDeRegistroAnteriorInvalido(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_lista(EnumFormatoTituloAquisitivo)

