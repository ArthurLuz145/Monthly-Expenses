#! python3

# Algortimo para calcular as contas do mês
# Colocar os valores pagos por cada um e o algoritmo calcula quanto e quem está devendo para quem.

import datetime
import easygui

var_today = datetime.datetime.today()
var_today = datetime.datetime.strftime(var_today, '%d-%m-%Y')

# Input the amount of people that paid something


# Input the name of the people that paid

name_1 = easygui.enterbox("First person that paid:")
name_2 = easygui.enterbox("Second person that paid:")

# Creation of lists with the values that were paid

list_name_1 = easygui.enterbox("How much did " + name_1 + " paid?")
list_name_1 = list_name_1.split()
list_name_1 = [int(i) for i in list_name_1]

list_name_2 = easygui.enterbox("How much did " + name_2 + " paid?")
list_name_2 = list_name_2.split()
list_name_2 = [int(i) for i in list_name_2]

# Algorithm to calculate the total for each person.
total = sum(list_name_1) + sum(list_name_2)
total_div = total / 2
tt_name_1 = total_div - sum(list_name_2)

if tt_name_1 < 0:
    owe_message = (name_1 + " owe " + str(-tt_name_1) + " to " + name_2)
else:
    owe_message = (name_2 + " owe " + str(tt_name_1) + " to " + name_1)

# Shows the totals in a message box.

easygui.msgbox("The total paid by " + str(name_1) + " is " + str(sum(list_name_1)) + "\nThe total paid by " + str(name_2) + " is " + str(sum(list_name_2)) + "\nThe monthly total expenses were " + str(total) + "\n\n" + owe_message)

# Logs the totals into a TXT file

line_message = ['\n', 'Closing date ' + str(var_today), "The total that " + str(name_1) + " paid this month was: " + str(sum(list_name_1)), 'The total that ' + str(name_2) + ' paid this month was: ' + str(sum(list_name_2)),  'Total spent this month was : ' + str(total)]
monthly_expenses_log = open('C:\\Users\\tuilu\\Documents\\Contas do mês\\ResumoContas.txt', 'a')

for line in line_message:
    monthly_expenses_log.write(line)
    monthly_expenses_log.write('\n')


monthly_expenses_log.close()
