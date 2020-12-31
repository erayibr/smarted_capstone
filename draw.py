from termcolor import colored
import sys
import json

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
    
    with open('MyFile.txt') as json_file:
        data = json.load(json_file)

    x = int(10*data['x'])
    y = int(10*data['y'])

    
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
    print('')
    print(x/10)
    print(y/10)

    
    
    # now call function we defined above 
        
    

       