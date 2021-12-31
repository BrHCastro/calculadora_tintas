from calculadora import Calculadora

calc = Calculadora()

largura: float = float(input("Qual a largura do cômodo? "))
profundidade: float = float(input("Qual a profundidade do cômodo? "))
altura: float = 2.9

calc.area_paredes: float = 2 * (largura + profundidade) * altura
calc.area_teto: float = largura * profundidade

print("A area das paredes é: ",
        calc.area_paredes
      )
print("A litragem de tinta necessária é: ",
        (calc.area_paredes + calc.area_teto) / 10  # 10 é o rendimento da tinta. 10m² / lt
      )

