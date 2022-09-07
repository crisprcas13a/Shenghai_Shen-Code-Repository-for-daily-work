import time
import keyboard
import  os
a=["zhang","shen","sss"]
number=len(a) 
luckey=0   
def getluckyguy(a):
    # os.system('pause')
    i=0
    while True:

            if keyboard.is_pressed('\r'):
                break
            print('\r'+a[i])
            i+=1
            global luckey
            if i== len(a):
                i=0
            time.sleep(0.1)
            luckey=a[i]
        
def main():
        getluckyguy(a)
    
                
main()