from django.shortcuts import render
from PIL import Image
from .models import Products
from user.models import Register,Purchase
from django.core.files import File

# Create your views here.
def alogin(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            paw = request.POST.get('paw')
            if email =='admin11@gmail.com' and paw=='admin11':
                return render(request,'a_home.html')
            else:
                return render(request,'a_login.html')

        except Exception as e:
            print("Exception is:", e)
            return render(request, 'a_login.html')

    else:
        return render(request, 'a_login.html')


def addproducts(request):
    if request.method == 'POST':
        try:
            pname = request.POST.get('pname')
            pcat = request.POST.get('pcat')
            pcost = request.POST.get('pcost')
            pquality = request.POST.get('pquality')
            pdec = request.POST.get('pdec')
            pimage = request.FILES['pimage']
            print(pimage)
            data = Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage,
            )
            data.save()
            return render(request, 'a_viewproducts.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request, 'a_addproducts.html')
    else:
        return render(request, 'a_addproducts.html')


def viewproducts(request):
    data = Products.objects.all()
    return render(request, 'a_viewproducts.html', {'viewproduct': data})


def apurchase(request):
    uid = request.session['userid']
    cdata = Register.objects.get(email=uid)
    cid = cdata.id
    data = Purchase.objects.all()
    return render(request, 'a_purchase.html', {'data': data})


def alogout(request):
    return render(request, 'index.html')





def ahome(request):
    return render(request, 'a_home.html')