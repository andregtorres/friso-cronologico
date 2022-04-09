from PIL import Image, ImageDraw, ImageFont
from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from funcoes import *

margemx , margemy =5,0
scale=2
l_max=1
h=28*scale
legenday=2*h*scale

l_sec = 1000*scale
l_dec = l_sec/10
l_ano = l_sec/100
n_linhas=50
fontsize=15*scale
font = ImageFont.truetype("DroidSans.ttf", fontsize)

cores = (("#FFE5CC","#FFCC99","#FFB266"),("#FFFFCC","#FFFF99","#FFFF66"),("#E5FFCC","#CCFF99","#B2FF66"))

palete= [["#FF0000","#FF9999","#000000"],["#FF0000","#FF9999","#FFFFFF"],
["#FF00EE","#FF7DF6","#000000"],["#FF00EE","#FF7DF6","#FFFFFF"],
["#7B00FF","#BD80FF","#000000"],["#7B00FF","#BD80FF","#FFFFFF"],
["#0004FF","#7D7FFF","#000000"],["#0004FF","#7D7FFF","#FFFFFF"],
["#0077FF","#85BEFF","#000000"],["#0077FF","#85BEFF","#FFFFFF"],
["#10BF00","#7AFF6E","#000000"],["#10BF00","#7AFF6E","#FFFFFF"],
["#FFF700","#FFFA66","#000000"],["#FFF700","#FFFA66","#FFFFFF"],
["#FF8800","#FFC685","#000000"],["#FF8800","#FFC685","#FFFFFF"]]


def romano(n):
    if n==1:
        return "I"
    if n==2:
        return "II"
    if n==3:
        return "III"
    if n==4:
        return "IV"
    if n==5:
        return "V"
    if n==6:
        return "VI"
    if n==7:
        return "VII"
    if n==8:
        return "VIII"
    if n==9:
        return "IX"
    if n==10:
        return "X"
    if n==11:
        return "XI"
    if n==12:
        return "XII"
    if n==13:
        return "XIII"
    if n==14:
        return "XIV"
    if n==15:
        return "XV"
    if n==16:
        return "XVI"
    if n==17:
        return "XVII"
    if n==18:
        return "XVIII"
    if n==19:
        return "XIX"
    if n==20:
        return "XX"
    if n==21:
        return "XXI"
def rectangulo (x,y,dx,dy, cor,cor_out):
    draw.rectangle((x,y,x+dx-1, y+dy-1),cor,outline=cor_out)
def rectangulot (x,y,dx,dy,cor,cor_out,texto,alinhamentox,alinhamentoy, cort):
    #alinhamento: -1       0       1
    toleranciax,toleranciay=5*scale,1*scale
    rectangulo(x,y,dx,dy,cor,cor_out)
    tx,ty=draw.textsize(texto,font)
    draw.text((x+dx/2*((1*alinhamentox)+1) -(tx/2)*((1*alinhamentox)+1) -toleranciax*alinhamentox ,y+(dy/2)*((1*alinhamentoy+1))-(fontsize/1.8)*((1*alinhamentoy+1))-toleranciay*(alinhamentoy)),texto,cort,font)
def escala (offsetx,offsety):
    for i in range(0, n_sec):
        x,y = i*l_sec+offsetx , +offsety
        rectangulot(x,y,l_sec, h,cores[i%2][2],None,repr(sec1-1+i)+"00" + "   sec."+romano(sec1+i),0,0,"Black")
        for j in range(0, 10):
            xx , yy = x + j*l_dec , y + h
            rectangulot(xx,yy,l_dec,h,cores[i%2][j%2],None,repr(j)+"0",0,0,"Black")
            rectangulo(xx,yy+h,l_dec,(n_linhas+1)*h,cores[i%2][j%2],None)
            for k in range(0, 10):
                tx,ty=draw.textsize("0",font)
                xxx,yyy=xx+k*l_ano,yy+h
                draw.text((xxx-tx/2,yyy+h/2-(fontsize/1.8)),repr(k),"Black",font)
    draw.line((offsetx,offsety+2*h-1,offsetx+n_sec*l_sec,offsety+2*h),fill="Black",width=1*scale)
    draw.line((offsetx,offsety+3*h-1,offsetx+n_sec*l_sec,offsety+3*h-scale),fill="Black",width=1*scale)
