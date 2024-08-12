class Calculadora:
    
    def somar(num1, num2):
        return int(num1 + num2)
  
    def maiorNumero(num1, num2):
        if num1 == num2:
            return 'Os dois números são iguais'
        return f'O maior número é {max(num1, num2)}'

    
    def diferenca(numero1, numero2):
        return abs(numero1 - numero2)
