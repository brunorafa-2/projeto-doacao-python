import time
# abertura do programa
print (" \033[30mGERENCIE SUA DOAÇÃO \033[m".center(65))
time.sleep(1)
print (" ")
print (" ")
sal = float (input ("\033[30mDigite seu salário: R$ \033[m"))
time.sleep(0.5)
porcentagem_doar = float (input ("\033[30mDigite a porcentagem da doação: \033[m"))
time.sleep(0.5)
print (" ")

# calculo
calculo = sal * (porcentagem_doar / 100)

# resultado
print (f"Você pode doar o valor de \033[30mR${calculo:.2f}\033[m")
print (" ")
if porcentagem_doar <= 10:
    print ("\033[30mBoa escolha! Doação consciente.\033[m")
elif porcentagem_doar <= 20:
    print ("\033[30mAtenção: verifique se isso não compromete seus gastos.\033[m")
else:
    print ("\033[31mALERTA: essa porcentagem pode comprometer sua renda.\033[m")

print (" ")
print (" ")
# final
print (" \033[32mCADA MÊS É ALGO NOVO E VALORES NOVOS. DOE, NEM QUE SEJA 1%! IRÁ AJUDAR MUITAS PESSOAS, MESMO COM POUCO!\033[m ".center(65))
