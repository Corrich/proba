answer_A = ["a"]
answer_B = ["b"]
answer_C = ["c"]
tak = ["T", "t"]
nie = ["N", "n"]
myinv = ["potion", "kamyk"]
miecz = 0
wojownik = 3
goblin = 4
wojownikzmieczem = 5
import random
random.randrange
from re import A
import time
wynikzmieczem = (random.randrange(1, 6) + wojownikzmieczem) - (random.randrange(1, 6) + goblin)
wynikbezmiecza = (random.randrange(1, 6) + wojownik) - (random.randrange(1, 6) + goblin)


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
            if wynikzmieczem > 0 :
                time.sleep(1)
                print("program wylicza wynik walki - masz miecz, większe szanse, że wygrasz")
                time.sleep(2)
                print ("Po zaciętej walce wygrałeś ze szkieletem! Gratuluję, zakończyłeś grę!")
            elif wynikzmieczem <= 0 :
                time.sleep(1)
                print("program wylicza wynik walki, masz miecz większe szanse, że wygrasz")
                time.sleep(2)
                print ("Szkielet pokonał Cię po zaciętej walce")
                print ("możesz zacząć od nowa:)")
                time.sleep(1)
                return wrota()
        elif x <1:
            if wynikbezmiecza > 0 :
                time.sleep(1)
                print ("Po zaciętej walce wygrałeś ze szkieletem mimo braku miecza! Gratuluję, zakończyłeś grę!")
            elif wynikbezmiecza <= 0 :
                time.sleep(1)
                print ("Szkielet cię pokonał, ale bez miecza miałeś naprawdę marne szanse")
                time.sleep(1)
                return wrota()

            
            
    if choice in answer_B:
        print ("dostałeś w plecy i dedłeś ")    
        time.sleep(2)
        return wrota()
        
wrota()
