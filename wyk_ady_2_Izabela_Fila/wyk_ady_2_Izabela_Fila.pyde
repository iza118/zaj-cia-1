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
    if natezenie == 1000:
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
