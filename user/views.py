from django.shortcuts import render,redirect
from .models import Register,Purchase
from admins.models import Products
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        try:
            cname = request.POST.get('cname')
            email = request.POST.get('email')
            paw = request.POST.get('paw')
            mno = request.POST.get('mno.')
            addr = request.POST.get('addr')
            pincode = request.POST.get('pincode')
            data = Register(
                cname=cname,
                email=email,
                paw=paw,
                mno=mno,
                addr=addr,
                pincode=pincode,
            )
            data.save()
            return render(request, 'index.html')
        except Exception as e:
            print("Exception is: ", e)
            return render(request, 'Register.html')
    else:
        return render(request, 'Register.html')


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            paw = request.POST.get('paw')
            data = Register.objects.get(email=email, paw=paw)
            request.session['userid'] = data.email
            print(data)
            return render(request, 'u_home.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'u_home.html')


def profile(request):
    try:
        uid=request.session['userid']
        print(uid)
        data=Register.objects.get(email=uid)
        return render(request,'profile.html',{'profile':[data]})
    except Exception as e:
        print("Exception is",e)
        return render(request,'u_home.html')


def products(request):
    data = Products.objects.all()
    return render(request,'u_products.html',{'product':data})


def buyproducts(request,id):
    if request.method=='POST':
        uid=request.session['userid']
        cid = Register.objects.get(email=uid)
        id1 = cid.id
        pid = request.POST.get('id')
        product =  Products.objects.get(id=id)
        data = Purchase(
            pname=product.pname,
            pcost=product.pcost,
            pquality=product.pquality,
            pdec=product.pdec,
            cid_id=id1,
            pid_id=id,

        )
        data.save()
        messages.success(request,'product purchased sucessfully.')
        return render(request,'u_products.html')
    else:
        messages.error(request,'Not purchased.')
        return redirect('products')


def upurchase(request):
    uid= request.session['userid']
    cdata=Register.objects.get(email=uid)
    cid=cdata.id
    data=Purchase.objects.filter(cid_id=cid)
    return render(request,'u_purchase.html',{'data':data})


def ulogout(request):
    return render(request,'index.html')


def uaccount(request):
    return render(request,'uaccount.html')


def contact(request):
    return render(request,'contact.html')


def furniture(request):
    return render(request,'furniture.html')


def digitalproducts(request):
    return render(request,'digi-products.html')


def clothing(request):
    return render(request,'clothing.html')


def household(request):
    return render(request,'household.html')


def inpro(request):
    return render(request, 'inpro.html')


def buy(request):
    return render(request,'buy.html')


def extra(request):
    return render(request,'extra.html')