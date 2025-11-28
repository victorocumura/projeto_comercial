from datetime import datetime

def calcular_juros(valor, data_vencimento, taxa_dia=0.025):
    """
    Calcula o valor dos juros de mora até hoje.
    """
    hoje = datetime.now().date()
    vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d").date()
    
    dias_atraso = (hoje - vencimento).days
    if dias_atraso <= 0:
        print("Não há juros, pagamento ainda não venceu.")
        return 0
    
    juros = valor * taxa_dia * dias_atraso
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Dias de atraso: {dias_atraso}")
    print(f"Taxa por dia: {taxa_dia*100:.2f}%")
    print(f"Juros total: R$ {juros:.2f}")
    return juros

