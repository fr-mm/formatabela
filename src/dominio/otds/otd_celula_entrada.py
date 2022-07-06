from dataclasses import dataclass


@dataclass(frozen=True)
class OTDCelulaEntrada:
    conteudo: str
    comentario: str
    cor_fundo: str
    cor_texto: str
