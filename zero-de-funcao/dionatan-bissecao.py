# Importamos a biblioteca sympy para lidar com a matemática simbólica.
import sympy as sp #caso não tenha essa biblioteca execute: pip install sympy

# =====================================================================
# ENTRADA DE DADOS
# =====================================================================

# 1. Definimos 'x' como uma variável simbólica para que o Python entenda 
# que se trata de uma incógnita matemática.
x = sp.symbols('x')

# 2. Recebemos a função do usuário como texto (string).
# Exemplo de entrada: x - 2**(-x) ou x**2 - 4
expr_str = input("Insira a expressão da função f(x) (ex: x - 2**(-x)): ")

# 3. Convertemos o texto para uma expressão matemática compreensível pelo sympy.
expr = sp.parse_expr(expr_str)

# 4. Transformamos a expressão simbólica em uma função executável e rápida.
# Isso substitui a sua antiga 'def func(x):', permitindo avaliar f(valor) diretamente.
func = sp.lambdify(x, expr, "math")

# 5. Recebemos os parâmetros do intervalo [a, b] e a tolerância (critério de parada).
a = float(input("Insira o limite inferior (a): "))
b = float(input("Insira o limite superior (b): "))
tolerancia = float(input("Insira o valor para a tolerância (ex: 0.001): "))

# =====================================================================
# ALGORITMO: MÉTODO DA BISSEÇÃO
# =====================================================================
# O Método da Bisseção é um método de busca de raízes que reduz o 
# intervalo pela metade a cada iteração. Ele é baseado no Teorema de Bolzano 
def bissecao(funcao, a, b, tolerancia):
    
    # VERIFICAÇÃO INICIAL (Teorema de Bolzano):
    # Se f(a) e f(b) tiverem o mesmo sinal, o produto será positivo.
    # O Teorema de Bolzano exige que haja uma troca de sinal no intervalo [a, b] 
    # para garantir a existência de pelo menos uma raiz real.
    if funcao(a) * funcao(b) >= 0:
        print("Erro: A função não muda de sinal no intervalo [a, b].")
        print("O Teorema de Bolzano não garante uma raiz neste intervalo. Tente outros valores.")
        return None

    # CRITÉRIO DE PARADA:
    # O laço continuará rodando enquanto o tamanho do intervalo (b - a) 
    # for estritamente maior que a tolerância exigida.
    while (b - a) > tolerancia:
        
        # Encontra o ponto médio do intervalo atual.
        meio = (a + b) / 2

        # Verifica se, por sorte, o ponto médio é a raiz exata.
        if funcao(meio) == 0:
            return meio

        # ATUALIZAÇÃO DO INTERVALO:
        # Se f(a) e f(meio) têm o mesmo sinal (produto positivo), significa que a raiz
        # não está entre 'a' e 'meio'. Logo, ela deve estar entre 'meio' e 'b'.
        # Portanto, atualizamos o limite inferior 'a' para ser o nosso 'meio'.
        if funcao(a) * funcao(meio) > 0:
            a = meio
            
        # Caso contrário, f(a) e f(meio) têm sinais opostos. A raiz está na primeira
        # metade do intervalo. Atualizamos o limite superior 'b' para ser o 'meio'.
        else:
            b = meio
            
    # Quando o intervalo for menor que a tolerância, o laço termina.
    # Retornamos o ponto médio do intervalo final como a melhor aproximação da raiz.
    return (a + b) / 2

# =====================================================================
# EXECUÇÃO E SAÍDA
# =====================================================================

# Chamamos a função passando nossa função matemática dinâmica e os parâmetros.
raiz = bissecao(func, a, b, tolerancia)

# Se a raiz foi encontrada (ou seja, se não parou na verificação de Bolzano), exibimos.
if raiz is not None:
    print(f"\nA raiz aproximada da função é: {raiz}")