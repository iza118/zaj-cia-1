def setup():
    size(900,900)
def draw():
    point(100,100)
    rectMode(CORNERS)
    rect(mouseX, mouseY, width/3*2, height/3*2)
def mouseClicked():
    clear()
    circle(100,300,400)
    
# brakuje konstrukcji warunkowej, którą również mieliśmy powtórzyć :)
# przy obecnym podejściu po pierwszym kliknięciu nie widać różnicy między następnymi kliknięciami i odkliknięciami
#1,5pkt
