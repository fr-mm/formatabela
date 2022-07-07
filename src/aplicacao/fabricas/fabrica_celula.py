from src.dominio.entidades import Celula
from src.dominio.otds import OTDCelula


class FabricaCelula:
    @staticmethod
    def criar_de_otd(otd: OTDCelula) -> Celula:
        return Celula(
            conteudo=otd.conteudo,
            comentario=otd.comentario,
            cor_fundo=otd.cor_fundo,
            cor_texto=otd.cor_texto
        )
