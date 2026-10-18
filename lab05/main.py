import sys

from logstats import parse_event, count_levels


for line in sys.stdin:

    print(type(line))
    print(parse_event(line))
    #lines = line.split(' ')    
    #print(count_levels(lines))

    
#if __name__=="__main__":
    #main()
