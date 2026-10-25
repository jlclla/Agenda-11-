#Programa de Detecção de Níveis de Água
#Autor: Juliana de Lima Custódio

#Utilização Biblioteca Colorama para colorir o terminal

from colorama import Fore, Style

print("----------------------NÌVEIS DE ÁGUA NO RESERVATÓRIO------------------------")
print("/Situação nível/-/Porcentagem/-/ Mensagem de alerta/------------------------")
print(Fore.RED +    "Nível Crítico -      0-20%  -    Risco de falta de água")
print(Fore.YELLOW + "Nível Baixo   -     20-40%  -    Atenção - Possível falta de água")
print(Fore.GREEN +  "Nível Médio   -     40-60%  -    Nível de água adequado")
print(Fore.CYAN +   "Nível Alto    -     60-80%  -    Nível de água elevado")
print(Fore.BLUE +   "Nível Máximo  -     80-100% -    Reservatório cheio - Alerta de transbordamento")
print("----------------------------------------------------------------------------")
