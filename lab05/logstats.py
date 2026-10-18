
import locale
   
def parse_event(line:str) -> dict:

    parts = line.split(' ')
            
    time_str, level_str, *massages_list = parts

    lev = ['DEBUG','INFO','WARNING','ERROR']
    
    time = time_str.strip()

    level = level_str.strip()
    
    if level not in lev:
        raise ValueError('незнакомый уровень')
    
        
    massages = ' '.join(massages_list).rstrip('\n') #cp1251
    massage = massages.encode("cp1251").decode("utf-8")
    
    return {'time':time, 'level':level,'massage':massage }  #locale.getpreferredencoding()


def list_levels(dict_pe: dict) -> str:
    
    return dict_pe.get('level')

#def count_levels(lines: list[dict])-> dict:
    
    

    

    
    
#def top_errors(lines:list[str], n:count) -> list[list]:

    

#def format_report(counts: dict,errors: list[list]) -> str:
    # errors : list[list] - top_errors
    # counts : dict - count_levels 
   
        
            
        

    
