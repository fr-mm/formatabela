from dataclasses import dataclass
from typing import List

from src.dominio.otds.otd_celula_entrada import OTDCelulaEntrada


@dataclass(frozen=True)
class OTDTabelaEntrada:
    nome: str
    nome_da_pagina: str
    conteudo: List[List[OTDCelulaEntrada]]
