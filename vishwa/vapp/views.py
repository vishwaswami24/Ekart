from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from vapp.models import Product,Cart,Order,OrderHistory,UserInfo
from django.db.models import Q      #Q object encapsulates a SQL expression in a Python object that can be used in database-related operations
import random
import razorpay
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
# Create your views here.

 
def products(request):
    p=Product.objects.filter(is_active=True)
    context={}
    context['data']=p
    return render(request,'index.html',context)

def contact(request):
    context={}
    u=User.objects.filter(id=request.user.id)
    context['data']=u
    return render(request,'contact.html',context)

def about(request):
    context={}
    u=User.objects.filter(id=request.user.id)
    context['data']=u 
    return render(request,'about.html',context)

def prodetails(request):
    context={}
    u=User.objects.filter(id=request.user.id)
    context['data']=u
    return render(request,'product_details.html',context)

def register(request):
    context={}
    if request.method == "GET":
        return render(request,'register.html')
    else:
        f=request.POST['ufname']
        l=request.POST['ulname']
        n=request.POST['uemail']
        p=request.POST['upass']
        cp=request.POST['ucpass']

        if  f=='' or l=='' or n=='' or p=='' or cp=='':
            context['errmsg']="Fields cannot be empty!!"
            return render(request,'register.html',context)
        elif p!=cp:
            context['errmsg']="Password and Confirm Password didn't matched."
            return render(request,'register.html',context)
        elif len(p)<8:
            context['errmsg']="Password must be at least 8 characters"
            return render(request,'register.html',context)
        else:
            try:
                u=User.objects.create(username=n,email=n,first_name=f,last_name=l)
                u.set_password(p)
                u.save()
                context['success']="User Created Successfully!"
                return render(request,'register.html',context)
            except Exception:
                context['errmsg']="User with same Username already exists.\nPlease Login."
                return render(request,'register.html',context)

# user django built-in framework functions
def user_login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        name=request.POST['uname']
        upass=request.POST['upass']
        #authenticate
        u=authenticate(username=name,password=upass)
        if u is not None:
            login(request,u)
            return redirect('/products')
        else:
            context={}
            context['errmsg']="Invalid username and password !!!"
            return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('/products')  

# user profile edit function 
def profile(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            m=UserInfo.objects.filter(id=request.user.id)
            context={}
            context['data']=m
            return render(request,'profile.html',context)
        else:
            name=request.POST['fname']
            sname=request.POST['lname']
            gen=request.POST['inlineRadioOptions']
            mo=request.POST['mobile']
            add=request.POST['add']
            pin=request.POST['pin']
            mail=request.POST['mail']
            co=request.POST['country']
            st=request.POST['state']
            
            u=User.objects.filter(id=request.user.id)
            ui=UserInfo.objects.filter(id=request.user.id)
            u.update(username=mail,email=mail,first_name=name,last_name=sname)
            n=len(ui)
            if n==0:
                ui=UserInfo.objects.create(userid=u[0],gender=gen,mobile=mo,address=add,pincode=pin,country=co,state=st)
                ui.save()
            else:
                ui.update(gender=gen,mobile=mo,address=add,pincode=pin,country=co,state=st)   
            return redirect('/profile')
    else:
        return redirect('/login')   

#category filter
def catfilter(request,cv):
    q1=Q(is_active=True)
    q2=Q(cat=cv)
    p=Product.objects.filter(q1 & q2)
    #print(p)
    context={}
    context['data']=p
    return render(request,'index.html',context)

#Sort Price Filter
def sortprice(request,sv):
    if sv=='1':
        t='-price'
    else:
        t='price'
    p=Product.objects.order_by(t).filter(is_active=True)
    context={}
    context['data']=p       
    return render(request,'index.html',context)

def pricefilter(request):
    min=request.GET['min']
    max=request.GET['max']
    q1=Q(price__gte=min)
    q2=Q(price__lte=max)
    p=Product.objects.filter(q1 & q2)
    context={}
    context['data']=p
    return render(request,'index.html',context)

def product_details(request,pid):
    p=Product.objects.filter(id=pid)
    context={}
    context['data']=p
    return render(request,'product_details.html',context)

def cart(request,pid):
    if request.user.is_authenticated:
        u=User.objects.filter(id=request.user.id)
        p=Product.objects.filter(id=pid)

        #Check product exist or not
        q1=Q(userid=u[0])
        q2=Q(pid=p[0])
        c=Cart.objects.filter(q1 & q2)
        #print(c)
        n=len(c)
        context={}
        context['data']=p
        if n==1:
            context['msg']="Product already exists in the cart !!!"
        else:
            c=Cart.objects.create(userid=u[0],pid=p[0])
            c.save()
            context['success']="Product added Successfully to Cart !!!"
        return render(request,'product_details.html',context)
    else:
        return redirect('/login')

def placeorder(request):
    c=Cart.objects.filter(userid=request.user.id)
    oid=random.randrange(1000,9999)
    for x in c:
        amount=x.qty*x.pid.price
        o=Order.objects.create(orderid=oid,qty=x.qty,pid=x.pid,userid=x.userid,amt=amount)
        o.save()
        x.delete()      
    return redirect('/fetchorder')

def fetchorderdetails(request):
    u=User.objects.filter(id=request.user.id)
    orders=Order.objects.filter(userid=request.user.id)
    sum=0
    for x in orders:
        sum=sum+x.amt
    
    context={}
    context['data']=u
    context['orders']=orders
    context['tamount']=sum
    context['n']=len(orders)
    return render(request,'placeorder.html',context)

def viewcart(request):
    u=User.objects.filter(id=request.user.id)
    c=Cart.objects.filter(userid=request.user.id)
    sum=0
    for x in c:
        sum=sum+x.pid.price*x.qty
        
    context={}
    context['data']=u
    context['c']=c
    context['total']=sum
    context['n']=len(c)
    return render(request,'cart.html',context)

def updateqty(request,x,cid):
    c=Cart.objects.filter(id=cid)
    q=c[0].qty
    if x=='1':
        q=q+1
    elif q>1:
        q=q-1
    c.update(qty=q)
    return redirect('/viewcart')        
    
def removecart(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/viewcart')  

def removeord(request,oid):
    o=Order.objects.filter(id=oid)
    o.delete()
    return redirect('/fetchorder')  

def makepayment(request):
    client = razorpay.Client(auth=("rzp_test_kXFXF8rCgidqau", "s8SRf1vqU2sXYTGzj6QvWftJ"))
    orders=Order.objects.filter(userid=request.user.id)
    sum=0
    for x in orders:
        sum=sum+x.amt
        oid=x.orderid

    data = { "amount": sum*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    print(payment)
    context={}
    context['payment']=payment
    context['amount']=sum
    return render(request,'pay.html',context)

def paymentsuccess(request):
    sub="Vishwa Ekart-Order Status"
    msg="Thanks for Shopping. Order Details are:"
    frm="swamivishwa0@gmail.com"
    u=User.objects.filter(id=request.user.id)
    context={}
    context['data']=u
    to=u[0].email
    send_mail(
                sub,
                msg,
                frm,
                [to],
                fail_silently=False
            )
    o=Order.objects.filter(userid=request.user.id)
    for x in o:
        oh=OrderHistory.objects.create(orderid=x.orderid,qty=x.qty,pid=x.pid,userid=x.userid,amt=x.amt)
        oh.save()
        x.delete()
    return render(request,'paymentsuccess.html')

def cart_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(userid=request.user.id).count()
    else:
        count = 0
    return JsonResponse({'count': count})
