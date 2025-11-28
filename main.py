from vendas import comissao_vendedores
from estoque import carregar_estoque, movimentar_estoque, salvar_estoque
from juros import calcular_juros

comissao_vendedores("dados/vendas.json")

estoque_lista = carregar_estoque("dados/estoque.json")
movimentar_estoque(estoque_lista, 102, -10, "Saída de cadernos")
salvar_estoque("dados/estoque.json", estoque_lista)

calcular_juros(1500, "2025-11-20")
