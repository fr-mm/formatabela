from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoDataDeMatriculaInvalida(ExcecaoDeDominio):
    def __init__(self, data: str) -> None:
        mensagem = f'Data inválida: {data}' \
                   f'\nDeve ser data existente, antes de agora, no formato DD/MM/AAAA'
        super().__init__(mensagem)
