from src.dominio.matricula.excecoes import ExcecaoDeDominio
from src.dominio.matricula.glossarios import Glossario


class ExcecaoLivroDeTituloAquisitivo(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        exemplos = self.formatar_lista(Glossario.exemplos_de_livro_de_registro_anterior)
        mensagem = f'Livro de Registro Anterior Inválido: {valor}' \
                   f'\n\nFormatos válidos:' \
                   f'\n{exemplos}'
        super().__init__(mensagem)
