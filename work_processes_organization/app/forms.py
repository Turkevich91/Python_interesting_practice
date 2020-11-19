from django import forms
from django.forms import ModelForm
import json
# from work_processes_organization.common.NestParser import Nest
from .models import Task


# nest = Nest().parse_striker_report
# print(json.dumps(nest.__dict__, indent=3))


# class NestApplier(forms.Form):
#     nest = Nest().parse_striker_report
#     name = nest.kit_name


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['release', 'loose_items', 'outsource_paint', 'zee_hats_angels']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
