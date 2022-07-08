from src.dominio.excecoes import ExcecaoDeDominio
from src.dominio.glossarios import Glossario


class ExcecaoNumeroDeOrdemDeLivroInvalido(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        formatos = self.formatar_lista(Glossario.exemplos_de_numero_de_ordem_de_livro)
        mensagem = f'Número de ordem de Livro inválido: {valor}' \
                   f'\n\nFormatos válidos:' \
                   f'\n{formatos}'
        super().__init__(mensagem)