def escalainv(offsetx,offsety):
    l_dec = l_sec/10
    l_ano = l_sec/100
    for i in range(0, n_sec):
        x,y = i*l_sec+offsetx , 3*h+offsety
        rectangulot(x,y,l_sec, -h,cores[i%2][2], None,repr(sec1-1+i)+"00" + "   sec."+romano(sec1+i),0,0,"Black")
        for j in range(0, 10):
            xx , yy = x + j*l_dec , y - h
            rectangulot(xx,yy,l_dec,-h,cores[i%2][j%2],None,repr(j)+"0",0,0,"Black")
            rectangulo(xx,yy-h,l_dec,-h,cores[i%2][j%2],None)
            for k in range(0, 10):
                tx,ty=draw.textsize("0")
                xxx,yyy=xx+k*l_ano,yy-2*h
                draw.text((xxx-2*tx,yyy+h/2-(fontsize/1.8)),repr(k),"Black", font)
    draw.line((offsetx,offsety+h,offsetx+n_sec*l_sec,offsety+h),fill="Black",width=1*scale)
    draw.line((offsetx,offsety,offsetx+n_sec*l_sec,offsety),fill="Black",width=1*scale)
def base(offsetx,offsety):
    escala(margemx,margemy)
    escalainv(margemx,margemy+(n_linhas+3)*h)
def bloco(linha,n,m,split,nome,cor):
    b=scale
    if linha>n_linhas or linha < 1:
        print("ERRO 01 - Linha invalida para " + nome)
    if n<100*(sec1-1) or m> 100*((sec1+n_sec)-1):
        print("ERRO 02 - Intervalo de anos invalido para " + nome)
    alinhamentoy=0
    x,y=(n-100*(sec1-1))*l_ano+margemx,(3+linha-1)*h+margemy-b
    dx,dy=(m-n)*l_ano,h
    if draw.textsize(nome)[0]>dx: alinhamentoy=1
    rectangulo(x,y,dx,dy+b,"Black",None)
    if split != None:
        dxlinha=(split-n)*l_ano
        rectangulo(x+b,y+b,dx-(2*b),dy-(b),cor[0],None)
        rectangulot(x+b,y+b,dxlinha-(2*b),dy-(b),cor[1],None,nome,-1,alinhamentoy, cor[2])
    else:
        rectangulot(x+b,y+b,dx-(2*b),dy-(b),cor[0],None,nome,-1,alinhamentoy, cor[2])   
def legenda(tabela):
    draw.text((margemx,height-legenday+h/4),"Legenda:","Black",font)
    for elemento in tabela:
        cor=palete[elemento[1]]
        texto=elemento[0].nome
        x,y=margemx+ 170*scale*(tabela.index(elemento)), height-legenday +h
        dx,dy=150*scale,h
        dxlinha=60*scale
        b=scale
        draw.rectangle((x+b,y+b,x+b+dx-(2*b),y+b+dy-(b)),cor[0],None)
        toleranciax,toleranciay=5*scale,1*scale
        tx,ty=draw.textsize(texto,font)
        alinhamentox=-1
        alinhamentoy=0
        draw.rectangle((x+b,y+b,x+b+dxlinha-(2*b),y+b+dy-(b)),cor[1],None)
        draw.text((x+b+dx/2*((1*alinhamentox)+1) -(tx/2)*((1*alinhamentox)+1) -toleranciax*alinhamentox ,y+b+(dy/2)*((1*alinhamentoy+1))-(fontsize/1.8)*((1*alinhamentoy+1))-toleranciay*(alinhamentoy)),texto, cor[2],font)
def linhomatic(tipo,lista_cat,lista_eventos):
    while True:
        print ("Linhas de interface exlusivas?")
        print("1 - Sim")
        print("2 - Nao")
        menu=input(">>>")
        if menu=="1":
            interface=1
            break
        if menu=="2":
            interface=0
            break
    tab_blocos=[]
    l_min=1
    l_top=40
    if tipo == "c":
        for cat in lista_cat:
            for evento in lista_eventos:
                if evento.categoria==cat:
                    #print (evento)
                    #print (l_max)
                    linha=procura_linha(evento.n,evento.m,l_min,l_top)
                    colore=atribuicao_cores3(evento,tab_cores)
                    #print ("Linha: ",linha,"\t Cor:", colore)
                    tab_blocos.append([linha,evento.n,evento.m,evento.split,evento.nome,palete[colore]])
            l_min=l_max+interface
    if tipo == "n":
        for cat in lista_cat:
            for evento in lista_eventos:
                if evento.nacionalidade==cat:
                    #print (evento)
                    #print (l_max)
                    linha=procura_linha(evento.n,evento.m,l_min,l_top)
                    colore=atribuicao_cores3(evento,tab_cores)
                    #print ("Linha: ",linha,"\t Cor:", colore)
                    tab_blocos.append([linha,evento.n,evento.m,evento.split,evento.nome,palete[colore]])
            l_min=l_max+interface
    if tipo == 0:
        for evento in lista_eventos:
            #print (evento)
            #print (l_max)
            linha=procura_linha(evento.n,evento.m,l_min,l_top)
            colore=atribuicao_cores3(evento,tab_cores)
            #print ("Linha: ",linha,"\t Cor:", colore)
            tab_blocos.append([linha,evento.n,evento.m,evento.split,evento.nome,palete[colore]])

    return tab_blocos
