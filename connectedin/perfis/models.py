from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

	nome = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)
	contatos = models.ManyToManyField('self') #self pq ele pode ter uma lista de outros perfis nesse campo
	usuario = models.OneToOneField(User, related_name="perfil")

	@property 
	def email(self):
		return self.usuario.email
		#como a classe do django User já tem um e-mail, não precisa criar outro, tem q dizer que 
		#o email que está sendo usado é o do usuario

	def convidar(self, perfil_convidado):
		#self vai pegar o proprio objeto que chamou esse metodo 
		convite = Convite(solicitante = self, convidado = perfil_convidado).save()



	"""Quando a classe já herda a classe Model de models, ela já tem acesso
	ao metodo __init__ que é tipo um construtor
	def __init__(self, nome='', email='', telefone='', nome_empresa=''):
		self.nome = nome
		self.email = email
		self.telefone = telefone
		self.nome_empresa = nome_empresa
	"""

		
class Convite(models.Model):
	
	solicitante = models.ForeignKey(Perfil, related_name='convites_feitos') 
	convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')
	'''
	no banco vai ser uma chave estrangeira com o id do perfil
	mas aqui vai ser um objeto perfil

	----------------

	o related_name cria uma variavel na classe que esta sendo relacionada
	para ter um relacionamento bidirecional, então é só fazer perfil.convites_feitos
	e retornará todos os convites que determinado usuário fez 
	'''
	def aceitar(self): #pega o convite que tá chamando o metodo
		self.convidado.contatos.add(self.solicitante) 
		#pega o convidado desse convite, no caso um objeto perfil, e adiciona o perfil do solicitante na lista 
		#lista de contatos do perfil do convidado e em baixo é a mesma coisa, só que o convidado é adicionado
		#na lista do solicitante
		self.solicitante.contatos.add(self.convidado)
		self.delete()

