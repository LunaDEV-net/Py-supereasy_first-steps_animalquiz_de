"""Tierquiz aus 'Progammieren mit Python supereasy'(ISBN'978-3-8310-3457-4')[S.36]"""
#Fragen by fraujoolie (https://create.kahoot.it/details/58988a75-ca0e-48a0-a2c4-a95f02eabb07)
#Quelle Welt (https://www.welt.de/kmpkt/article159843804/Das-schnellste-fliegende-Tier-ist-gar-kein-Vogel.html)
#def clear by (https://www.delftstack.com/de/howto/python/python-clear-console/)
#code by @Greenbyte
    #2022-04-02

import time
import os

points = 0

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def shutdown(duration, points, message, shutdownmessage):
    durationleft = duration
    print()
    print("-----------------------------------------------")
    print()
    print(message)
    print("Deine Punktzahl ist " + str(points))
    print()
    print(shutdownmessage + str(duration) + " sekunden")
    print()
    print("-----------------------------------------------")
    while durationleft > 1:
        durationleft = durationleft - 1
        clear()
        print()
        print("-----------------------------------------------")
        print()
        print(message)
        print("Deine Punktzahl ist " + str(points))
        print()
        print(shutdownmessage + str(durationleft) + " sekunden")
        print()
        print("-----------------------------------------------")
        time.sleep(1)
    quit()
    

#Überprüfung der Antwort
def test_q(question, answer):
    global points
    stillguess = True
    tries = 0
    if question == "exit":
        shutdown(int(5), points, 'Du hast den Befehl "exit" aus geführt', "Exit in ")
    while stillguess and tries < 3:
        if question.lower() == answer.lower():
            print("Richtige Antwort")
            points = points + 1
            stillguess = False
        else:
            if tries < 2:
                question = input("Flasch. Versuche es erneut: ")
            tries = tries + 1
    if tries == 3:
        print("---------------------------------------")
        print("Die richtige Antword ist " + answer)
        shutdown(int(5), points, 'Du hast deine 3 Versuche aufgebraucht, deswegen musst du von vorne Starten', "Programmschliesung in ")

#Erkärung
print()
print("Rate das Tier")
print()
print("""Schreibe welches Tier deise Eigenschaften hat.
(Groß/Kleinschreibung egal)
Schreibe 'exit' um das Programm zu Schliesen""")

repeatquestion = "j"

while repeatquestion == "j": 
    #fragen
    q1 = input("Welcher Bär lebt am Nordpol? ")
    test_q(q1, "Eisbär")

    q2 = input("Es ist das schnellste Landtier. ")
    test_q(q2, "Gepard")

    q3 = input("Dieses Tier soll man an der Leine führen, es ist für viele Leute ein echter Freund. ")
    test_q(q3, "Hund")

    q4 = input("Dieses Tier kann gut springen, es trägt das Baby in einem Beutel. ")
    test_q(q4, "Känguru")

    q5 = input("Das schnellste fliegende Tier. ")
    test_q(q5, "Fledermaus")

    q6 = input("Größtes Tier. ")
    test_q(q6, "Blauwal")

    #ergebnis
    print("Deine Punktzahl ist " + str(points))

    repeatquestion = input("Noch eine Runde spielen?(j/n) ")

#Ende
shutdown(int(5), points, 'Du willst also keine weitere Runde Spielen,', "OK, ende in ")