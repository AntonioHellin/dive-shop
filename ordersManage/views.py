from ordersManage.models import Article
from ordersManage.forms import ContactForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def search_products(request):

    return render(request, "search_products.html")

def search(request):
    product = request.GET.get("prd", "").strip()

    if product:
        if len(product) > 20:
            message = "Article query is too long (maximum 20 characters)."
        else:
            articles = Article.objects.filter(name__icontains=product)
            return render(request, "result_search.html", {"articles": articles, "query": product})
    else:
        message = "You did not insert anything to search."

    return HttpResponse(message)


def contact(request):
    if request.method == "POST":
        myForm = ContactForm(request.POST)
        if myForm.is_valid():
            cleanFormData = myForm.cleaned_data
            recipient = getattr(settings, 'CONTACT_RECIPIENT_EMAIL', '') or getattr(settings, 'EMAIL_HOST_USER', '')
            if recipient:
                send_mail(
                    cleanFormData['subject'],
                    cleanFormData['email'],
                    cleanFormData.get('email', ''),
                    [recipient],
                )
            return render(request, "thanks.html")
    else:
        myForm = ContactForm()

    return render(request, "contact_form.html", {"form": myForm})