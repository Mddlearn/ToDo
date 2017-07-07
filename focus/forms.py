from django import forms


class TodoForm(forms.Form):
    todo = forms.CharField(widget=forms.TextInput())
    priority = forms.IntegerField(widget=forms.TextInput())
