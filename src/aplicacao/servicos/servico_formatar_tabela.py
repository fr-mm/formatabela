from src.aplicacao.interfaces.interface_servico_ler_tabela import (
    InterfaceServicoLerTabela,
)


class ServicoFormatarTabela:
    __servico_ler_tabela: InterfaceServicoLerTabela

    def __init__(self, servico_ler_tabela: InterfaceServicoLerTabela) -> None:
        self.__servico_ler_tabela = servico_ler_tabela

    def executar(self):
        pass
