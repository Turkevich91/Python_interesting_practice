from django import forms


class AddTools(forms.Form):
    machine = forms.CharField(label="Machine", max_length=100)
    tool_type = forms.CharField(label="tool type:", max_length=20)


