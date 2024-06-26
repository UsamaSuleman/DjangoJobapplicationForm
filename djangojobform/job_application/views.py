from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


# view functions
def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            message_body = F"A nnew job appl;ication submitted{first_name}"
            email_message=EmailMessage("Form Dubmission Confirmation",message_body,to=[email])
            email_message.send()
            messages.success(request, "Submitted Sucessfully")

    return render(request, "index.html")
