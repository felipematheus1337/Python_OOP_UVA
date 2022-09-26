from curses.ascii import isdigit
from numbers import Number
from conta import Conta
import random

def main():
    
    print("BEM VINDO A REGISTER BANK ACCOUNT UVA!")
    
    titular = input('seu nome: ')
    numero = random.randrange(10000,20000,2)
    saldo = float(input('saldo: '))
    limite = float(input('limite: '))
    conta = Conta(numero,titular,saldo,limite)
    
    print("------------------------.----------------")
    print("BEM VINDO AO MAIN MENU OF BANK ACCOUNT UVA")
    print("------------------------.----------------")
    
    op = 5
    
    while op != 0:
        print("pressione 1 para extrato, pressione 2 para deposito, pressione 3 para sacar, pressione 0 para encerrar a sessão")
        
        op = input('')
        if(checkIfTheValueIsAnNumber(op)):
             if(int(op) == 0):
                 break
             elif(int(op) == 1):
                 conta.extrato()
                 
             elif(int(op) == 2):
                 print('valor de deposito : ')
                 valor_deposito = input('')
                 conta.deposita(float(valor_deposito))
    
             elif(int(op) == 3):
                print('valor de saque : ')
                valor_saque = input('')
                conta.saca(float(valor_saque))
                    
               
        else:
            print("Nas operações somente valores inteiros!! Por favor tente novamente")
            
            
            
            
def checkIfTheValueIsAnNumber(value):
        if(isdigit(value) == True):
            return True
        else:
            return False
            

        
    
    
if __name__ == "__main__":
    main()
    