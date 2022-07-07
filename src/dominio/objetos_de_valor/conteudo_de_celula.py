from dataclasses import dataclass


@dataclass(frozen=True)
class ConteudoDeCelula:
    valor: str

    @property
    def existe(self) -> bool:
        return self.valor != ''
