from django.shortcuts import redirect, render
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


def index(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            select = form.cleaned_data['select']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            first_ruby = form.cleaned_data['first_ruby']
            last_ruby = form.cleaned_data['last_ruby']
            gender = form.cleaned_data['gender']
            age = str(form.cleaned_data['age'])
            sender = form.cleaned_data['sender']
            tel_number = form.cleaned_data['tel_number']
            postal_code = form.cleaned_data['postal_code']
            todouhuken = form.cleaned_data['todouhuken']
            sikucyouson = form.cleaned_data['sikucyouson']
            bannti = form.cleaned_data['bannti']
            heyabangou = form.cleaned_data['heyabangou']
            message = form.cleaned_data['message']
            recipients = [settings.EMAIL_HOST_USER]

            subject = '有限会社和泉電設_'+ select +'に関するメール'
            message = '「お問い合わせメール」'+'\n'+'お問い合わせ内容 : '+ select +'\n'+'名前 : '+ first_name +' '+ last_name +'\n'+'ふりがな : '+ first_ruby +' '+ last_ruby +'\n'+'性別 : '+ gender +'\n'+'生年月日 : '+ age +'\n'+'メールアドレス : '+ sender +'\n'+'電話番号 : '+ tel_number +'\n'+'郵便番号 : '+ postal_code +'\n'+'住所 : '+ todouhuken + sikucyouson + bannti + heyabangou +'\n'+'お問い合わせ詳細 : '+ message

            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('app:index')

    else:
        form = ContactForm()


    return render(request, 'app/base.html', {'form': form})