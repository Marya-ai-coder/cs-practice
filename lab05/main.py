
from logstats import parse_event, list_levels, count_levels, list_error, \
     top_errors, format_report
     
list_level = []
list_errors = []

path = input()

with open(path, encoding='utf-8') as f:
    for line in f:
    
        try:
            list_level.append(list_levels(parse_event(line)))
        except ValueError:
            list_level.append('BROKEN')

        try:
            list_errors.append(list_error(parse_event(line)))
        except ValueError:
            list_errors.append('BROKEN')
            
#print(list_level)
#print(count_levels(list_level))
#print(list_errors)

def main():
    format_report(count_levels(list_level), top_errors(list_errors,3))

    with open('report.txt','w',encoding='utf-8') as f:
        f.write(str(len(list_level))+'\n')
        f.write(str(list_level.count('ERROR'))+'\n')
        
        if len(list_level) != 0:
            f.write(str(list_level.count('BROKEN')))
    
if __name__=="__main__":
    main()
