num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
op = input("Введите требуемую операцию из + - * / : ")

while op != "+" and op != "-" and op != "*" and op != "/":
  print("Введена некорректная операция")
  op = str(input("Введите корректную операцию из + - * / : "))
else:
  if op == '+':
    print("Сумма равна: ", num1 + num2)
  elif op == '-':
    print("Разность равна: ", num1 - num2)
  elif op == '*':
    print("Произведение равно: ", num1 * num2)
  elif op == '/' and num2 != 0:
    print("Частное равно: ", num1 / num2)
  elif op == '/' and num2 == 0:
    print("Делить на ноль нельзя!")
    while num2 == 0:
      num2 = int(input("Измените второе число: "))
    else:
      print("Частное равно: ", num1 / num2)