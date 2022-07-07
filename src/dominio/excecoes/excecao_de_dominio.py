class ExcecaoDeDominio(Exception):
    def __init__(self, mensagem: str) -> None:
        super().__init__(f'\n\n{mensagem}')
