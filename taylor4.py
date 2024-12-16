import decimal

# Define a precisão dos calculos com decmal para 1000 casas decimais
decimal.getcontext().prec = 1000  

def calcular_ex_taylor(x, epsilon):
    """
    Inicializa o termo (x^0 / 0!), ou seja, 1.
    :param x: Valor de x
    :param epsilon: Limiar de precisão para interrupção do cálculo
    :return: Aproximação de e^x e número de termos usados
    """
    # Convertendo x para número de precisão arbitrária
    x = decimal.Decimal(x)  
    resultado = decimal.Decimal(1)
    termo = decimal.Decimal(1)      
    k = 1
    num_termos = 1

    # Verifica se o termo atual ainda é significativo
    while abs(termo) > epsilon:  
        termo *= x / k
        resultado += termo
        k += 1
        num_termos += 1
    
    return resultado, num_termos

def calcular_ex_taylor_com_decomposicao(x, epsilon):
    """
    Calcula e^x para valores grandes de x usando decomposição.
    :param x: Valor de x
    :param epsilon: Limiar de precisão para interrupção do cálculo
    :return: Aproximação de e^x e número de termos usados
    """
    LIMITE = 709  # Limite para evitar overflow em math.exp
    
    # Separa numerador do denomiinador
    if abs(x) > LIMITE:
        inteiro = int(x)
        fracao = x - inteiro
        
        # Decomposição exponencial: e^x = e^(parte inteira) * e^(parte fracionária)
        resultado_inteiro, num_termos_inteiro = calcular_ex_taylor(inteiro, epsilon)
        resultado_fracao, num_termos_fracao = calcular_ex_taylor(fracao, epsilon)
        
        return resultado_inteiro * resultado_fracao, num_termos_inteiro + num_termos_fracao
    else:
        # Para valores dentro do limite, calculamos diretamente
        return calcular_ex_taylor(x, epsilon)


if __name__ == "__main__":
    print("Cálculo de e^x para números de qualquer magnitude sem overflow")
    # Entrada é um número
    x = float(input("Digite o valor de x: "))
    
    """
    Entrada deve ser 1e-x (exemplo: 1e−6 significa 1×10^−6, ou seja, 0.000001)
    está dizendo que a diferença entre o valor calculado da função e^x e o valor exato deve ser menor do que 0.000001 para que a soma da série de Taylor seja interrompida.
    """
    epsilon = float(input("Digite o valor do limiar de precisão (epsilon): "))

    resultado, num_termos = calcular_ex_taylor_com_decomposicao(x, epsilon)
    print(f"O valor aproximado de e^{x} é: {resultado}")
    print(f"Foi necessário usar {num_termos} termos para alcançar a precisão desejada.")
    print(f"O valor aproximado de e^{x} é: {resultado:.3e}")
