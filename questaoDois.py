def questaoDois():
  num = int(input("Informe um número: "))
  a, b = 0, 1

  if num == 0 or num == 1:
    print(f"O número {num} pertence à sequência de Fibonacci.")
    return


  while b <= num:
    if b == num:
      print(f"O número {num} pertence à sequência de Fibonacci.")
      return

    a, b = b, a + b

  print(f"O número {num} não pertence à sequência de Fibonacci.")

questaoDois()