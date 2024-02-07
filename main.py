import random, datetime

def is_number(str_to_check):
    while True:
        try:
            int(str_to_check)
            return True
        except ValueError:
            log_to_file('Введено не число', 'USER', 'ERROR')
            return False

def get_input(minmax, array):
    while True:
        str_to_check = input('Введите число: ')
        if not is_number(str_to_check):
            continue
        if not input_checked(str_to_check, minmax, array):
            continue
        return int(str_to_check)

# вынести вывод ошибки в отдельную функцию
def input_checked(str_to_check, minmax, array):
    if not minmax[0] <= int(str_to_check) <= minmax[1]:
        print(f'Число вне диапазона {minmax[0]} - {minmax[1]}.')
        log_to_file(f'Введено число {str_to_check} - вне диапазона {minmax[0]} - {minmax[1]}', 'USER', 'ERROR')
        return False
    if int(str_to_check) in array:
        print(f'Число уже использовалось ранее.')
        log_to_file(f'Введено число {str_to_check} - уже использовалось ранее', 'USER', 'ERROR')
        return False
    return True

def log_to_file(text, who='SYSTEM', prefix='INFO'):
    with open('log.txt', 'a', encoding='utf-8') as file:
        str_to_write = f'{str(datetime.datetime.now()).split('.')[0]} [{prefix}] [{who}]: {text}'
        file.write(str_to_write + '\n')

if __name__ == '__main__':

    less_than_num = []
    more_than_num = []

    minmax = (1, 100)

    num = random.randint(minmax[0], minmax[1])
    log_to_file(f'Загадано число {num}', 'SYSTEM')
    print(f'Загадано случайное число от {minmax[0]} до {minmax[1]}, попробуй угадать!')
    count = 0
    answer = 0
    while answer != num:
        count += 1
        print(f'Попытка №{count}')
        answer = get_input(minmax, less_than_num + more_than_num)
        if answer < num:
            print('Загаданное число больше введенного')
            less_than_num.append(answer)
        if answer > num:
            print('Загаданное число меньше введенного')
            more_than_num.append(answer)
        log_to_file(f'Попытка №{count}. Предложено число {answer}', 'USER')
    else:
        print(f'Ура, это и правда {num}. Потребовалось {count} попыток.')
        log_to_file(f'Угадано число {num}. Попыток: {count}', 'SYSTEM')
        log_to_file(f'Числа меньше заданного: {less_than_num}; Больше заданного: {more_than_num}')