#! python3

# Algortimo para calcular as contas do mês
# Colocar os valores pagos por cada um e o algoritmo calcula quanto e quem está devendo para quem.

import datetime

dia_de_hoje = datetime.datetime.today()
dia_de_hoje = datetime.datetime.strftime(dia_de_hoje, '%d-%m-%Y')

# Criação de listas com os valores de pagamentos.
print('Quais são os valores que a Paola pagou?')
listpaola = [int(x) for x in input().split()]

print('Quais são os valores que o Arthur pagou?')
listarthur = [int(x) for x in input().split()]

# Cálculo dos totais para cada um.
total = sum(listarthur) + sum(listpaola)
totaldiv = total / 2
ttpaola = totaldiv - sum(listpaola)

# Mostra os totais no console.
print('Total da Paloa é ' + str(sum(listpaola)))
print('Total do Arthur é ' + str(sum(listarthur)))
print('Total do mês é ' + str(total))

# Final, mostra quem deve para quem de acordo com os calculos anteriores.
if ttpaola > 0:
    print('A Paola deve ' + str(ttpaola) + ' para o Arthur')
else:
    print('O Arthur deve ' + str(-ttpaola) + ' para a Paola')

linhas = ['\n', 'Data fechamento ' + str(dia_de_hoje), 'O total da Paola no mês foi: ' + str(ttpaola), 'O total do Arthur no mês foi: ' + str(sum(listarthur)), 'O total gasto no mês foi: ' + str(total)]
contas_do_mes_log = open('C:\\Users\\tuilu\\Documents\\Contas do mês\\ResumoContas.txt', 'a')

for line in linhas:
    contas_do_mes_log.write(line)
    contas_do_mes_log.write('\n')


contas_do_mes_log.close()
