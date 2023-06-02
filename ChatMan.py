import datetime #en modul som gjør at python kan fortelle deg dato og tid
import random #modul som gjør at python kan velge en tilfeldig objekt fra en liste

liste = ["navn, alder, funfact, dato, spesifik dato; år, måned, dag, uke, klokke, enkel matte; plus, minus, gange, dele, vis du ikke skjøner svaret kan du spørre 'hvorfor', forr å få op listen over spørsmål skriv 'liste'"]
navn = ["i'm the ChatMan. Ski-bi dibby dib yo da dub dub", "det sier jeg ikke", "jeg er The ChatMan", "Ski-bi dibby dib yo da dub dub"]
vorfor = ["for at du skal ha noe å lure på", "vatta faen", "idk", "¯\_(ツ)_/¯", "fordi"]
funfact = ["under krigen om Pelusium festet de persiske soldatene katter till skjoldene sin så egypterne ikke kunne slåss tilbake", "det er ikke skjellet inni deg, du er en hjerne i en bein mech med kjøtt rustning", "babi koalaer spiser mamma koalaens drit som er vorfor nesten alle koalaer har klamydia"]

print("spørr meg va som helst fra listen under (ikke bruk spørsmåltegn)")

print(liste[0])


while True: #looper koden
    x = datetime.datetime.now() #gjør at jeg ikke trenger å skrive "datetime.datetime.now()" vær gang jeg vil bruke tiden, i stedet for kan jeg bare skrive "x"

    spørsmål=input(">")

    #navn
    if spørsmål == "navn":
        print(random.choice(navn))
    elif spørsmål == "hva er dit navn":
        print(random.choice(navn))
    elif spørsmål == "dit navn":
        print(random.choice(navn))
    elif spørsmål == "hva heter du":
        print(random.choice(navn))
    elif spørsmål == "hva er navnet dit":
        print(random.choice(navn))
    #alder
    elif spørsmål == "alder":
        print("jeg ble laget 31/05/23")
    elif spørsmål == "når ble du født":
        print("jeg ble laget 31/05/23")
    elif spørsmål == "hvor gammel er du":
        print("jeg ble laget 31/05/23")
    elif spørsmål == "hva er din alder":
        print("jeg ble laget 31/05/23")
    elif spørsmål == "når ble du laget":
        print("jeg ble laget 31/05/23")
    #funfact
    elif spørsmål == "funfact":
        print(random.choice(funfact))
    #dato
    elif spørsmål == "dato":
        print("datoen er", x.strftime("%x")) #"strftime" er for å kunne printe en spesifik del av datoen, "%x" er at den bare skal printe dato
    #dag
    elif spørsmål == "dag":
        print("i dag er det", x.strftime("%A"), "den", x.strftime("%d")) #"%A" er langt navn for ukedag, man kan få forkortet navn med "%a", "%d" er dagen i måneden
    #måned
    elif spørsmål == "måned":
        print("det er", x.strftime("%B")) #"%B" er det fulle navnet til måneden, man kan også få den til å printe en forkortet verson med "%b"
    #uke
    elif spørsmål == "uke":
            print("det er uke", x.strftime("%V")) #"%V" er uken i året fra 01-53, man kan få 00-53 hvor ukene starter på søndag med "%U" og starter på mandeg med "%W" (hvis du bruker de to siste kodene vil den printe forige uke)
    #klokke
    elif spørsmål == "klokke":
        print("klokka er", x.strftime("%H"), ":", x.strftime("%M"), "eller", x.strftime("%I"), ":", x.strftime("%M"), x.strftime("%p")) #"%H" er timen i døgnet på 24-timers klokke, "%M" er minutter, "%I" er timen i døgnet på 12-timers klokke, "%p" er AM og PM, du kan få vilket sekund det er med "%S"
    #år
    elif spørsmål == "år":
        print(x.year) #"x.year" printer vilket år det er, man kan også bruke "%Y" for fullt år, eller "%y" for forkortet år (om man bruker de to siste kodene må man ha med "strftime" etter "x.")
    #vorfor
    elif spørsmål == "hvorfor":
        print(random.choice(vorfor)) #printer en tilfeldig onjekt fra vorfor listen
    #liste
    elif spørsmål == "liste": #om du ikke husker listen og ikke gidder å scrolle oppover kan du skrive liste for å få se den på nytt
        print(liste[0])
    #plus
    elif spørsmål == "plus":
        number1 = input("første tallet:")
        number2 = input("andre tallet:")
        sum = int(number1)+int(number2) #plusser sammen de to tallene fra unputtene
        print("svaret er", str(sum)) #printer svaret
    #minus
    elif spørsmål == "minus":
        number1 = input("første tallet:")
        number2 = input("andre tallet:")
        subtract = int(number1)-int(number2) #trekker tallet fra første input fra talet fra andre input
        print("svaret er", str(subtract)) #printer svaret
    #gange
    elif spørsmål == "gange":
        number1 = input("første tallet:")
        number2 = input("andre tallet:")
        multiply = int(number1)*int(number2) #ganger tallene fra inputtene med hverandre
        print("svaret ditt er", str(multiply)) #printer svaret
    #dele
    elif spørsmål == "dele":
        number1 = input("første tallet:")
        number2 = input("andre tallet:")
        divide = int(number1)/int(number2) #deler talet fra første input med tallet fra andre input
        print("bibbedi bobbedi boo your answer is twenty two. nei da det er", str(divide)) #printer svaret

    else:
        print("så du ikke listen?") #om den ikke kjenner igejn det du ville at den skal gjøre gir den deg listen på nytt
        print(liste[0])