from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post #modelo deveria ser usado para criar este formulário
		fields = ('title', 'text',)
		
			
	
		