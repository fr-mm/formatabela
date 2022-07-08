from src.dominio.matricula.excecoes import ExcecaoDeDominio
from src.dominio.matricula.glossarios import Glossario


class ExcecaoFolhaDeLivro(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_lista(Glossario.exemplos_de_folha_de_livro)
        mensagem = f'Folha de livro inválida: {valor}' \
                   f'\n\nFormatos válidos:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
