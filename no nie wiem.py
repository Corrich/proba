answer_A = ["a"]
answer_B = ["b"]
tak = ["T", "t"]
nie = ["N", "n"]

miecz = 0

def wrota():
    print("otwierają się wielkie stalowe wrota, co robisz:")
    print("""a rozbrajasz pułapki
    b wchodzisz z buta""")
    choice = input(">>> ")
    if choice in answer_A:
        option_korytarz()
    elif choice in answer_B:
        print ("dedles!")
        option_odpoczatku()
        
    
def option_korytarz():
    print("widzisz wąską ścieżkę")
    print("""co robisz
    a biegniesz
    b idziesz ostrożnie""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("poślizgnołeś się wpadłeś w kolce no i dedłeś!")
        option_odpoczatku()
    elif choice in answer_B:
        option_komnata1()

def option_komnata1():
    print("""widzisz dużą komnatę. W środku namalowany jest pentagram, jeśli chcesz go użyć wybierz a
    jeśli chcesz przejść przez całą komnatę wybierz b""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("czujesz że się teleportujesz i cofa cię do korytarza!")
        option_korytarz
    elif choice in answer_B:
        option_komnata2()

def option_komnata2() :
    print("na ziemi leży miecz, chcesz go podnieść T/N")
    choice = input(">>> ")
    if choice in tak:
        miecz = 1 
    else:
        miecz = 0
    print ("\nAtakuje cię szkielet!!!")
    
    print ("""  co robisz
    A. Walczysz
    B. Uciekasz""")
    choice = input(">>> ")
    if choice in answer_A:
        if miecz > 1:
            print ("pokonujesz szkieleta")
            print ("wygrywasz grę")
        else :
            print ("bez miecza nie masz szans. Dedłeś!")
    elif choice in answer_B:

        print ("dostajesz w plecy i dedłeś")

def option_odpoczatku():
    print ("odrodzenie. Zaczynasz od nowa!")
    choice = input(">>> ")
    option_korytarz
wrota()
