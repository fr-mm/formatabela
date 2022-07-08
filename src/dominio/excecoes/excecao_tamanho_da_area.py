from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoTamanhoDaArea(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        mensagem = f'Tamanho da área inválido: {valor}' \
                   f'\nDeve ser um número positivo com casas decimais separados por vírgula ou ponto'
        super().__init__(mensagem)