def procura_linha(n,m,li,lf):
    xi,xf=n-(sec1-1)*100,m-(sec1-1)*100
    global l_max
    global alocamento
    for i in range (li-1,lf-1):
        check=0
        for j in range(xi,xf):
            if alocamento[i][j]== True:
                check=check+1
        if check==m-n:
            for j in range(xi,xf):
                alocamento[i][j]=False
            l=i+1
            if l>l_max:
                l_max=l
            return l
def atribuicao_cores2(lista):
    tabela=[]
    while True:
        print ("Cores por Categoria (1) ou Nacionalidade (2)? Defeito (3)")
        user=input(">>> ")
        if user == "1":
            y=[]
            gerar_palete()
            for x in lista:
                if x.categoria not in y:
                    y.append(x.categoria)
            break
        if user=="2":
            y=[]
            gerar_palete()
            for x in lista:
                if x.nacionalidade not in y:
                    y.append(x.nacionalidade)
            break
        if user=="3":
            y=[]
            for x in lista:
                if x.categoria not in y:
                    y.append(x.categoria)
            for yy in y:
                j=(yy.id*2+len(palete)-2) % (len(palete))
                tabela.append([yy,j])
            return tabela, user   
        else:
            print ("Entrada invalida")
    for yy in y:
        i=int(input(yy.nome+" - Cor: "))
        tabela.append([yy,i])
    return tabela, user
def atribuicao_cores3(evento,tabela_user):
    tabela=tabela_user[0]
    user=tabela_user[1]
    if user == "1": 
        y=session.query(Categoria).all()
        for yy in y:
            if evento.categoria==yy:
                for x in tabela:
                    if x[0]==yy:
                        return x[1]
    if user=="2":
        y=session.query(Nacionalidade).all()
        for yy in y:
            if evento.nacionalidade==yy:
                for x in tabela:
                    if x[0]==yy:
                        return x[1]
    if user=="3":
        y=session.query(Categoria).all()
        for yy in y:
            if evento.categoria==yy:
                for x in tabela:
                    if x[0]==yy:
                        return x[1]      
def gerar_palete():
    scale=1
    fontsize=15*scale
    font = ImageFont.truetype("DroidSans.ttf", fontsize)
    l=len(palete)
    margem =7*scale
    h2=20*scale
    gap=4*scale
    width2, height2 = 2*margem+ 150*scale, ((l*h2)+(l-1)*gap)*scale+2*margem
    img2 = Image.new( 'RGB', (width2,height2), "white")
    draw2 = ImageDraw.Draw(img2)
    for cor in palete:
        x,y=margem,(palete.index(cor))*(h2+gap)+margem
        dx,dy=150*scale,h2
        dxlinha=60*scale
        b=scale
        draw2.rectangle((x+b,y+b,x+b+dx-(2*b),y+b+dy-(b)),cor[0],None)
        toleranciax,toleranciay=5*scale,1*scale
        #rectangulo(x+b,y+b,dxlinha-(2*b),dy-(b),cor[1],None)
        texto="Cor "+str(palete.index(cor))
        tx,ty=draw2.textsize(texto,font)
        alinhamentox=-1
        alinhamentoy=0
        draw2.rectangle((x+b,y+b,x+b+dxlinha-(2*b),y+b+dy-(b)),cor[1],None)
        draw2.text((x+b+dx/2*((1*alinhamentox)+1) -(tx/2)*((1*alinhamentox)+1) -toleranciax*alinhamentox ,y+b+(dy/2)*((1*alinhamentoy+1))-(fontsize/1.8)*((1*alinhamentoy+1))-toleranciay*(alinhamentoy)),texto, cor[2],font)
        #rectangulot(x+b,y+b,dxlinha-(2*b),dy-(b),cor[1],None,texto,-1,0, cor[2])

    img2.show()
