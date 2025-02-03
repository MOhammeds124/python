'''
Mohammed sayaim
''' 
import os 
from os import path

msg=["new file name:","existing file name:"]

def askinfo():
    checkpoint= "askinfo" 
    whichoption= str(input("1-create a new file \n""2-search for existing file \n""select option by typing 1 or 2:"))
    checkinfo(whichoption,checkpoint) 
def checkinfo(optionwhich,pointcheck):
    global whichfilename
    match(pointcheck):
        case 'askinfo':
            checkvalue= ord(optionwhich)
            if(int(checkvalue)<49 or int(checkvalue)>50):
                print("please input 1 or 2")
                askinfo()
            else:
                if (optionwhich== 1):
                    whichfilename= str(input(msg[0]))
                else:
                    whichfilename= str(input(msg[1]))

                whichfilename= whichfilename+".doc"
                FileConnectivity()
                askinfo()
        case default: 
            print("huzzton... we have a problem")
            sys.exit()
def FileConnectivity():
    fileDir= os.path.dirname(os.path.realpath("__file__"))
    fileexist=bool(path.exists(whichfilename))

    if(fileexist==True):
        adminfile=open(whichfilename,"r")
    else:
        adminfile=open(whichfilename,"x")

    adminfile.close()
        
    
def main():
    askinfo()


if __name__=="__main__":
    main()
