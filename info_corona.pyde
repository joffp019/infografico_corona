from __future__ import unicode_literals

from processing.data import Table

add_library('VideoExport')

ultimarow = 0

gravando = True

comtexto = True

x = 100

#corona Bolsonaro

def setup():
    
    frameRate(10)
    
    global video_export
    video_export = VideoExport(this, 'infocorona.mp4')
    
    video_export.setQuality(90, 0)
  
    video_export.setFrameRate(20)
    
    video_export.startMovie()
    
    global font5
    font5 = loadFont('publicsans_lightitalic.vlw')
    
    global font4
    font4 = loadFont('publicsans_semibolditalic.vlw')
    
    global font3
    font3 = loadFont('oswald_semibold.vlw')
    
    global font2
    font2 = loadFont('publicsans_semibold.vlw')
    
    global font1
    font1 = loadFont('oswald_semibold.vlw')
    
    global table
    table = loadTable('infocorona.csv', 'header')
        
    # global fala
    # fala = ''
        
    # botar a foto 
        
    size(1200,750)
    background(0,0,0)
    
    fill(120)
    noStroke()
    rect(0,0,400,750)
    
    global var
    var = 80
    
    fill(60)
    rect(20, 120, 360, 250)
    triangle(230,300,330,300,230,400)
    
    titulo()
    
    foto = loadImage('bolsonaro.png')
    image(foto,-15,414)
    
    global icon
    icon = loadImage('icon-01.png')
    
    textAlign(LEFT)
    fill(255, 80)
    textFont(font5)
    textSize(14)
    textLeading(18)
    text('Atualizado em 8 de agosto', 20, 390, 100, 100)

def virus(v):
    global ultimarow
    fill('#F26767')
    noStroke()
    for n in range (v):
        # if n == ultimarow:
        #     fill(255)
        # else:
        #     fill('#F26767')
        x = random(402,1198)
        y = random(122,748)
        ellipse (x, y, 2, 2)
        
    
def fonte():
    fill('#F26767')
    rect(400,40,800,80)
    fill(0,0,0,90)
    textAlign(LEFT)
    textFont(font2)
    textSize(12)
    text('Fonte: Ministério da Saúde', 415, 98, 220, 200)
    # text('A partir de 08/06: Consórcio de veículos da imprensa', 416, 80, 200, 200)
    
    
def titulo():
    fill(0)
    rect(400,0,800,40)
    fill('#F26767')
    textAlign(CENTER)
    textFont(font2)
    textSize(16)
    text('Total de óbitos no Brasil causados pelo Covid-19, desde março', 800, 26)
    
def data(a):
    fill(0)
    # rect(400, 120, 800, 30)
    # fill('#F26767')
    textAlign(LEFT)
    textFont(font2)
    textSize(24)
    text(a, 415, 75)
    
def mortes(b):
    global var
    fill(0)
    textAlign(CENTER)
    textFont(font2)
    textSize(16)
    text('Mortes diárias', 800 - var, 64)
    textAlign(CENTER)
    textFont(font1)
    textSize(38)
    text(str(b), 800 - var, 105)   
    # println(b)
    
def acumulado(c):
    fill(0)
    textAlign(CENTER)
    textFont(font2)
    textSize(16)
    text('Acumulado', 800 + var, 64)
    textAlign(CENTER)
    textFont(font1)
    textSize(38)
    text(str(c), 800 + var, 105)
    
def frase(d, fonte):
    if d != '':
        fill(60)
        rect(20, 120, 360, 250)
        
        # '#FFF703' amarelo
        # '#23761C' verde

    fill('#F26767')
    textAlign(LEFT)
    textFont(fonte)
    textSize(30)
    textLeading(38)
    text(d, 40, 140, 320, 200)
    
    # \n -> quebra de linha
    
def noticia(e, fonte):
    if e != '':
        fill(120)
        rect(0, 0, 400, 120)
    fill(60)
    # println(x)
    textAlign(LEFT, BOTTOM)
    textFont(fonte)
    textSize(16)
    textLeading(20)
    text(e, 20, 25, 320, 80)
    
def acidentes(f):
    fill(0, 100)
    textAlign(RIGHT)
    textFont(font1, 30)
    text('= ' + str(f/200), 1025, 90)
    textAlign(LEFT)
    textFont(font2)
    textSize(12)
    text('acidentes aéreos (200 pessoas)', 1035, 65, 120, 160)
    global icon
    image(icon, 1140, 58)

def loadData():
    t = millis()
        
    global ultimarow
    global comtexto
        
    n = int(t/1000) # contador de "segundos"
    # print(n)
        
    row = table.getRow(int(n)) 
            
    a = row.getString('data')
    b = row.getInt('mortes')
    c = row.getInt('acumulado')
    d = row.getString('frase')
    e = row.getString('noticia')
    
    fonte()
    data(a)
    if n > ultimarow: # a cada segundo, n fica maior, superando uma integral por vez
        virus(b) # b é especificado pela row correspondente do n do momento
        ultimarow = n #transforma o decimal na integral
        print(ultimarow)
        
    mortes(b)
    acidentes(c)
    acumulado(c)
    frase(d, font3)
          
    noticia(e, font4)  
        
    if n == 148:
        noLoop()
        video_export.endMovie()
    
def draw():
    
    loadData()
    
    if gravando:
        video_export.saveFrame()
    
    
                

    
    
    
