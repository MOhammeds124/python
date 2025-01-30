'''
Mohammed sayaim
''' 
import os 
from os import path 
def askinfo():
    checkpoint= "askinfo" 
    whichoption= int(input("1-create a new file \n""2-search for existing file \n""select option by typing 1 or 2:"))
    checkinfo(whichoption,checkpoint) 
def checkinfo(optionwhich,pointcheck):
    checkvalue= str(optionwhich)
    checkvalue= ord(checkvalue)
    match(pointcheck):
        case 'askinfo':
            if(int(checkvalue)<49 or int(checkvalue)>50):
                print("please input 1 or 2")
                askinfo()
            else: 
                print("You have chosen wisely")
                askinfo()
        case default: 
            print("huston... we have a problem")
        
    
def main():
    askinfo()


if __name__=="__main__":
    main()