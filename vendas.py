import json

def calcular_comissao(valor):
    """Calcula comissão baseado nas regras fornecidas."""
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05

def comissao_vendedores(arquivo_json):
    """Calcula a comissão total de cada vendedor a partir de um JSON de vendas."""
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    comissoes = {}
    for venda in dados["vendas"]:
        vendedor = venda["vendedor"]
        valor = venda["valor"]
        comissao = calcular_comissao(valor)
        comissoes[vendedor] = comissoes.get(vendedor, 0) + comissao
    
    print("=== Comissão Total por Vendedor ===")
    for vendedor, total in comissoes.items():
        print(f"{vendedor}: R$ {total:.2f}")
    return comissoes


