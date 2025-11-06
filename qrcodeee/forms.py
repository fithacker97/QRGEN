from django import forms

class QRCodeForm(forms.Form):
    name = forms.CharField(max_length=100 , label =' entre name'
                           , widget= forms.TextInput(attrs={'placeholder': 'Your Name',
                                                            'class': 'form-control'}))
    url = forms.URLField(label=' paste URL' , max_length=200 ,
                          widget=forms.URLInput(attrs={'placeholder': 'Your URL',
                                                        'class': 'form-control'}))
