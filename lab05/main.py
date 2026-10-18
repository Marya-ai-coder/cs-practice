import sys

from logstats import parse_event, list_levels, count_levels, list_error, \
     top_error
     

list_level = []
list_errors = []

for line in sys.stdin:
    
    try:
        list_level.append(list_levels(parse_event(line)))
    except ValueError:
        list_level.append('BROKEN')

    try:
        list_errors.append(list_error(parse_event(line)))
    except ValueError:
        list_errors.append('BROKEN')

    
#print(list_level)
print(count_levels(list_level))
print(top_error(list_errors,1))

def main():
    with open('report.txt','w',encoding='utf-8') as f:

#if __name__=="__main__":
    #main()
