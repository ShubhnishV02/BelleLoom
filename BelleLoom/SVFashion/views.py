from django.shortcuts import redirect, render
from ShopByNewCollection.models import ShopByNewCollection

# "*" takes all the models name which is inside the store model
from store.models import *

from django.contrib import messages
from django.http import JsonResponse


def Homepage(request):
    newcollectiondata = ShopByNewCollection.objects.all()
    categorydata = Category.objects.filter(status=0)
    productsdata = Products.objects.all()
    data = {'title' : 'RAFashion | HomePage',
        "newcollectiondata" : newcollectiondata,
        "categorydata" : categorydata,
        "productsdata": productsdata,
       }
    return render(request, "index.html" , data)

def Categoryy(request):
    categorydata = Category.objects.filter(status=0)
    data = {
        'categorydata' : categorydata
    }
    return render(request, "CategoryPRODUCTS.html", data)

def categoryView(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        productsdata = Products.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        data = {"productsdata": productsdata,
                "category_name" : category_name}
        return render(request, "CategoryPRODUCTS.html", data)
    else:
        messages.warning(request, "no such category found")
        return redirect("")


def SINGLEPRODUCT(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Products.objects.filter(slug=prod_slug, status=0)):
            productsdata = Products.objects.filter(slug=prod_slug, status=0).first()
            data = {
                "productsdata" : productsdata
            }
            return render(request,"SinglePRODUCT.html", data)
        
        else:
            messages.error(request, "No such Product found")
            return redirect("/")
        
    else:
        messages.error(request, "No such Category found")
        return redirect("/")
    
    

def ABOUTUS(request):
    return render(request, "AboutUS.html")

def CONTACTUS(request):
    return render(request, "CONTACTus.html")

def TESTIMONIALS(request):
    return render(request, "Testimonials.html")

def PRIVACYPOLICY(request):
    return render(request, "privacypolicy.html")

def TERMSANDCONDITIONS(request):
    return render(request, "termsANDconditions.html")

def FAQS(request):
    return render(request, "FAQs.html")


def check_delivery_area(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode', '')
        try:
            area = DeliveryArea.objects.get(pincode=pincode)
            response_data = {
                'delivery_available': True,
                'cod_available': area.cod_available,
            }
        except DeliveryArea.DoesNotExist:
            response_data = {
                'delivery_available': False,
            }
        return JsonResponse(response_data)
    return render(request, 'your_template.html')