def selecionador_eventos():
    lista=[]
    while True:
        print ("Selecionar")
        print("1 - Tudo")
        print("2 - Metodo aditivo")
        print("3 - Metodo subtrativo")
        print("l - Limpar seleçao")
        print("s - Guardar lista")
        menu=input(">>>")
        if menu == "1":
            lista=session.query(Evento).all()
            print ("Todos os eventos selecionados")
        elif menu== "2":
            while True:
                print ("Adicionar por")
                print("1 - Eventos")
                print("2 - Categorias")
                print("3 - Nacionalidades")
                print("4 - Tags")
                print("\\ - Voltar")
                menu2=input(">>>")
                if menu2 =="\\":
                    break
                elif menu2 =="1":
                    while True:
                        print ("Organizar por")
                        print("1 - Categorias")
                        print("2 - Nacionalidades")
                        print("\\ - Voltar")
                        menu3=input(">>>")
                        if menu3 =="\\":
                            break
                        elif menu3 =="1":
                            x=session.query(Categoria).all()
                            for y in x:
                                print(y)
                                for z in y.eventos:
                                    print (z.id, z.nome)
                            x=input_list()
                            for y in x:
                                if session.query(Evento).filter_by(id=y).first() != None:
                                    z=session.query(Evento).filter_by(id=y).first()
                                    lista.append(z)
                                    print ("Evento ",z," adicionado com sucesso")
                                else:
                                    print ("W: Evento id: ",y," nao existe")
                        elif menu3 =="2":
                            x=session.query(Nacionalidade).all()
                            for y in x:
                                print(y)
                                for z in y.eventos:
                                    print (z.id, z.nome)
                            x=input_list()
                            for y in x:
                                if session.query(Evento).filter_by(id=y).first() != None:
                                    z=session.query(Evento).filter_by(id=y).first()
                                    lista.append(z)
                                    print ("Evento ",z," adicionado com sucesso")
                                else:
                                    print ("W: Evento id: ",y," nao existe")
                elif menu2 =="2":
                    list_categorias()
                    x=input_list()
                    for y in x:
                        if session.query(Categoria).filter(Categoria.id == y).first() != None:
                            cat=session.query(Categoria).filter(Categoria.id == y).one()
                            eventos=session.query(Evento).filter_by(categoria=cat).all()
                            lista=list(set(lista+eventos))
                            print ("Eventos com Nacionalidade ",cat," adicionados com sucesso")
                        else:
                            print ("W - elemento",y,"nao existe")
                elif menu2 =="3":
                    list_nacionalidades()
                    x=input_list()
                    for y in x:
                        if session.query(Nacionalidade).filter(Nacionalidade.id == y).first() != None:
                            nac=session.query(Nacionalidade).filter(Nacionalidade.id == y).one()
                            eventos=session.query(Evento).filter_by(nacionalidade=nac).all()
                            lista=list(set(lista+eventos))
                            print ("Eventos com Nacionalidade ",nac," adicionados com sucesso")
                        else:
                            print ("W - elemento",y,"nao existe")
                elif menu2 =="4":
                    list_tags()
                    x=input_list()
                    for y in x:
                        if session.query(Tag).filter(Tag.id == y).first() != None:
                            t=session.query(Tag).filter(Tag.id == y).one()
                            eventos=t.evento
                            lista=list(set(lista+eventos))
                            print ("Eventos com Tag ",t," adicionados com sucesso")
                        else:
                            print ("W - elemento",y,"nao existe")
        elif menu== "3":
            while True:
                print ("Retirar da lista por")
                print("1 - Evento")
                print("2 - Categorias")
                print("3 - Nacionalidades")
                print("4 - Tags")
                print("\\")
                menu2=input(">>>")
                if menu2 =="\\":
                    break
                elif menu2 =="1":
                    while True:
                        print ("Organizar por")
                        print("1 - Categorias")
                        print("2 - Nacionalidades")
                        print("\\ - Voltar")
                        menu3=input(">>>")
                        if menu3 =="\\":
                            break
                        elif menu3 =="1":
                            x=session.query(Categoria).all()
                            for y in x:
                                print(y)
                                for z in y.eventos:
                                    if z in lista:
                                        print (z.id, z.nome)
                            x=input_list()
                            for y in x:
                                if session.query(Evento).filter_by(id=y).first() != None:
                                    z=session.query(Evento).filter_by(id=y).first()
                                    if z in lista:
                                        lista.remove(z)
                                    print ("Evento ",z," removidos com sucesso")
                                else:
                                    print ("W: Evento id: ",y," nao existe")
                        elif menu3 =="2":
                            x=session.query(Nacionalidade).all()
                            for y in x:
                                print(y)
                                for z in y.eventos:
                                    if z in lista:
                                        print (z.id, z.nome)
                            x=input_list()
                            for y in x:
                                if session.query(Evento).filter_by(id=y).first() != None:
                                    z=session.query(Evento).filter_by(id=y).first()
                                    if z in lista:
                                        lista.remove(z)
                                    print ("Evento ",z," removidos com sucesso")
                                else:
                                    print ("W: Evento id: ",y," nao existe")

                elif menu2 =="2":
                    list_categorias()
                    x=input_list()
                    for y in x:
                        if session.query(Categoria).filter(Categoria.id == y).first() != None:
                            cat=session.query(Categoria).filter(Categoria.id == y).one()
                            lista[:] = [i for i in lista if not i.categoria==cat]
                            print ("Eventos com Categoria ",cat," removidos com sucesso")
                        else:
                            print ("W - elemento",y,"nao existe")
                elif menu2 =="3":
                    list_nacionalidades()
                    x=input_list()
                    for y in x:
                        if session.query(Nacionalidade).filter(Nacionalidade.id == y).first() != None:
                            nac=session.query(Nacionalidade).filter(Nacionalidade.id == y).one()
                            lista[:] = [i for i in lista if not i.nacionalidade==nac]
                            print ("Eventos com Nacionalidade ",nac," removidos com sucesso")
                        else:
                            print ("W - elemento",y,"nao existe")
                elif menu2 =="4":
                    list_tags()
                    x=input_list()
                    for y in x:
                        if session.query(Tag).filter(Tag.id == y).first() != None:
                            t=session.query(Tag).filter(Tag.id == y).one()
                            lista[:] = [i for i in lista if i not in t.evento]
                            print ("Eventos com Tag ",t," removidos com sucesso")
                        else:
                            print ("W - elemento",y,"nao existe")
        elif menu=="s":
            break
        elif menu=="l":
            lista=[]

    return lista
