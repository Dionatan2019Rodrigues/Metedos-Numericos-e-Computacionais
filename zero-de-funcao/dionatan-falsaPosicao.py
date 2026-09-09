# Importamos a biblioteca sympy para permitir a leitura de funções dinâmicas
import sympy as sp

# =====================================================================
# ENTRADA DE DADOS
# =====================================================================

# 1. Definimos 'x' como variável simbólica
x = sp.symbols('x')

# 2. Recebemos a expressão da função do usuário
# Exemplo de entrada: 2**x - 3*x
expr_str = input("Insira a expressão da função f(x) (ex: 2**x - 3*x): ")
expr = sp.parse_expr(expr_str)

# 3. Transformamos a expressão em uma função rápida do Python
func = sp.lambdify(x, expr, "math")

# 4. Recebemos os parâmetros (corrigido o segundo input que pedia 'a' novamente)
a = float(input("Insira o limite inferior (a): "))
b = float(input("Insira o limite superior (b): "))
tolerancia = float(input("Insira o valor para a tolerância (ex: 0.001): "))

# =====================================================================
# ALGORITMO: MÉTODO DA FALSA POSIÇÃO
# =====================================================================
# O Método da Falsa Posição (ou Regula Falsi) não divide o intervalo ao meio.
# Ele traça uma reta entre os pontos (a, f(a)) e (b, f(b)) e usa a raiz 
# dessa reta como a nova aproximação. É uma média ponderada.

def falsa_posicao(funcao, a, b, tolerancia):
    
    # VERIFICAÇÃO INICIAL (Teorema de Bolzano):
    if funcao(a) * funcao(b) >= 0:
        print("Erro: A função não muda de sinal no intervalo [a, b].")
        print("O Teorema de Bolzano não garante uma raiz neste intervalo. Tente outros valores.")
        return None

    # Variável para contar as iterações e mostrar de forma didática na tela
    iteracao = 1

    # CRITÉRIO DE PARADA:
    # Mantive a lógica do seu código original: laço roda enquanto o tamanho do intervalo for maior que a tolerância.
    while abs(b - a) > tolerancia:
        
        # CÁLCULO DO PONTO (Média Ponderada):
        # Fórmula clássica da Falsa Posição
        ponto = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
        
        # Exibição do passo a passo (como mostrado em aula)
        print(f"Iteração {iteracao:02d} | Aproximação x = {ponto:.6f}")
        iteracao += 1

        # Verifica se por sorte já caímos na raiz exata
        if funcao(ponto) == 0:
            return ponto

        # ATUALIZAÇÃO DO INTERVALO:
        # Verifica em qual subintervalo ocorreu a troca de sinal.
        if funcao(a) * funcao(ponto) > 0:
            # Sinais de f(a) e f(ponto) são iguais. A raiz está entre 'ponto' e 'b'.
            a = ponto
        else: 
            # Sinais são opostos. A raiz está entre 'a' e 'ponto'.
            b = ponto
            
    # Ao sair do while, calculamos e retornamos a última e mais precisa estimativa do ponto.
    ponto_final = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
    return ponto_final

# =====================================================================
# EXECUÇÃO E SAÍDA
# =====================================================================

raiz = falsa_posicao(func, a, b, tolerancia)

if raiz is not None:
    print(f"\nValor aproximado da raiz final: {raiz}")