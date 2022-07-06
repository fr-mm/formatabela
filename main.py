from src.infraestrutura.servicos.servico_ler_tabela import ServicoLerTabela

# IGNORAR TUDO NESSE ARQUIVO POR ENQUANTO
ler_tabela = ServicoLerTabela()
tabela = ler_tabela.executar("./testes/exemplos/tabela_teste.xlsx")
[print([celula.cor_fundo for celula in item]) for item in tabela.conteudo]
