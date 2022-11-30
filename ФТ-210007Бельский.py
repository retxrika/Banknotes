import os

def input_int(msg: str) -> int:
    '''
    Ввод целого числа с проверкой на ошибки.

    Параметры:
    msg - Информационное сообщение пользователю (type str). (Обязательный)

    Ошибки:
    Invalid input - Неверный ввод.
    Number must be greater than 0 - Число должно быть больше нуля.

    Возврат:
    Целое число введенное пользователем.
    '''
    invalid_input_err = 'Invalid input'
    out_range_err = f'Number must be greater than 0'

    # Возвращает форматированную строку ошибки.
    def get_error(text : str):
        return '\033[31m{}\033[0m'.format('ERROR: ' + text + '! Try again...')

    while True:
        try:
            num = int(input(msg + ': '))
        except:
            print(get_error(invalid_input_err))
            continue
        
        if  num <= 0:
            print(get_error(out_range_err))
            continue

        return num

if __name__ == '__main__':
    banknotes = [1, 2, 4, 8, 16, 32, 64]
    amount_banks = 0

    os.system('cls')    
    sum_total = input_int('Введите общую сумму')
    print('\nКупюра\tКоличество')
    
    # Уменьшаем sum_total пока не дойдет до нуля 
    # попутно печатая используемые купюры для вычета.
    while sum_total != 0:
        last_bank = banknotes[-1]
        residue = sum_total - last_bank

        if residue >= 0:
            sum_total -= last_bank
            amount_banks += 1

            if residue == 0:
                print(f'{last_bank}\t{amount_banks}')

        if residue < 0:
            if amount_banks > 0:
                print(f'{last_bank}\t{amount_banks}')
                amount_banks = 0
            banknotes.remove(last_bank)
