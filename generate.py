#!/usr/bin/env python3
import sys,random

used= []
setofchars="3489RYUPDFHJKZCVN";
# setofchars="12345"
#codelength=4
codelength=9

def validcode(code,used):
    is_valid = not(code in used)
    # if not is_valid:
    # print("not valid",code)
    return is_valid

def generate_code():
    generated = []
    for n in range(codelength):
        selectedchar = str(setofchars[random.randrange(len(setofchars))])
        while selectedchar in generated:
            selectedchar = str(setofchars[random.randrange(len(setofchars))])
#            print ("selected")
#            print (selectedchar)
        generated.append(selectedchar)
#        print(generated)
        
    part = ''.join(generated)
    newcode = "Q"+ part
    return newcode

def main():
    if (len(sys.argv)<2):
        print ("./generate.py <howmany>")
        exit(1)
    howmany = int(sys.argv[1])
        
    ignorefile = open("ignore","r")
    lines = ignorefile.readlines()
    for y in lines:
        used.append(y.rstrip())
    
    for x in range(howmany):
        newcode = generate_code();
        while (not validcode(newcode,used)):
            newcode = generate_code()
            
        print (newcode)
        used.append(newcode)
        
if __name__ == "__main__":
    main()
