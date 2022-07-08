from dataclasses import dataclass
from typing import List

from src.dominio.tabela.otds.otd_celula import OTDCelula


@dataclass(frozen=True)
class OTDTabela:
    nome: str
    nome_da_pagina: str
    conteudo: List[List[OTDCelula]]
