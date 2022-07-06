from dataclasses import dataclass


@dataclass(frozen=True)
class Celula:
    conteudo: str
    comentario: str
    cor: str
    largura: int
