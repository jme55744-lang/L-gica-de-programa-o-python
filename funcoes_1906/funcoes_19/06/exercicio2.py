def desenhar_retangulo(altura, largura):
    largura = 18
    altura = 5
    print("+"+"-"*(largura-2)+"+")
    for i in range(altura-2):
        print("|"+" "*(largura-2)+"|")
    if altura>1:
        print("+"+"-"*(largura-2)+"+")
    
retangulo = desenhar_retangulo(10, 10)
print(retangulo) 