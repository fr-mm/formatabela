from abc import ABC, abstractmethod

from src.dominio.otds.otd_tabela import OTDTabela


class InterfaceServicoLerTabela(ABC):
    @abstractmethod
    def executar(self, arquivo: str) -> OTDTabela:
        pass
