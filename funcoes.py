from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///DB_Friso.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def mostrar_tudo():
	print ("\n")
	print ("Eventos:")
	print (session.query(Evento).all())
	print ("Nacionalidades:")
	print (session.query(Nacionalidade).all())
	print ("Categorias:")
	print (session.query(Categoria).all())
	print ("\n")
def list_eventos():
	lista=session.query(Evento).all()
	if lista:
		print("---- Eventos: ----")
		for x in lista:
			print ("{}\t{}".format(x.id, x))
	else:
		print ("\nNao ha nada aqui :o" )
def mostrar_eventos():
		list_eventos()
		print("Ver em detalhe?")
		print( "0 para voltar")
		y=input_int("id: ")
		if y!=0:
			print ("#"*20)
			x=session.query(Evento).filter(Evento.id == y).one()
			x.mostrar()
			print ("#"*20)
def list_nacionalidades():
	lista=session.query(Nacionalidade).all()
	for x in lista:
		print ("{}\t{}".format(x.id, x))
	if not lista:
			print ("\nNao ha nada aqui :o" )
def list_categorias():
	lista=session.query(Categoria).all()
	for x in lista:
		print ("{}\t{}".format(x.id, x))
	if not lista:
			print ("\nNao ha nada aqui :o" )
def list_tags():
	lista=session.query(Tag).all()
	for x in lista:
		print ("{}\t{}".format(x.id, x))
	if not lista:
		print ("\nNao ha nada aqui :o")
def list_pontos():
	lista=session.query(Ponto).all()
	for x in lista:
		print ("{}\t{}".format(x.id, x))
	if not lista:
			print ("\nNao ha nada aqui :o" )
def limpa_eventos():
	lista=session.query(Evento).all()
	for evento in lista:
		session.delete(evento)
def limpa_nacionalidades():
	lista=session.query(Nacionalidade).all()
	for nac in lista:
		session.delete(nac)
def limpa_categorias():
	lista=session.query(Categoria).all()
	for cat in lista:
		session.delete(cat)
def limpa_tudo():
	limpa_categorias()
	limpa_nacionalidades()
	limpa_eventos()
def confirmacao1():
	while 1:
			confirmar=input("Confirmar? (y / n)\n")
			if confirmar == "n":
				return False
			if confirmar== "y":
				return True
def confirmacao(new):
	while 1:
			confirmar=input("Confirmar? (y / n)\n")
			if confirmar == "n":
				new.delete()
				print ("Entrada descartada")
				return None
			if confirmar== "y":
				return new
def input_int(string):
	while True:
		try:
			x=int(input(string))
			return x
		except (TypeError,ValueError, NameError, SyntaxError):
			print("E: Entrada invalida")
def input_list():
	while True:
		try:
			y= input('id (forma 1, 2, 7): ').split(',')
			x=list(map(int,y))
			return x
		except (TypeError,ValueError, NameError, SyntaxError):
			print ("E - Entrada invalida")

def input_nacionalidade():
	print (" --- Nova Nacionalidade ---")
	parametros=[None] *2
	parametros[0]=input("Sigla: ")
	parametros[1]=input("Nome: ")
	print (parametros)
	confirmar=input("Confirmar? (y / n)\n")
	if confirmar != "y":
		print ("Entrada descartada")
		return None
	else:
		new=Nacionalidade(sigla= parametros[0], nome=parametros[1])
		session.add(new)
		print ("Nacionalidade",new,"criada com sucesso")
		return new
def input_nacionalidade2(sig):
	print (" --- Nova Nacionalidade ---")
	parametros=[None] *2
	parametros[0]=sig
	parametros[1]=input("Nome: ")
	print (parametros)
	if confirmacao1()==True:
		new=Nacionalidade(sigla= parametros[0], nome=parametros[1])
		session.add(new)
		print ("Nacionalidade",new,"criada com sucesso")
		return new
	else:
		return None
def input_categoria():
	print (" --- Nova Categoria ---")
	parametros=[None]
	parametros[0]=input("Nome: ")
	print (parametros)
	confirmar=input("Confirmar? (y / n)\n")
	if confirmar != "y":
		print ("Entrada descartada")
		return None
	else:
		new=Categoria(nome=parametros[0])
		session.add(new)
		session.flush()
		print ("Categoria",new,"criada com sucesso")
		return new
def input_tag():
	print (" --- Nova Tag ---")
	nome=input("Nome: ")
	print (nome)
	confirmar=input("Confirmar? (y / n)\n")
	if confirmar != "y":
		print ("Entrada descartada")
		return None
	else:
		new=Tag(nome=nome)
		session.add(new)
		print ("Tag",new,"criada com sucesso")
		return new
