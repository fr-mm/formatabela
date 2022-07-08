from dataclasses import dataclass


@dataclass(frozen=True)
class Celula:
    conteudo: str
    comentario: str
    cor_texto: str
    cor_fundo: str
