from abc import ABC, abstractmethod

from src.dominio.otds.otd_tabela_entrada import OTDTabelaEntrada


class InterfaceServicoLerTabela(ABC):
    @abstractmethod
    def executar(self, arquivo: str) -> OTDTabelaEntrada:
        pass
