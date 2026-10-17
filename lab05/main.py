import sys

from logstats import parse_event


def read_lines():
    with open("report.txt","w", encoding="utf-8") as rep:
        for line in sys.stdin:
            rep.write(parse_event(line)+'\n')
            #return parse_event(line)
            

def main():            
    print(read_lines())

    
if __name__=="__main__":
    main()
