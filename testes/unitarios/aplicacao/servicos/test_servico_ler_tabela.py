from pathlib import Path
from unittest import TestCase

from src.infraestrutura.enums import EnumServicoLerTabela
from testes import exemplos

from src.infraestrutura.servicos import ServicoLerTabela


class TestServicoLerTabela(TestCase):
    def setUp(self) -> None:
        self.arquivo = f'{Path(exemplos.__file__).parent}/tabela_teste.xlsx'
        self.servico_ler_tabela = ServicoLerTabela()

    def test_executar_QUANDO_arquivo_existe_ENTAO_retorna_otd_com_nome_esperado(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        nome_esperado = 'tabela_teste'
        self.assertEqual(otd.nome, nome_esperado)

    def test_executar_QUANDO_tabebla_possui_mais_de_uma_pagina_ENTAO_retorna_otd_com_nome_da_pagina_esperado(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        nome_da_pagina_esperado = 'pagina1'
        self.assertEqual(otd.nome_da_pagina, nome_da_pagina_esperado)

    def test_executar_QUANDO_tabela_eh_3x3_ENTAO_retorna_otd_com_conteudo_3x3(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        tamanho_das_linhas = [len(linha) for linha in otd.conteudo]
        tamanho_das_linhas_esperado = [3, 3, 3]
        self.assertEqual(tamanho_das_linhas, tamanho_das_linhas_esperado)

    def test_executar_QUANDO_celula_nao_tem_conteudo_ENTAO_retorna_dto_onde_celula_contem_conteudo_esperado(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        celula_vazia = otd.conteudo[1][1]
        conteudo_da_celula_esperado = EnumServicoLerTabela.VALOR_PADRAO.value
        self.assertEqual(celula_vazia.conteudo, conteudo_da_celula_esperado)

    def test_executar_QUANDO_tabela_preenchida_ENTAO_retorna_otd_com_celulas_com_conteudo_na_ordem_esperada(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        conteudos_na_ordem_esperada = [
            ['a1', 'b1', 'c1'],
            ['a2', '', 'c2'],
            ['a3', 'b3', 'c3']
        ]
        conteudos = [[celula.conteudo for celula in linha] for linha in otd.conteudo]
        self.assertEqual(conteudos, conteudos_na_ordem_esperada)

    def test_executar_QUANDO_celula_contem_comentario_ENTAO_retorna_otd_com_celula_contendo_comentario_esperado(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        celula = otd.conteudo[0][0]
        conteudo_esperado = 'foo'
        self.assertEqual(celula.comentario, conteudo_esperado)

    def test_executar_QUANDO_celula_nao_contem_tetxto_ENTAO_retorna_otd_com_celula_com_cor_do_texto_esperada(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        celula = otd.conteudo[1][1]
        cor_do_texto_esperada = EnumServicoLerTabela.VALOR_PADRAO.value
        self.assertEqual(celula.cor_texto, cor_do_texto_esperada)

    def test_executar_QUANDO_celula_contem_texto_colorido_ENTAO_retorna_otd_com_celula_contendo_cor_texto_diferente_do_padrao(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        celula = otd.conteudo[0][0]
        self.assertNotEqual(celula.cor_texto, EnumServicoLerTabela.VALOR_PADRAO.value)

    def test_executar_QUANDO_celula_nao_contem_texto_colorido_ENTAO_retorna_otd_com_celula_contendo_cor_texto_padrao(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        celula = otd.conteudo[1][0]
        self.assertEqual(celula.cor_texto, EnumServicoLerTabela.VALOR_PADRAO.value)

    def test_executar_QUANDO_celula_contem_fundo_colorido_ENTAO_retorna_otd_com_celula_contendo_cor_fundo_diferente_do_padrao(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        celula = otd.conteudo[0][0]
        self.assertNotEqual(celula.cor_fundo, EnumServicoLerTabela.COR_FUNDO_PADRARO.value)

    def test_executar_QUANDO_celula_nao_contem_fundo_colorido_ENTAO_retorna_otd_com_celula_contendo_cor_fundo_padrao(self) -> None:
        otd = self.servico_ler_tabela.executar(self.arquivo)

        celula = otd.conteudo[1][0]
        self.assertEqual(celula.cor_fundo, EnumServicoLerTabela.VALOR_PADRAO.value)

