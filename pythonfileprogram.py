'''
Mohammed sayaim
''' 
import os 
from os import path
import sys
global checkpoint, whichoption
msg=["new file name:","existing file name:"]

def askinfo():
    checkpoint= "askinfo" 
    whichoption= str(input("1-create a new file \n""2-search for existing file \n""3- exit the program\n""select option by typing 1,2, or 3:"))
    checkinfo(whichoption,checkpoint) 
def checkinfo(optionwhich,pointcheck):
    global whichfilename
    match(pointcheck):
        case 'askinfo':
            checkvalue= ord(optionwhich)
            if(int(checkvalue)<49 or int(checkvalue)>51):
                print("please input 1 or 2")
                askinfo()
            else:
                match(optionwhich):
                    case '1':
                        whichfilename= str(input(msg[0]))
                    case '2':
                        whichfilename= str(input(msg[1]))
                    case '3':
                        exitprogram()
                    case default:
                        print("huzzton... we have a problem")
                        sys.exit()

                whichfilename= whichfilename+".doc"
                FileConnectivity()
                askinfo()
        case 'exitprogram':
            checkvalue= ord(optionwhich)
            if(int(checkvalue)==121 or int(checkvalue)== 110):
                if(optionwhich== "y"):
                    sys.exit()
                else:
                    askinfo()
            else:
                print("please type y or n")
                exitprogram()
                
        case default: 
            print("huzzton... we have a problem")
            sys.exit()
def exitprogram():
    checkpoint= "exitprogram"
    whichoption= str(input("are you sure? \n""type y for yes and n for no:"))
    checkinfo(whichoption,checkpoint)
    
def FileConnectivity():
    fileDir= os.path.dirname(os.path.realpath("__file__"))
    fileexist=bool(path.exists(whichfilename))

    if (fileexist==True):
        adminfile=open(whichfilename,"r")
    else:
        adminfile=open(whichfilename,"x")

    adminfile.close()
        
    
def main():
    askinfo()


if __name__=="__main__":
    main()
