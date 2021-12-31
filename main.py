from calculadora import Calculadora

calc = Calculadora()

largura: float = float(input("Qual a largura do cômodo? "))
profundidade: float = float(input("Qual a profundidade do cômodo? "))
altura: float = 2.9

# calc.area_paredes: float = 2 * (largura + profundidade) * altura

# calc.area_teto: float = largura * profundidade

print("A area das paredes é: ",
        calc.calcular_area_parede(largura, profundidade, altura)
      )

print("A area do této é: ",
        calc.calcular_area_teto(largura, profundidade)
      )

print("A litragem de tinta necessária é: ",
        calc.calcular_litragem_necessaria()
      )

