"""Tierquiz aus 'Progammieren mit Python supereasy'(ISBN'978-3-8310-3457-4')[S.36]"""
#Fragen by fraujoolie (https://create.kahoot.it/details/58988a75-ca0e-48a0-a2c4-a95f02eabb07)
#Quelle Welt (https://www.welt.de/kmpkt/article159843804/Das-schnellste-fliegende-Tier-ist-gar-kein-Vogel.html)
#code by @Greenbyte
    #2022-04-02

points = 0

#Überprüfung der Antwort
def test_q(question, answer):
    global points
    stillguess = True
    tries = 0
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
        print("Die richtige Antword ist " + answer)


print("Rate das Tier")

#fragen

q1 = input("Welcher Baer lebt am Nordpol? ")
test_q(q1, "Eisbaer")

q2 = input("Es ist das schnellste Landtier. ")
test_q(q2, "Gepard")

q3 = input("Dieses Tier soll man an der Leine führen, es ist für viele Leute ein echter Freund. ")
test_q(q3, "Hund")

q4 = input("Dieses Tier kann gut springen, es trägt das Baby in einem Beutel. ")
test_q(q4, "Känguru")

q5 = input("Das schnellste fliegende Tier. ")
test_q(q5, "Fledermaus")

q6 = input("Groeßtes Tier. ")
test_q(q6, "Blauwal")

#ergebnis
print("Deine Punktzahl ist " + str(points))
