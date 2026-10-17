import locale
   
def parse_event(line:str) -> dict:
    parts = line.split(' ')
    time_str, level_str, *massages_list = parts

    lev = ['DEBUG','INFO','WARNING','ERROR']
    
    time = time_str.strip()
    
    level = level_str.strip()
    if not level:
        raise ValueError("уровень не указан")
    if level not in lev:
        raise ValueError('незнакомый уровень')

    massages = ''.join(massages_list).strip() #cp1251
    massage = massages.encode("cp1251").decode("utf-8")
    
    return massage #{'time':time, 'level':level,'massage':massage }  #locale.getpreferredencoding()

def count_levels(lines)-> dict:

    
