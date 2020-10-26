from django import forms

# CADA TIPO DE CAMPO TEM UMA FERRAMENTA QUE DETERMINA COMO O CAMPO É RENDERIZADO EM HTML
class EmailFormulario(forms.Form): # FORMUÁIO CRIADO ERDANDO A CLASSE BASE Form
    nome = forms.CharField(max_length=30) # O CAMPO NOME É UM CharField. ESSE TIPO DE CAMPO É RENDERIZADO COMO UMA AREA DE INPUT DE TEXTO DE ELEMENTO HTML.
    email = forms.EmailField() # REQUER UM ENDERESSO DE EMAIL VÁLIDO, CASO COTRÁRIO O CAMPO DE VALIDAÇÃO VAI LEVANTAR UM forms.ValidationError
    para = forms.EmailField() # REQUER UM ENDERESSO DE EMAIL VÁLIDO
    comentarios = forms.CharField(required=False,
                                  widget=forms.Textarea) # required=False FAZ O CAMPO DE COMENTÁRIO OPCIONAL
