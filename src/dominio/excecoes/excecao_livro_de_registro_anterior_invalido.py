from src.dominio.excecoes import ExcecaoDeDominio
from src.dominio.glossarios import Glossario


class ExcecaoLivroDeRegistroAnteriorInvalido(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        exemplos = self.formatar_lista(Glossario.exemplos_de_livro_de_registro_anterior)
        mensagem = f'Livro de Registro Anterior Inválido: {valor}' \
                   f'\n\nFormatos válidos:' \
                   f'\n{exemplos}'
        super().__init__(mensagem)
