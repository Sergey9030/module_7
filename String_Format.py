name1 = 'Мастера кода'                                    # Название первой команды
name2 = 'Волшебники данных'                               # Название второй команды
team1_num = 6                                             # Количество участников первой команды
team2_num = 3                                             # Количество участников второй команды
score1 = 40                                               # Решено заданий первой командой
score2 = 20                                               # Решено заданий второй командой
team1_time = 160                                          # Затрачено времени первой командой
team2_time = 160                                          # Затрачено времени первой командой
tasks_total = score1 + score2                             # Всего решено заданий
time_avg = (team1_time + team2_time) / (score1 + score2)  # Среднее время выполнения задания
time1_avg = (team1_time * team1_num) / score1             # Трудозатраты на 1 задание у первой команды
time2_avg = (team2_time * team2_num) / score2             # Трудозатраты на 1 задание у второй команды
challenge_result = ''                                     # Победитель турнира

# Побеждает тот, у кого меньше затраты человекосекунд на 1 задание

if time1_avg == time2_avg:
    challenge_result = 'Дружба'
elif time1_avg < time2_avg:
    challenge_result = 'команда '+name1
else:
    challenge_result = 'команда '+name2

# Использование %:
print('В команде %s участников: %s !' % (name1, team1_num))
print('В команде %s участников: %s !' % (name2, team2_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# Использование format():
print('Команда {} решила задач: {} !'.format(name2, score2))
print('{} решили задачи за {} с !'.format(name2, team2_time))
print('Команда {} решила задач: {} !'.format(name1, score1))
print('{} решили задачи за {} с !'.format(name1, team1_time))

# Использование f-строк:
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: победила {challenge_result}!')
