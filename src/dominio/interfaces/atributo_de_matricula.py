from __future__ import annotations

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

    def eh_igual_a(self, atributo_de_matricula: AtributoDeMatricula) -> bool:
        return self.valor == atributo_de_matricula.valor

