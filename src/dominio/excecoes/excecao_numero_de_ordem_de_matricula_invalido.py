from src.dominio.excecoes.excecao_de_dominio import ExcecaoDeDominio


class ExcecaoNumeroDeOrdemDeMatriculaInvalido(ExcecaoDeDominio):
    def __init__(self, numero_de_ordem: str) -> None:
        mensagem = f'Número de ordem inválido: {numero_de_ordem}' \
                   f'\nDeve ser numérico, inteiro e maior que 0'
        super().__init__(mensagem)
