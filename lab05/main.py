import sys

from logstats import parse_event, list_levels, count_levels, list_error, \
     top_errors, format_report
     

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

def main():
    format_report(list_level, count_levels)

if __name__=="__main__":
    main()
