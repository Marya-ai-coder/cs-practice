
import locale
   
def parse_event(line:str) -> dict:

    parts = line.split(' ')
            
    time_str, level_str, *massages_list = parts

    lev = ['DEBUG','INFO','WARNING','ERROR']
    
    time = time_str.strip()

    level = level_str.strip()
    
    if level not in lev:
        raise ValueError('незнакомый уровень')
    
        
    massage = ' '.join(massages_list).rstrip('\n') #cp1251

    return {'time':time, 'level':level,'message':massage }

def list_levels(dict_pe: dict) -> str:
    
    return dict_pe.get('level')

def list_error(dict_pe: dict) -> str:
    
    if dict_pe['level'] == 'ERROR':
        return dict_pe.get('message')

def count_levels(lines: list[str])-> dict:
    
    count = {}

    for line in lines:
        try:
            e = parse_event(line)
            level = e.get('level')
        except ValueError:
            level = 'BROKEN'
            
        count[level] = count.get(level,0) + 1
        
    sorted_count = dict(sorted(count.items()))
    
    return sorted_count

def top_errors(lines:list[str], n:int) -> list[list]:

    top = {}
    for line in lines:
        try:
            e = parse_event(line)
            
            if e.get('level') == "ERROR":
                errorM = e.get('message')
                top[errorM] = top.get(errorM,0) + 1
        except ValueError:
            level = 'BROKEN'

    top_er = sorted(top.items(), key = lambda x: x[1], reverse = True)

    top_error = [list(i) for i in top_er[:n]]
                     
    return top_error
    

def format_report(counts: dict, errors: list[list]) -> str:
    st = []
    
    st.append('Отчёт по журналу\n\n')
    for n in counts.items():
        st.append(f'{n[0]}: {n[1]}\n')
    st.append('\nЧастые ошибки:\n')
    for n in errors:
        st.append(f'- {n[0]} - {n[1]}\n')
        
    res = ''.join(st)
    
    with open('report.txt','w', encoding='utf-8') as f:
        f.write(res)

        return res
    
    
            
        

    
