from src.dominio.matricula.excecoes import ExcecaoDeDominio


class ExcecaoDataDeMatricula(ExcecaoDeDominio):
    def __init__(self, data: str) -> None:
        mensagem = f'Data inválida: {data}' \
                   f'\nDeve ser data existente, antes de agora, no formato DD/MM/AAAA'
        super().__init__(mensagem)
