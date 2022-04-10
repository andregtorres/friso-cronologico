from model import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from funcoes import *


def menu_novo():
	while 1:
		print ('\n---- Novo ----')
		print ("1 - Evento")
		print ("2 - Nacionalidade")
		print ("3 - Categoria")
		print ("4 - Tag")
		print ("5 - Ponto")
		print ("\ - Voltar")
		menu2 = input(">>> ")
		if menu2=="1":
			while True:
				print ("\n---- Evento ----")
				print ("\n1 - Terminal")
				print ("2 - Ficheiro")
				print ("\- Voltar")
				menu3 = input(">>> ")
				if menu3=="1":
					input_evento()
				if menu3=="2":
					ficheiro=input("Ficheiro de input: ")
					novos_ficheiro(ficheiro)
				if menu3=="\\":
					break
		if menu2=="2":
			input_nacionalidade()
		if menu2=="3":
			input_categoria()
		if menu2=="4":
			input_tag()
		if menu2=="5":
			input_ponto()
		if menu2=="\\":
			break
def menu_alterar():
	while 1:
		print ("\n---- Alterar ----")
		print ("1 - Evento")
		print ("2 - Nacionalidade")
		print ("3 - Categoria")
		print ("4 - Tag")
		print ("5 - Ponto")
		print ("\ - Voltar")
		menu2 = input(">>> ")
		if menu2=="1":
			list_eventos()
			x=input_int("id:")
			ev=session.query(Evento).filter(Evento.id == x).one()
			while 1:
				print ("\n---- Campo ----")
				print ("1 - Nome")
				print ("2 - n")
				print ("3 - m")
				print ("4 - Descricao")
				print ("5 - Split")
				print ("6 - Nacionalidade")
				print ("7 - Categoria")
				print ("8 - Tags")
				print ("9 - Pontos")
				print ("\ - Voltar")
				menu3 = input(">>> ")
				if menu3 =="1":
					ev.nome=input("Nome: ")
				if menu3 == "2":
					ev.n=input_int("n:")
				if menu3 == "3":
					ev.m=input_int("m:")
				if menu3 == "4":
					ev.description=input("Descricao:")
				if menu3 == "5":
					ev.split=input_int("Split:")
				if menu3 == "6":
					ev.nacionalidade=select_nacionalidade()
				if menu3 == "7":
					ev.categoria=select_categoria()
				if menu3 == "8":
					ev.tags= ev.tags + select_tag()
				if menu3 == "9":
					ev.pontos= ev.pontos + select_ponto()
				if menu3=="\\":
					break
		if menu2=="2":
			list_nacionalidades()
			x=input_int("id:")
			nac=session.query(Nacionalidade).filter(Nacionalidade.id == x).one()
			while 1:
				print ("\n---- Campo ----")
				print ("1 - Sigla")
				print ("2 - Nome")
				print ("\ - Voltar")
				menu3 = input(">>> ")
				if menu3 =="1":
					nac.sigla=input("Sigla: ")
				if menu3 =="2":
					nac.nome=input("Nome: ")
				if menu3=="\\":
					break
		if menu2=="3":
			list_categorias()
			x=input_int("id:")
			cat=session.query(Categoria).filter(Categoria.id == x).one()
			while 1:
				print ("\n---- Campo ----")
				print ("1 - Nome")
				print ("\ - Voltar")
				menu3 = input(">>> ")
				if menu3 =="1":
					cat.nome=input("Nome: ")
				if menu3=="\\":
					break
		if menu2=="4":
			list_tags()
			x=input_int("id:")
			tag=session.query(Tag).filter(Tag.id == x).one()
			while 1:
				print ("\n---- Campo ----")
				print ("1 - Nome")
				print ("2 - Eventos")
				print ("\ - Voltar")
				menu3 = input(">>> ")
				if menu3 =="1":
					tag.nome=input("Nome: ")
				if menu3 =="2":
					list_eventos()
					y=input_list()
					for z in y:
						if session.query(Evento).filter(Evento.id == z).first()!=None:
							ev=session.query(Evento).filter(Evento.id == z).first()
							ev.tags.append(tag)
							print ("Tag",tag,"adicionada ao evento", ev)
						else:
							print ("W: Evento id: ",z," nao existe")

				if menu3=="\\":
					break
		if menu2=="5":
			list_pontos()
			x=input_int("id:")
			p=session.query(Ponto).filter(Ponto.id == x).one()
			while 1:
				print ("\n---- Campo ----")
				print ("1 - Nome")
				print ("2 - Ano")
				print ("3 - Eventos")
				print ("\ - Voltar")
				menu3 = input(">>> ")
				if menu3 =="1":
					p.nome=input("Nome: ")
				if menu3 =="2":
					p.data=input("Ano: ")
				if menu3 =="3":
					list_eventos()
					y=input_list()
					for z in y:
						ev=session.query(Evento).filter(Evento.id == z).one()
						ev.pontos.append(p)
						print ("Ponto",p,"adicionada ao evento", ev)
				if menu3=="\\":
					break
		if menu2 == "\\":
			break
