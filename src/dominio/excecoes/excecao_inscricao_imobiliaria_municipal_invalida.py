from typing import List

from src.dominio.enums import EnumFormatoDeInscricaoImobiliariaMunicipal
from src.dominio.excecoes import ExcecaoDeDominio
from src.dominio.glossarios import Glossario


class ExcecaoInscricaoImobiliariaMunicipalInvalida(ExcecaoDeDominio):
    def __init__(self, valor: str, opcoes_compartilhadas: List[str]) -> None:
        opcoes = [Glossario.inscricao_imobiliaria_municipal[opcao] for opcao in EnumFormatoDeInscricaoImobiliariaMunicipal]
        opcoes = self.formatar_lista(opcoes + opcoes_compartilhadas)
        mensagem = f'Inscrição imobiliária inválida: {valor}' \
                   f'\n\nFormatos válidos:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
