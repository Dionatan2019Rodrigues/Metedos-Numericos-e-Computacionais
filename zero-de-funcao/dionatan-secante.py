# Importamos a biblioteca sympy para permitir a leitura de funções dinâmicas
import sympy as sp

# =====================================================================
# ENTRADA DE DADOS
# =====================================================================

# 1. Definimos 'x' como variável simbólica
x = sp.symbols('x')

# 2. Recebemos a expressão da função do usuário
# Exemplo de entrada: x**3 - 9*x + 3 ou 2**x - 3*x
expr_str = input("Insira a expressão da função f(x) (ex: x**3 - 9*x + 3): ")
expr = sp.parse_expr(expr_str)

# 3. Transformamos a expressão em uma função rápida do Python (lambdify).
# Isso evita o uso lento de '.subs().evalf()' dentro do laço de repetição.
func = sp.lambdify(x, expr, "math")

# 4. Recebemos os dois chutes iniciais (x0 e x1) e a tolerância de parada
x0 = float(input("Insira o primeiro chute inicial (x0 / Ponto A): "))
x1 = float(input("Insira o segundo chute inicial (x1 / Ponto B): "))
tolerancia = float(input("Insira o valor para a tolerância (ex: 0.001): "))

# =====================================================================
# ALGORITMO: MÉTODO DA SECANTE
# =====================================================================
# O Método da Secante é uma variação do Método de Newton-Raphson que evita 
# a necessidade de calcular a derivada analítica f'(x).
# Em vez da derivada, ele aproxima a inclinação por uma reta secante 
# que passa pelos dois últimos pontos conhecidos: (x0, f(x0)) e (x1, f(x1)).

def secante(funcao, x0, x1, tolerancia, max_iter=100):
    
    a = x0
    b = x1
    iteracao = 1

    # CRITÉRIO DE PARADA:
    # O laço roda enquanto a variação entre os dois últimos pontos
    # for estritamente maior que a tolerância exigida.
    while abs(b - a) > tolerancia:
        
        fa = funcao(a)
        fb = funcao(b)

        # VERIFICAÇÃO DE SEGURANÇA (Divisão por zero):
        # Se f(b) == f(a), o denominador da fórmula fica nulo.
        # Geometricamente, isso significa que a reta secante ficou horizontal 
        # e é paralela ao eixo x, não sendo possível projetar a próxima aproximação.
        if abs(fb - fa) < 1e-12:
            print("\nErro: f(a) é igual (ou muito próximo) a f(b).")
            print("A reta secante ficou horizontal, gerando uma divisão por zero. O método não pode continuar.")
            return None

        # FÓRMULA DO MÉTODO DA SECANTE:
        # c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        c = (a * fb - b * fa) / (fb - fa)

        # Exibição do passo a passo (como mostrado em aula)
        print(f"Iteração {iteracao:02d} | Aproximação x = {c:.6f}")
        iteracao += 1

        # Critério de parada antecipada se encontrarmos a raiz exata
        if funcao(c) == 0:
            return c

        # ATUALIZAÇÃO DOS PONTOS PARA A PRÓXIMA ITERAÇÃO:
        # O ponto antigo 'a' avança para 'b', e o ponto 'b' passa a ser a nova aproximação 'c'.
        a = b
        b = c

        # Trava de segurança contra laço infinito caso o método divirja
        if iteracao > max_iter:
            print("\nAviso: O método atingiu o número máximo de iterações sem convergir.")
            break

    return b

# =====================================================================
# EXECUÇÃO E SAÍDA
# =====================================================================

raiz = secante(func, x0, x1, tolerancia)

if raiz is not None:
    print(f"\nValor aproximado da raiz final: {raiz}")