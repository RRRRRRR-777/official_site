from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    select = forms.fields.ChoiceField(choices = (('採用について', '採用'),('質問について', '質問'),('相談について', '相談'),),
             label='お問い合わせ内容', required=True, widget=forms.widgets.RadioSelect)
    first_name = forms.CharField(label='性', max_length=100, widget=forms.TextInput(attrs={'placeholder': '例 : 山田',}))
    last_name = forms.CharField(label='名', max_length=100, widget=forms.TextInput(attrs={'placeholder': '例 : 太郎',}))
    first_ruby = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': '例 : ヤマダ',}))
    last_ruby = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': '例 : タロウ',}))
    gender = forms.select = forms.fields.ChoiceField(choices = (('男性', '男性'),('女性', '女性'),),
             label='性別', required=True, widget=forms.widgets.RadioSelect)
    age = forms.DateField(label='生年月日', help_text='カレンダーボタンを押してください', widget = forms.NumberInput(attrs={'type': 'date'}))
    sender = forms.EmailField(label='メールアドレス', help_text='※ご確認の上、正しく入力してください。', widget=forms.TextInput(attrs={'placeholder': 'aaa@bbb.com',}))
    
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_number = forms.CharField(validators=[tel_number_regex], max_length=15, label='電話番号')

    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    postal_code = forms.CharField(validators=[postal_code_regex], max_length=7, label='郵便番号')

    todouhuken = forms.CharField(label='都道府県', max_length=100)
    sikucyouson = forms.CharField(label='市区町村', max_length=100)
    bannti = forms.CharField(label='番地', max_length=100)
    heyabangou = forms.CharField(label='建物名・部屋番号', max_length=100, required=False)
    message = forms.CharField(label='お問い合わせ詳細', widget=forms.Textarea(attrs={'cols': '32', 'rows': '13'}))

