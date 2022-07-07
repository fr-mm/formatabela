from dataclasses import dataclass

from src.dominio.interfaces import AgregadoDeMatricula
from src.dominio.objetos_de_valor import TamanhoDaArea, MedidaDaArea


@dataclass(frozen=True)
class AreaDeMatricula(AgregadoDeMatricula):
    tamanho: TamanhoDaArea
    medida: MedidaDaArea
