def calculadora (num1, num2, operacao):

  if operacao ==1:
    return num1 + num2
  elif operacao ==2:
    return num1 - num2
  elif operacao ==3:
    return num1 * num2
  elif operacao == 4:
    return num1 / num2
  else:
    print("Operção invalida")

  print("Escolha a operação:")
  print("1 - soma\n2 - Subtração\n3 - Multiplicação\n4 - Divição")
operacao = int(input())

print("Digite o primeiro numero:")
num1 = float(input())
print("Digite o segundo numero")
num2 = float(input())

resultado = calculadora (num1, num2,operacao)
print("Resultado:", resultado)
 