def input_ponto():
	print (" --- Novo Ponto ---")
	parametros=[None]*2
	parametros[0]=input("Nome: ")
	parametros[1]=input_int("Ano: ")
	print (parametros)
	confirmar=input("Confirmar? (y / n)\n")
	if confirmar != "y":
		print ("Entrada descartada")
		return None
	else:
		new=Ponto(nome=parametros[0],ano=parametros[1])
		session.add(new)
		print ("Ponto",new,"criado com sucesso")
		return new
def select_nacionalidade():
	print ("Nacionalidade:")
	list_nacionalidades()
	print ("0 para inserir nova")
	x=input_int("Nacionalidade (id): ");
	if x==0:
		return input_nacionalidade()
	else:
		return session.query(Nacionalidade).filter(Nacionalidade.id == x).one()
def select_categoria():
	print ("Categoria:")
	list_categorias()
	print ("0 para inserir nova")
	x=input_int("Categoria (id): ")
	if x==0:
		return input_categoria()
	else:
		return session.query(Categoria).filter(Categoria.id == x).one()
def select_tag():
	print ("Tags:")
	list_tags()
	print ("0 para inserir nova")
	tags=[]
	x=input_list()
	for i in x:
		if i==0:
			x.remove(i)
			while True:
				nova=input_tag()
				tags.append(nova)
				print ("Tag",nova,"adicionada com sucesso")
				print ("Adicionar outra Tag?")
				if confirmacao1()==True:
					pass
				else:
					break
		else:
			if session.query(Tag).filter(Tag.id == i).one() != None:

				tags.append(session.query(Tag).filter(Tag.id == i).one())
				print ("Tag",session.query(Tag).filter(Tag.id == i).one(),"adicionada com sucesso")
			else:
				print ("W - elemento",i,"nao existe")
	return tags
def select_ponto():
	print ("Pontos:")
	list_pontos()
	print ("0 para inserir nova")
	p=[]
	x=input_list()
	for i in x:
		if i==0:
			x.remove(i)
			while True:
				nova=input_ponto()
				p.append(nova)
				print ("Ponto",nova,"adicionado com sucesso")
				print ("Criar outro Ponto?")
				if confirmacao1()==True:
					pass
				else:
					break
		else:
			if session.query(Ponto).filter(Ponto.id == i).one() != None:
				p.append(session.query(Ponto).filter(Ponto.id == i).one())
				print ("Ponto",session.query(Ponto).filter(Ponto.id == i).one(),"adicionado com sucesso")
			else:
				print ("W - elemento",i,"nao existe"	)
	return p
def input_evento():
	parametros=[None] *3
	parametros[0]=input("nome: ")
	parametros[1]=input_int("n: ")
	parametros[2]=input_int("m: ")
	new=Evento(nome= parametros[0], n=parametros[1], m=parametros[2])
	new.nacionalidade=select_nacionalidade()
	new.categoria= select_categoria()
	print ("#"*20)
	print (new)
	print (new.nacionalidade)
	print (new.categoria)
	print ("#"*20)
	confirmacao(new)
def novos_ficheiro(fich):
	ficheiro=open(fich, "r")
	novos=[]
	for line in ficheiro:
		campo=line.strip().split(";")
		print (campo)
		novos.append(campo)
	if confirmacao1()==False:
		return False
	for evento in novos:
		#se anda nao existe
		if not session.query(Evento).filter_by(nome=evento[0]).first():
		# session.query(Evento).filter(Evento.nome.like(evento[0])).all():
			new=Evento(nome= evento[0], n=int(evento[1]), m=int(evento[2]))
			print (session.query(Nacionalidade).filter_by(sigla=evento[3]).first())
			if not session.query(Nacionalidade).filter_by(sigla=evento[3]).first():
				print ("Nacionalidade:",evento[3],"nao existe. Criar?")
				if confirmacao1()==True:
					nac=input_nacionalidade2(evento[3])
					new.nacionalidade=nac
			else:
				new.nacionalidade=session.query(Nacionalidade).filter_by(sigla=evento[3]).first()
			if not session.query(Categoria).filter_by(nome=evento[4]).first():
				print ("Categoria:",evento[4],"nao existe. Criar?")
				if confirmacao1()==True:
					cat=Categoria(nome=evento[4])
					new.categoria=cat
			else:
				new.categoria=session.query(Categoria).filter_by(nome=evento[4]).first()
			#tags
			if len(evento)>5:
				if not session.query(Tag).filter_by(nome=evento[5]).first():
					print ("Tag:",evento[5],"nao existe. Criar?")
					if confirmacao1()==True:
						tag=Tag(nome=evento[5])
						new.tags.append(tag)
				else:
					tag=session.query(Tag).filter_by(nome=evento[5]).first()
					new.tags.append(tag)
			session.add(new)
			print("{} adicionado com sucesso".format(new))
		else:
			print ("Evento",evento[0],"ja existente, ignorado")
	ficheiro.close()
