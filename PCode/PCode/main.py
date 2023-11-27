import os
import time
os.system('cls')
print("Starting Gesture Recognition......")
time.sleep(2)
os.system('cls')
outloop =  1
while outloop==1:
    inloop = 1
    print('_______________________________________')
    print('Choose the Following:')
    print('_______________________________________')
    print('1.One Hand Detection(Computer Controls)')
    print('2.Two Hand Detection(Gesture Detection)')
    print('3.Exit')
    print('_______________________________________')
    id = int(input('Enter your Option: '))
    os.system('cls')

    if id==1:
        while inloop==1:
            print('_______________________________________')
            print('Choose the Following:')
            print('_______________________________________')
            print('1.Start One Hand Detection')
            print('2.Start Dynamic Gesture Training')
            print('3.Start Static Gesture Training')
            print('4.Go Back')
            print('5.Exit')
            print('_______________________________________')
            inid = int(input('Enter your option: '))
            os.system('cls')
            if inid==1:
                print('--------------------------')
                print('Starting Gesture Detection')
                print('--------------------------')
                
                os.system('python 1H/Detection1H.py')
                
                print('-------------------------')
                print('Gesture Detection Stopped')
                print('-------------------------')
                time.sleep(2)

            elif inid==2:
                print('---------------------------------')
                print('Starting Dynamic Gesture Training')
                print('---------------------------------')
                os.system('python 1H/Dynamic.py')
                print('---------------------------------')
                print('Dynamic Gesture Training Stopped')
                print('---------------------------------')
                time.sleep(2)

            elif inid==3:
                print('--------------------------------')
                print('Starting Static Gesture Training')
                print('--------------------------------')
                os.system('python 1H/Static.py')
                print('--------------------------------')
                print('Static Gesture Training Stopped')
                print('--------------------------------')
                time.sleep(2)
            
            elif inid==4:
                print('-------------------')
                print('Going Back')
                print('-------------------')
                inloop = 0
                time.sleep(2)
            
            elif inid==5:
                print('-------------------')
                print('Closing Program')
                print('-------------------')
                time.sleep(2)
                exit()
            else:
                print('------------------------')
                print('Choose the GIVEN OPTIONS')
                print('------------------------')
                time.sleep(2)
            os.system('cls')

        
    elif id==2:
        while inloop==1:
            print('_______________________________________')
            print('Choose the Following:')
            print('_______________________________________')
            print('1.Start Two Hand Detection')
            print('2.Start Dynamic Gesture Training')
            print('3.Start Static Gesture Training')
            print('4.Go Back')
            print('5.Exit')
            print('_______________________________________')
            inid = int(input('Enter your option: '))
            os.system('cls')
            if inid==1:
                print('--------------------------')
                print('Starting Gesture Detection')
                print('--------------------------')
                os.system('python 2H/Detection2H.py')
                print('-------------------------')
                print('Gesture Detection Stopped')
                print('-------------------------')
                time.sleep(2)

            elif inid==2:
                print('---------------------------------')
                print('Starting Dynamic Gesture Training')
                print('---------------------------------')
                os.system('python 2H/Dynamic.py')
                print('---------------------------------')
                print('Dynamic Gesture Training Stopped')
                print('---------------------------------')
                time.sleep(2)

            elif inid==3:
                print('---------------------------------')
                print('Starting Static Gesture Training')
                print('---------------------------------')
                os.system('python 2H/Static.py')
                print('---------------------------------')
                print('Static Gesture Training Stopped')
                print('---------------------------------')
                time.sleep(2)
            
            elif inid==4:
                print('-------------------')
                print('Going Back')
                print('-------------------')
                inloop = 0
                time.sleep(2)
            
            elif inid==5:
                print('-------------------')
                print('Closing Program')
                print('-------------------')
                time.sleep(2)
                exit()
            else:
                print('------------------------')
                print('Choose the GIVEN OPTIONS')
                print('------------------------')
                time.sleep(2)
            os.system('cls')            

    elif id == 3:
        exit()
    
    else:
        print('------------------------')
        print('Choose the GIVEN OPTIONS')
        print('------------------------')
        time.sleep(2)
        os.system('cls') 