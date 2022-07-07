import re
from typing import List

from src.dominio.enums import EnumOpcoesCompartilhadas, EnumFormatoDeInscricaoImobiliariaMunicipal
from src.dominio.excecoes.excecao_inscricao_imobiliaria_municipal_invalida import \
    ExcecaoInscricaoImobiliariaMunicipalInvalida
from src.dominio.interfaces import AtributoDeMatricula


class InscricaoImobiliariaMunicipalDeMatricula(AtributoDeMatricula):
    __OPCOES_COMPARTILHADAS = [
        EnumOpcoesCompartilhadas.AUSENTE.value,
        EnumOpcoesCompartilhadas.NAO_SE_APLICA.value
    ]
    __valor: str

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> str:
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor

    @staticmethod
    def OPCOES_COMPARTILHADAS() -> List[str]:
        return InscricaoImobiliariaMunicipalDeMatricula.__OPCOES_COMPARTILHADAS

    def __validar(self, valor: str) -> str:
        valor = valor.strip()
        if valor in self.__OPCOES_COMPARTILHADAS:
            return valor
        return self.__validar_formato(valor)

    def __validar_formato(self, valor: str) -> str:
        formatos = [formato.value for formato in EnumFormatoDeInscricaoImobiliariaMunicipal]
        for formato in formatos:
            if re.match(formato, valor):
                return valor
        raise ExcecaoInscricaoImobiliariaMunicipalInvalida(valor, self.__OPCOES_COMPARTILHADAS)

