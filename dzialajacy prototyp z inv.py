answer_A = ["a"]
answer_B = ["b"]
answer_C = ["c"]
tak = ["T", "t"]
nie = ["N", "n"]
myinv = ["potion", "kamyk"]
miecz = 0
from re import A
import time

def wrota():
    print("otwierają się wielkie stalowe wrota, co robisz:")
    print("""a rozbrajasz pułapki
    b wchodzisz z buta
    c sprawdzasz co masz w kieszeni""")
    choice = input(">>> ")
    if choice in answer_A:
        option_korytarz()
    elif choice in answer_B:
        print ("dedles! zacznij od nowa")
        time.sleep(2)
        return wrota()
    elif choice in answer_C:
        print (myinv)
        time.sleep(1)
        return wrota()
        


        
    
def option_korytarz():
    print("widzisz wąską ścieżkę")
    print("""co robisz
    a biegniesz
    b idziesz ostrożnie""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("poślizgnołeś się wpadłeś w kolce no i dedłeś!")
        time.sleep(2)
        return wrota()
    elif choice in answer_B:
        option_komnata1()

def option_komnata1():
    print("""widzisz dużą komnatę. W środku namalowany jest pentagram, jeśli chcesz go użyć wybierz a
    jeśli chcesz przejść przez całą komnatę wybierz b""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("czujesz że się teleportujesz i cofa cię do korytarza!")
        time.sleep(1)
        return option_korytarz()
    elif choice in answer_B:
        option_komnata2()


def option_komnata2() :
    print("na ziemi leży miecz, chcesz go podnieść T/N")
    choice = input(">>> ")
    if choice in tak:
       myinv.append("miecz")
       option_komnata3()
    else:
        
        option_komnata3()


def option_komnata3():

    print ("\nAtakuje cię szkielet!!!")
    
    print ("""  co robisz
    A. Walczysz
    B. Uciekasz
    C. Sprawdzasz plecak""")
    choice = input(">>> ")
    if choice in answer_A:
                
        x = myinv.count("miecz")
        if x == 1:
    
            print ("pokonujesz szkieleta")
            print ("wygrywasz grę")
        elif x <1:
            print ("bez miecza nie masz szans. Dedłeś!")
            return wrota()
    if choice in answer_B:
        print ("dostałeś w plecy i dedłeś ")    
        time.sleep(2)
        return wrota()
        
wrota()
