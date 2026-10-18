import sys

from logstats import parse_event, list_levels

list_level = []

for line in sys.stdin:
    
    try:
        list_level.append(list_levels(parse_event(line)))
    except ValueError:
        list_level.append('BROKEN')
    
    print(list_level)
#if __name__=="__main__":
    #main()
