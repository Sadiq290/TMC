from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models

class Problem(forms.ModelForm):
    class Meta:
        model = models.Problem
        fields = "__all__"
        exclude = ('first_solve','problem_maker')
        labels = {
            'problem_name': 'Problem Name',
            'problem': 'Problem',
            'answer': 'Answer',
            'problem_hardness': 'Problem Hardness',
            'problem_cat': 'Problem Category',
            'point': 'Problem Point',
        }
        widgets = {
            'problem_name': forms.TextInput(attrs={'class':'form-control',}),
            'problem': forms.Textarea(attrs={'class':'form-control',}),
            'answer': forms.NumberInput(attrs={'class':'form-control',}),
            'point': forms.NumberInput(attrs={'class':'form-control'}) 
        }

class ClubMember(forms.ModelForm):
    class Meta:
        model = models.ClubMember
        fields = "__all__"
        labels = {
            'name' : 'Name',
            'dept' : 'Department',
            'post' : 'Post',
            'image' : 'Image'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'dept' : forms.TextInput(attrs={'class':'form-control'}),
            'post' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control'})
        }

