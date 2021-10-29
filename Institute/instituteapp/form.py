from django import forms

class registerform(forms.Form):
    username=forms.CharField(label="Username :" ,widget=forms.TextInput(attrs={'class':'form-control',
                                                                               'placeholder':'username'}))



    email=forms.CharField(label='Email-Id',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))


    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    confirmPassword =forms.CharField(label='confirm password.',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'conform password'}))
