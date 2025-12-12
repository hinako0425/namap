from django import forms
from .models import Customer,Activity

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer #どのモデルをベースにするか
        #フォームに表示するフィールド
        fields = ('company_name','contact_name','email','phone','user','tags')

        #必須項目にしたくない場合など、個別の設定
        #(今回はuserとtagsを必須ではない設定にする)
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields=('activity_date','status','note')
        widgets={
            'activity_date':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'note':forms.Textarea(attrs={'class':'form-control','rows':2}),
        }