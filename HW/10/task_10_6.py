# Дан файл, содержащий различные даты.
# Каждая дата - это число, месяц и год. Найти самую раннюю дату. [02-8.1-ML-29]

birthday_list = []
with open('task_10_6_1.txt', "r") as birthday:
    for line in birthday.readlines():
        birthday_list.append(line)
counter = 0
length = len(birthday_list)
youngest = birthday_list[0].strip().split('-')
for i in range(1, length):
    pretendent = birthday_list[i].strip().split('-')
    if int(youngest[2]) < int(pretendent[2]):
        youngest = pretendent
    else:
        if int(youngest[2]) == int(pretendent[2]):
            if int(youngest[1]) < int(pretendent[1]):
                youngest = pretendent
            else:
                if int(youngest[1]) == int(pretendent[1]):
                    if int(youngest[0]) < int(pretendent[0]):
                        youngest = pretendent
print('-'.join(youngest))
