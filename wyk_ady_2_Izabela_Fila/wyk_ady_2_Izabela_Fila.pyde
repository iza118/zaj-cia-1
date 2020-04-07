def setup():
    size(400,400)
    stroke(17,200,99)
    strokeWeight(3)
    global natezenie
    natezenie = 2
    global szerokosc
    szerokosc = 200
    global wysokosc
    wysokosc = 0
    global szybkoscWys
    szybkoscWys = 5
    global szybkoscSzer
    szybkoscSzer = 5

    
def draw():
    global natezenie
    
    natezenie = natezenie + 1
    if natezenie == 255: # wartość koloru nie może być większa niż 255, nie możęmy przewidzieć jak zachowa się rpogram jeżeli podamy wyższą... zachowa najwyższą możliwą/ zrobi modulo 255/wyrzuci błąd? Nawet różne  interpetery tego samego języka mogą to różnie traktować.
        natezenie = 0
    
    global szerokosc
    global wysokosc
    global szybkoscWys
    global szybkoscSzer
   
    szerokosc = szerokosc + szybkoscSzer
    if (szerokosc > width  or szerokosc < 1):
        szybkoscSzer = szybkoscSzer *-1
        
    wysokosc = wysokosc + szybkoscWys
    if (wysokosc > height  or wysokosc < 1):
        szybkoscWys = szybkoscWys *-1
        
    fill(natezenie, 200,17,99)
    circle(szerokosc, wysokosc, 50)

def mousePressed():
    exit()
    
# ładnie ponazywane zmienne
# zmiana koloru miała być z użyciem kolekcji, któe mieliście powtórzyć przy okazji tematu
# 1,25p
