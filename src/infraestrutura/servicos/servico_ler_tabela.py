from openpyxl import load_workbook


class ServicoLerTabela:
    def executar(self, endereco_tabela_xlsx: str):
        tabela = load_workbook(endereco_tabela_xlsx)
        print(tabela)
