import random
import os
import time 
def exi():
    exit(0)
def menu():
    num=int(input("\n        MENU\n====================\ \n1.Single player      |\n2.Multiplayer        |\n3.Exit               |\n====================/ \n--> "))
    if num==1:
            def sing():
                n = random.randint(1,2)
                ra1='Heads'
                ra2='Tails'
                print("           Single player           \n------------------------------------------------")
                p1=int(input("Enter 1 for Heads and 2 for Tails: "))
                if n==p1 and p1==1:
                    time.sleep(0.3)
                    print("\nIt is {}! You won the Toss ".format(ra1))
                elif n!=p1 and p1==2:
                    time.sleep(0.3)
                    print("\nIt is {}! You lost the Toss ".format(ra1)) 
                elif n==p1 and p1==2:
                    time.sleep(0.3)
                    print("\nIt is {}! You won the Toss ".format(ra2))
                elif n!=p1 and p1==1:
                    time.sleep(0.3)
                    print("\nIt is {}! You lost the Toss ".format(ra2))
                repl = input("------------------\nDo you want to replay? y/n :\n------------------\n")
                if repl=='Y' or repl =='y':
                    os.system("cls")
                    sing()
                else:
                    os.system("cls")
                    menu()
            sing()
    if num==2:
            
            print("           Multiplayer           \n------------------------------------------------")
            nam=input("Do you want to Enter Players name? Y/N ")
            if nam=='Y' or nam=='y':
                n1=input("Enter Player-1 Name: ")
                n2=input("Enter Player-1 Name: ")
            elif nam=='N' or nam=='n':   
                p1=int(input("Player-1 Enter the 1 for Heads or 2 for Tails:  "))
                p2=int(input("Player-2 Enter the 1 for Heads or 2 for Tails:  "))
                n = random.randint(1,2)
                if p1==p2:
                    print("Don't enter the same number")
                elif n==p1:
                    print("")
                elif n==p2:
                    print("")
                if n==p1 and n==1:
                    print("It is Heads! Player-1 won the Toss\n")
                elif n==p1 and n==2:
                    print("It is Tails! Payer-1 won the Toss\n")
                elif n==p2 and n==1:
                    print("It is Heads! Player-2 won the Toss\n")
                elif n==p2 and n==2:
                    print("It is Tails! Player-2 won the Toss\n")
                #time.sleep(5)
                #os.system("cls")
                menu()    
            def nam1():
                p1=int(input("{} Enter the 1 for Heads or 2 for Tails:  ".format(n1)))
                p2=int(input("{} Enter the 1 for Heads or 2 for Tails:  ".format(n2)))
                n = random.randint(1,2)
                if p1==p2:
                    print("\nDon't enter the same number")
                elif n==p1 and n==1:
                    print("\nIt is Heads! {} won the Toss".format(n1))
                elif n==p1 and n==2:
                    print("\nIt is Tails! {} won the Toss".format(n1))
                elif n==p2 and n==1:
                    print("\nIt is Heads! {} won the Toss".format(n2))
                elif n==p2 and n==2:
                    print("\nIt is Tails! {} won the Toss".format(n2))            
                repl = input("------------------\nDo you want to replay? y/n :\n------------------\n")
                if repl=='Y' or repl =='y':
                    nam1()
                else:
                    os.system("cls")
                    menu()
            nam1()  
    if num==3:
        exi()
    else:
        print("Invalid Entry!")
        time.sleep(0.8)
        os.system("cls")
        menu()
menu()
