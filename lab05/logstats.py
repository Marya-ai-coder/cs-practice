
import locale
   
def parse_event(line:str) -> dict:

    parts = line.split(' ')
            
    time_str, level_str, *massages_list = parts

    lev = ['DEBUG','INFO','WARNING','ERROR']
    
    time = time_str.strip()

    try:
        level = level_str.strip()
        
        if level not in lev:
            raise ValueError('незнакомый уровень')
    except ValueError:
        level = 'BROKEN'

    

    massages = ' '.join(massages_list).rstrip('\n') #cp1251
    massage = massages.encode("cp1251").decode("utf-8")
    
    return {'time':time, 'level':level,'massage':massage }  #locale.getpreferredencoding()

def count_levels(lines: list[str])-> dict:
    parts = lines.split(' ')
    lvl = {}
    
    for l in lines:
        DEBUG ='DEBUG'
        INFO = 'INFO''ERROR'
        WARNING = 'WARNING'
        ERROR = parts['ERROR']
        BROKEN = 'BROKEN'

        lvl[ERROR] = lvl.get('ERROR',0) + 1

    return lvl

   
        
            
        

    
