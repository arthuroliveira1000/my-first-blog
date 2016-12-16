from django.shortcuts import render, redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil

class RegistrarUsuarioView(View):
	
	template_name = 'registrar.html'

	def get(self, request): #exibi o formulario para o usuario
		
		return render(request, self.template_name)

	def post(self, request): # faz o tratamento desses dados inseridos pelos usuários
		form = RegistrarUsuarioForm(request.POST)
		if form.is_valid():
			dados_form = form.data

			usuario = User.objects.create_user(dados_form['nome'], 
											   dados_form['email'], 
											   dados_form['senha'])

			perfil = Perfil(nome=dados_form['nome'],
							email=dados_form['email'], 
							telefone=dados_form['telefone'],
							nome_empresa=dados_form['nome_empresa'],
							usuario=usuario)
			print('chego aqui!')
			perfil.save()
			return redirect('index')
		print('form não é valido!')
		return render(request, self.template_name, {'form':form})




		
		
