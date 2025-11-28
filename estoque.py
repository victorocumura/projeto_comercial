
import json
import uuid

def carregar_estoque(arquivo_json):
    with open(arquivo_json, "r", encoding="utf-8") as f:
        return json.load(f)["estoque"]

def salvar_estoque(arquivo_json, estoque):
    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump({"estoque": estoque}, f, indent=4)

def movimentar_estoque(estoque, codigo_produto, quantidade, descricao):
    """
    Realiza uma movimentação de entrada ou saída no estoque.
    Retorna a quantidade final do produto.
    """
    id_movimentacao = str(uuid.uuid4())
    
    for produto in estoque:
        if produto["codigoProduto"] == codigo_produto:
            produto["estoque"] += quantidade
            print(f"Movimentação ID: {id_movimentacao}")
            print(f"Produto: {produto['descricaoProduto']}")
            print(f"Descrição: {descricao}")
            print(f"Quantidade movimentada: {quantidade}")
            print(f"Estoque final: {produto['estoque']}")
            return produto["estoque"]
    
    print("Produto não encontrado!")
    return None


