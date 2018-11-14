start=0
with open('DemographicsofTurkmenistan.txt') as fp:
    data=fp.readlines()
    print(data[10])
    for line in data:
        print(line)
        if "| " in line:
            start=0
        elif "|" in line:
            start=1
        else: 
            print(line,file=fp,end="")
##    for temp in data:
##        if temp.startswith("{"):
##            continue
##        if temp=='}':
##            start=1
##        if start:print(i,file=fp,end="")
##    
##    data = fp.readlines()
##    start=0
##    for i in data:
##            if i == '{':continue
##            if i == '}': start=1
##            if start: print(i,file=fp,end="")
