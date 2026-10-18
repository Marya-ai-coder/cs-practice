
from logstats import parse_event, list_levels, count_levels, list_error, \
     top_errors, format_report

def main():

    list_level = []
    list_errors = []
    
    lines = []
    
    path = input()
    
    with open(path, encoding='utf-8') as f:
        for line in f:
            
            lines.append(line)

            try:
                list_errors.append(list_error(parse_event(line)))
                list_level.append(list_levels(parse_event(line)))
                
            except ValueError:
                list_level.append('BROKEN')
                list_errors.append('BROKEN')
            
    format_report(count_levels(lines), top_errors(list_errors,3))

    print(str(len(list_level)))
    print(str(list_level.count('ERROR')))
        
    if len(list_level) != 0:
        print(str(list_level.count('BROKEN')))
    

if __name__=="__main__":
    main()
