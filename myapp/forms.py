from django import forms
from .models import home

class AddKost(forms.ModelForm):
    class Meta:
        model = home
        fields = '__all__'

        widgets = {
        'nama' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Kost', 'required' : 'required'}),
        'harga' : forms.TextInput({'class':'form-control', 'placeholder':'Rp.', 'required' : 'required'}),
        'alamat' : forms.TextInput({'class':'form-control', 'placeholder':'Alamat Lengkap', 'required' : 'required'}),
        'coordX' : forms.TextInput({'class':'form-control', 'placeholder':'Kordinat X', 'required' : 'required'}),
        'coordY' : forms.TextInput({'class':'form-control', 'placeholder':'Kordinat Y', 'required' : 'required'}),
        'keterangan' : forms.Textarea({'class':'form-control', 'placeholder':'Keterangan', 'required' : 'required'}),
        'foto' : forms.FileInput({'class':'form-control', 'placeholder':'Foto Kost', 'required' : 'required'}),
    }