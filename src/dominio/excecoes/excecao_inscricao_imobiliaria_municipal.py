from src.dominio.enums import EnumFormatoInscricaoImobiliariaMunicipalDeMatricula
from src.dominio.excecoes import ExcecaoDeDominio


class ExcecaoInscricaoImobiliariaMunicipal(ExcecaoDeDominio):
    def __init__(self, valor: str) -> None:
        opcoes = self.formatar_valores_de_enum(EnumFormatoInscricaoImobiliariaMunicipalDeMatricula)
        mensagem = f'Inscrição imobiliária inválida: {valor}' \
                   f'\n\nFormatos válidos:' \
                   f'\n{opcoes}'
        super().__init__(mensagem)
