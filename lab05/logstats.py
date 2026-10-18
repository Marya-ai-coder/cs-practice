
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
    
    return {'time':time, 'level':level,'massage':massage }


def list_levels(dict_pe: dict) -> str:
    
    return dict_pe.get('level')

def list_error(dict_pe: dict) -> str:
    
    if dict_pe['level'] == 'ERROR':
        return dict_pe.get('massage')

def count_levels(lines: list[str])-> dict:
    
    count = {}

    for i in lines:
        count[i] = count.get(i,0) + 1

    return count

def top_errors(lines:list[str], n:count) -> list[list]:

    top = {}

    for i in lines:
        if i is not None:
            if i != 'BROKEN':
                top[i] = top.get(i,0) + 1

    top_er = sorted(top.items(), key = lambda x: x[1], reverse = True)

    return top_er[:n]
    

def format_report(counts: dict,errors: list[list]) -> str:
    
    with open('report.txt','w',encoding='utf-8') as f:
        f.write(str(len(counts))+'\n')
        f.write(str(counts.count('ERROR'))+'\n')
        
        if len(counts) != 0:
            f.write(str(counts.count('BROKEN')))
        
            
        

    
