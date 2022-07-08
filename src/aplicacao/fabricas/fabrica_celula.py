from src.dominio.tabela.entidades import Celula
from src.dominio.tabela.otds import OTDCelula


class FabricaCelula:
    @staticmethod
    def criar_de_otd(otd: OTDCelula) -> Celula:
        return Celula(
            conteudo=otd.conteudo,
            comentario=otd.comentario,
            cor_fundo=otd.cor_fundo,
            cor_texto=otd.cor_texto
        )