def menu_mostrar():
	while 1:
		print ("\n---- Mostrar ----")
		print ("1 - Evento")
		print ("2 - Nacionalidade")
		print ("3 - Categoria")
		print ("4 - Tag")
		print ("5 - Ponto")
		print ("6 - Tudo")
		print ("\ - Voltar")

		menu2 = input(">>> ")
		if menu2=="1":
			mostrar_eventos();
		if menu2=="2":
			list_nacionalidades();
		if menu2=="3":
			list_categorias();
		if menu2=="4":
			list_tags();
		if menu2=="5":
			list_pontos();
		if menu2=="6":
			mostrar_tudo()
		if menu2=="\\":
			break
def menu_apagar():
	while 1:
		print ("\n---- Apagar ----")
		print ("1 - Evento")
		print ("2 - Nacionalidade")
		print ("3 - Categoria")
		print ("4 - Tag")
		print ("5 - Tudo"	)
		print ("\ - Voltar")
		menu2 = input(">>> ")
		if menu2=="1":
			list_eventos()
			x=input_list()
			ev=[]
			for i in x:
				if  session.query(Evento).filter(Evento.id == i).one() != None:
					ev.append(session.query(Evento).filter(Evento.id == i).one())
				else:
					print ("W - elemento",i,"nao existe")
			if ev:
				print (ev)
				if confirmacao1()==True:
					for evv in ev:
						session.delete(evv)
		if menu2 == "2":
			list_nacionalidades()
			x=input_list()
			ev=[]
			for i in x:
				if session.query(Nacionalidade).filter(Nacionalidade.id == i).one() != None:
					ev.append(session.query(Nacionalidade).filter(Nacionalidade.id == i).one())
				else:
					print ("W - elemento",i,"nao existe")
			if ev:
				print (ev)
				if confirmacao1()==True:
					for evv in ev:
						session.delete(evv)
		if menu2 == "3":
			list_categorias()
			x=input_list()
			ev=[]
			for i in x:
				if session.query(Categoria).filter(Categoria.id == i).one() != None:
					ev.append(session.query(Categoria).filter(Categoria.id == i).one())
				else:
					print ("W - elemento",i,"nao existe")
			if ev:
				print (ev)
				if confirmacao1()==True:
					for evv in ev:
						session.delete(evv)
		if menu2 == "4":
			list_tags()
			x=input_list()
			ev=[]
			for i in x:
				if session.query(Tag).filter(Tag.id == i).one() != None:
					ev.append(session.query(Tag).filter(Tag.id == i).one())
				else:
					print ("W - elemento",i,"nao existe")
			if ev:
				print (ev)
				if confirmacao1()==True:
					for evv in ev:
						session.delete(evv)
		if menu2=="5":
			if confirmacao1()==True:
				limpa_tudo()
		if menu2 == "\\":
			break

#MENU
print ("\n ---- DB Manager - Friso Cronologico - v0.3 ----")
while 1:
	print ("\n---- MENU ----")
	print ("1 - Mostrar")
	print ("2 - Novo")
	print ("3 - Alterar")
	print ("4 - Guardar DB")
	print ("5 - Apagar")
	print ("q - Sair")

	menu1 = input(">>> ")
	if menu1=="2":
		menu_novo();
	if menu1=="1":
		menu_mostrar()
	if menu1=="3":
		menu_alterar()
	if menu1=="q":
		break
	if menu1=="4":
		session.commit()
		print ("DB saved")
	if menu1=="5":
		menu_apagar()
