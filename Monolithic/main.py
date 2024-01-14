from calculator.operations import addition, subtraction, multiplication, division
import time


def calculator():
    while True:
        print('-----------------------------------------')
        print("Escolha a operação que deseja fazer:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        option = input("Digite o número da operação desejada: \n")

        if(option == '0'):
            print("A calculadora está sendo encerrada...")
            time.sleep(1)
            exit()
        
        try:
            num1 = int(input("Escolha o primerio valor: "))
            num2 = int(input("Escolha o segundo valor: "))
            operation(option, num1, num2)
        except ValueError:
            print("Talvez os valores escolhidos não estão corretos ou a operação não exista. Tente novamente")
            break


def operation(option, num1, num2):
    if option == '1':
        print(f'Resultado da operação: {addition(num1, num2)} \n')
        print('-----------------------------------------')
    elif option == '2':
        print(f'Resultado da operação: {subtraction(num1, num2)} \n')
        print('-----------------------------------------')
    elif option == '3':
        print(f'Resultado da operação: {multiplication(num1, num2)} \n')
        print('-----------------------------------------')
    elif option == '4':
        print(f'Resultado da operação: {division(num1, num2)} \n')
        print('-----------------------------------------')
    else:
        print("Não existe nenuma operação desse tipo. Tente novamente. \n")
        print(('-----------------------------------------'))
        

if __name__ == "__main__":
    calculator()