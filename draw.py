x= 0
y = 0

from termcolor import colored
import sys

# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

while True:
    sleep(2) 
    clear()

    for i in range(35):
        print('', end='\n')
        for k in range (40):
            if(y == (34-i) and x == k):
                print(colored(chr(0x2588) + chr(0x2588) , 'red'), end = ' ')
            elif( (i == 34 and (k == 1 or k == 24)) or (i==0 and k == 26)): 
                print(colored(chr(0x2588) + chr(0x2588) , 'green'), end = ' ')
            else:
                print(colored(chr(0x2588) + chr(0x2588) , 'blue'), end = ' ')
    # sleep for 2 seconds after printing output 

    print(' ')
    
    
    # now call function we defined above 
        
    

       