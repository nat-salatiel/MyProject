a = 0
b = 1
resultado = 0


while resultado < 2000:
    resultado = a + b 
    a = b
    b = resultado
    if resultado > 2000: 
        break
    print(resultado)
    
   

    