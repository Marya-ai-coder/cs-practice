def parse_record(line:str): # -> dict
    
    # разбирает строку "город;температура;дата" в словарь Негодная строка - ValueError
    
    parts = line.splite(';') # список ["город";"температура";"дата"]

    # проверяем на ошибку в колличестве введенного
    if len(parts) != 3:
        raise ValueError(f'Ожидалось 3 поля через ";", получено {len(parts)}')

    #присваиваем значения переменным из списка ( не забываем, что они в формате str)
    city_str,temp_str,date_str = parts 

    city = city_str.strip() # .strip() уберет пробелы если они есть
    if not city:
        raise ValueError('Пустое название города в строке')

    try: # попробуем преобразовать температуру если она число
        temp = float(temp_str)
    except: # если не получилось
        raise ValueError(f' Неудалось преобразовать температуру {temp_str} в число')

    date = date_str.strip()
    if not date:
        raise ValueError('Пустое значение даты')

    # возвращаем результат в виде словаря
    return {'city':city,'temp':temp,'date':date}
     
def read_valid(lines: list[str]): # -> list[dict]
    # разбирает строки журнала, пропуская пустые и негодные
    try:
    except:

def average_by_city(records: list[dict]): # -> dict
    # средняя температура по каждому городу округленная по десятых

def warmes_city(records: list[dict]): # ->str
    # город с наибольшей средней температурой. При равенстве - первый по алфавиту
    
