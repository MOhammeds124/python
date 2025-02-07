import sys 
import os 
from os import path 

msg= ["new file name", "existing file name"]
def main():
  askinfo() 

def askinfo(): 
  checkpoint= "askinfo"
  whichoption= str(input("1-create a new file\n"
                       "2-search for existing file\n"
                       "3-exit\n"
                       "select an option by typing 1,2 or 3:"))
  checkinfo(whichoption, checkpoint)
def checkinfo(optionwhich, pointcheck):
  global whichfilename 
  match (pointcheck): 
    case "askinfo": 
      optwhich= ord(optionwhich)
      if (optwhich<49 or optwhich>51): 
        print("incorrect response")
        askinfo()
      else:
        match(optionwhich): 
          case "1": 
            whichfilename= str(input(msg[0]))
          case "2": 
            whichfilename= str(input(msg[1]))
          case "3": 
            print("thank you") 
            sys.exit()
          case default: 
            print("huston we have a problem")
            sys.exit()
        whichfilename= whichfilename +".doc" 
        fileconnectivity() 
    case default: 
      print("huston we have a problem")
      sys.exit()
def fileconnectivity():
  global adminfile
  filedir= os.path.dirname(os.path.realpath('__file__')) 
  fileexist= bool(path.exists(whichfilename))
  if (fileexist==True): 
    print("file exists!")
    adminfile= open(whichfilename, "r")
  else: 
    yesno= str(input("file does not exist, would you like to create it?(y/n)")); 
    if yesno.upper()=="Y": 
      adminfile= open(whichfilename, "x") 
      collectinfo() 
      ifstart= str(input("would you like to preform another action?(y/n)")).upper() 
      if ifstart=="Y":
        askinfo() 
      else: 
        print("thank you")
        sys.exit()
    else: 
      sys.exit()

def collectinfo(): 
  print("lets start by creating a username and password for your file") 
  username=str(input("username:")) 
  password=str(input("password:"))
  Writetofile(username, password, whichfilename)
def Writetofile(name, passwd, thefile):
  adminfile= open(thefile,"w") 
  adminfile.write(name+""+passwd)
  adminfile.close()


if __name__== "__main__": 
  main()
