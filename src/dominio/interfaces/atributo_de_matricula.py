from abc import ABC, abstractmethod


class AtributoDeMatricula(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @property
    @abstractmethod
    def texto(self) -> str:
        pass
