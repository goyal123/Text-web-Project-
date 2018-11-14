''' '''
##with open('addout2.txt') as fp:
##    data = fp.readlines()
##
##with open("removed.txt",'w') as fp:
##    start=1
##    for line in data:
##        temp = line.replace(" ",'')
##        if "==Seealso==" in temp or "==Furtherreading==" in temp or "==Externallinks==" in temp or "==References==" in temp : start=0
##        #if "==See also==" in line or "== See also ==" in line or "==See also ==" in line: start=0
##        if "Category:" in line: start=1
##        if start: print(line,file=fp, end="")

'''     '''

##with open("removed.txt") as fp:
##    data = fp.readlines()
##
##with open("category.csv",'w') as fp:  
##    for line in data:
##        if "Category:" in line:
##            temp = line
##            temp = temp.replace("Category:","")
##            print(temp, file=fp, end="")

'''   RAW LINKS CODE  '''

##with open('demofile1.txt') as fp:
##    data = fp.readlines()
##
##with open("rawlinks.txt",'w') as fp:
##    start=1
##    for line in data:
##        temp = line.replace(" ",'')
##        if  "==Externallinks==" in temp: start=0;continue
##        if "==" in line: start=1
##        if not start:
##            if line.startswith("* ["):
##                print(line, file=fp, end="")
		      

''' LINKS CODE  '''

##with open('rawlinks.txt') as fp:
##    data = fp.readlines()
##start=0
##with open("links.txt",'w') as fp:
##    for line in data:
##        if line.startswith("* [["): continue
##        for i in line:
##            if i == '[': start=1;continue
##            if i == ']': start=0;print(file=fp)
##            if start: print(i,file=fp,end="")


''' LINKS CSV CODE  '''

##with open('links.txt') as fp:
##    data = fp.readlines()
##
##with open("links.csv",'w') as fp:
##    for line in data:
##        if line.startswith("http"): print(line,file=fp,end="")      
    
''' CITE CODE  '''
##
##with open('demofile1.txt') as fp:
##    data = fp.readlines()
##
##start=0
##with open("cites.txt",'w') as fp:
##    for line in data:
##        temp = line.strip()
##        if start==1:print(line, file=fp, end="")
##        if start==1 and "}}" in temp: start=0
##        if temp.startswith("* {{cite") or temp.startswith("* {{Cite"):
##            print(line, file=fp, end="")
##            if not "}}" in temp: start=1
##            
##		      