def ordenar(lista_eventos):
    while True:
        print ("Ordenar")
        print("1 - Por Categoria")
        print("2 - Por Nacionalidade")
        print("3 - Nao Ordenar")
        menu=input(">>>")
        if menu == "1":
            cats=[]
            for ev in lista_eventos:
                if ev.categoria not in cats:
                    cats.append(ev.categoria)
            i=1
            for cat  in cats:
                print (i,cat.nome)
                i=i+1
            while True:
                ordem=input_list()
                if ordem =="\\": return ("c", cats)
                if len(ordem)==len(cats):
                    ordenada=[]
                    for i in range(len(ordem)):
                        ordenada.append(cats[ordem[i]-1])
                    return ("c",ordenada)
        if menu == "2":
            cats=[]
            for ev in lista_eventos:
                if ev.nacionalidade not in cats:
                    cats.append(ev.nacionalidade)
            i=1
            for cat  in cats:
                print (i,cat.nome)
                i=i+1
            while True:
                ordem=input_list()
                if ordem =="\\": return ("n", cats)
                if len(ordem)==len(cats):
                    ordenada=[]
                    for i in range(len(ordem)):
                        ordenada.append(cats[ordem[i]-1])
                    return ("n",ordenada)
        if menu == "3":
            return (0,0)

lista_eventos=selecionador_eventos()

sec1=21
secf=0
for evento in lista_eventos:
    if evento.n<(sec1-1)*100:
        sec1=(evento.n//100)+1
    if evento.m>(secf-1)*100:
        secf=(evento.m//100)+1

n_sec=secf-sec1+1


alocamento = [[True for i in range(n_sec*100)] for j in range(40)]
tab_cores=atribuicao_cores2(lista_eventos)
tipo , pois=ordenar(lista_eventos)
tab_blocos=linhomatic(tipo, pois, lista_eventos)

n_linhas=l_max
width, height = l_sec*n_sec + margemx*2 , (6+n_linhas)*h + margemy*2 + legenday
output = "friso.png"

img = Image.new( 'RGB', (width,height), "white") 

draw = ImageDraw.Draw(img)

legenda(tab_cores[0])
base(margemx,margemy)
for x in tab_blocos:
    bloco(x[0],x[1],x[2],x[3],x[4],x[5])

#img.show()
img.save(output)
