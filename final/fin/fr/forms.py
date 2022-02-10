from django import forms

class FileForm(forms.Form):
    file = forms.FileField(label="file")

class AddForm(forms.Form):
   descripcion = forms.CharField(label="desc")
   cliente = forms.CharField(label="cliente")
   nopedido = forms.IntegerField(label='No. Pedido')
   fechapedido = forms.DateField(label='fecha')

class DeleteForm(forms.Form):
    username = forms.CharField(label="Nombre")