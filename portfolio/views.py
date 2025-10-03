from django.shortcuts import render

from .forms import ContactForm
from django.core.mail import send_mail
from projects.models import Skill




# Create your views here.
def about_me_view(request):
    skills_list = Skill.objects.all()
    context= {"skills":skills_list}
    return render(request, 'portfolio/about_me.html',context)


def experience_view(request):
    skills_list = Skill.objects.all()
    context= {"skills":skills_list}
    return render(request, 'portfolio/experience.html',context)

def contact_view(request):
    if request.method == 'POST': #means the form is not empty
        #to send the email
        form = ContactForm(request.POST)
        #collect the data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            #Build the full email
            message_body = (
                f'You have a new email from your portfolio \n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}'
            )

            # try send the email
            try:
                send_mail(
                    "Email from portfolio", #Subject
                    message_body, #message body --> the user typed
                    email, # From email: The user´s email
                    ['jparra@sdgku.edu'] # TO: Where you want to receive the email
                )
                #after sending the email
                form = ContactForm()
                return render(request, 'portfolio/contact.html',{'form':form})
            except Exception as e:
                print(f'Error sending email: {e}')

                return render(request, 'portfolio/contact.html',{'form':form})
        else:
            print("data" + name, email, message)
    else: 
        form = ContactForm()
        return render(request, 'portfolio/contact.html',{'form':form})

    



