from Calculadora import Calculadora
calc = Calculadora(10, 5, '+')
calc.mostrarResultado()
calc.valorA = 20
calc.valorB = 10
calc.operacao = '-'
calc.mostrarResultado()
calc.operacao = '*'
calc.mostrarResultado()
calc.operacao = '/'
calc.mostrarResultado()
calc.valorB = 0
try:
    calc.mostrarResultado()
except SystemExit as e:
    print(e)
calc.operacao = '^'
try:
    calc.mostrarResultado()
except SystemExit as e:
    print(e)
