largura: float = float(input("Qual a largura do cômodo? "))
profundidade: float = float(input("Qual a profundidade do cômodo? "))
altura: float = 2.9

area_paredes: float = 2 * (largura + profundidade) * altura
area_teto: float = largura * profundidade

print("A area das paredes é: ",
        area_paredes
      )
print("A litragem de tinta necessária é: ",
        (area_paredes + area_teto) / 10  # 10 é o rendimento da tinta. 10m² / lt
      )

