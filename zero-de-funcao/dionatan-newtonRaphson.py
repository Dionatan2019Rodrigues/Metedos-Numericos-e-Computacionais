# Importamos a biblioteca sympy para cálculo simbólico e derivação automática
import sympy as sp

# =====================================================================
# ENTRADA DE DADOS
# =====================================================================

# 1. Definimos 'x' como variável simbólica
x = sp.symbols('x')

# 2. Recebemos a expressão da função do usuário
# Exemplo de entrada: x**3 - 9*x + 3 ou x - 2**(-x)
expr_str = input("Insira a expressão da função f(x) (ex: x**3 - 9*x + 3): ")
expr = sp.parse_expr(expr_str)

# 3. Calculamos a derivada f'(x) de forma automática usando o SymPy
derivada_expr = sp.diff(expr, x)
print(f"-> Derivada f'(x) calculada automaticamente: {derivada_expr}")

# 4. Transformamos a função e a sua derivada em funções nativas do Python (lambdify).
func = sp.lambdify(x, expr, "math")
dfunc = sp.lambdify(x, derivada_expr, "math")

# 5. Recebemos o chute inicial (x0) e a tolerância de parada
chute = float(input("Insira o chute inicial (x0): "))
tolerancia = float(input("Insira o valor para a tolerância (ex: 0.001): "))

# =====================================================================
# ALGORITMO: MÉTODO DE NEWTON-RAPHSON
# =====================================================================
# O Método de Newton-Raphson é um método aberto que utiliza a reta tangente 
# à curva no ponto atual para projetar a próxima aproximação da raiz. 
# Possui convergência quadrática (muito rápida), mas exige o cálculo da derivada f'(x).

def newton_raphson(funcao, derivada, chute_inicial, tolerancia, max_iter=100):
    
    x_atual = chute_inicial
    
    # Inicializamos x_anterior com um valor diferente para garantir a entrada no while
    x_anterior = x_atual + 2 * tolerancia
    
    iteracao = 1

    # CRITÉRIO DE PARADA:
    # O laço roda enquanto a variação entre a aproximação atual e a anterior 
    # for estritamente maior que a tolerância exigida.
    while abs(x_atual - x_anterior) > tolerancia:
        
        # Guardamos o valor atual para ser o valor anterior no ciclo
        x_anterior = x_atual
        
        # Avaliamos a derivada no ponto anterior
        f_linha = derivada(x_anterior)
        
        # VERIFICAÇÃO DE SEGURANÇA:
        # Se a derivada for igual a zero (ou quase zero), a reta tangente fica horizontal 
        # e o método falha por divisão por zero ou projeta o próximo x para o infinito.
        if abs(f_linha) < 1e-12:
            print("\nErro: A derivada f'(x) é zero ou muito próxima de zero neste ponto.")
            print("A reta tangente ficou horizontal e o método não pode continuar. Tente outro chute inicial.")
            return None
        
        # FÓRMULA DE NEWTON-RAPHSON:
        # x_{k+1} = x_k - ( f(x_k) / f'(x_k) )
        x_atual = x_anterior - (funcao(x_anterior) / f_linha)
        
        # Exibição do passo a passo (como mostrado em aula)
        print(f"Iteração {iteracao:02d} | Aproximação x = {x_atual:.6f}")
        iteracao += 1

        # Critério de parada antecipada se encontrarmos a raiz exata
        if funcao(x_atual) == 0:
            break

        # Trava de segurança contra laço infinito caso o método divirja
        if iteracao > max_iter:
            print("\nAviso: O método atingiu o número máximo de iterações sem convergir.")
            break

    return x_atual

# =====================================================================
# EXECUÇÃO E SAÍDA
# =====================================================================

raiz = newton_raphson(func, dfunc, chute, tolerancia)

if raiz is not None:
    print(f"\nValor aproximado da raiz final: {raiz}")