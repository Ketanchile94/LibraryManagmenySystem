from django.shortcuts import render, redirect
from book.models import Books, Contact
from django.db.models import Q, Max, Min, Avg, Sum, Count
from django.contrib.auth.forms import UserCreationForm
from book.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def registeruser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('login')
        context={'form':form}
        return render(request,'register.html', context)

def loginuser(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'login.html', context)
            
def logoutuser(request):
	logout(request)
	return redirect('login')
    
@login_required(login_url='login')
def index(request):
 return render(request, 'index.html')

@login_required(login_url='login')
def add(request):
    if (request.method == 'POST'):
        book = request.POST['book_name']
        author = request.POST['author_name']
        bookprice = request.POST['price']
        booktype= request.POST['Type_of_Book']
        insert_data = Books.myObjects.create(book_name= book, author_name = author, price = bookprice, Type_of_Book = booktype)
        insert_data.save()
        return redirect('/')
    return render(request,'addbook.html')

def upcomingbook(request):
     return render(request,'upcomingbook.html')

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email =request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(username=username, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent !")
    return render(request,'contact.html')


def updatebook(request,did):
    if (request.method == 'POST'):
        book = request.POST['book_name']
        author = request.POST['author_name']
        bookprice = request.POST['price']
        booktype= request.POST['Type_of_Book']
        record_to_be_update=Books.myObjects.filter(id=did)
        record_to_be_update.update(book_name= book, author_name = author, price = bookprice, Type_of_Book = booktype)
        return redirect("/")
    else:
        content={}
        content['data']=Books.myObjects.get(id=did)
        return render(request,'viewbook.html', content)

def search(request, id):
    if id== 'search':
        search_value = request.GET['search']
        q1 = Q(book_name__startswith=search_value)|Q(book_name__startswith=search_value.title())
        q2 = Q(author_name__startswith=search_value)|Q(author_name__startswith=search_value.title())
        q3 = Q(Type_of_Book__startswith=search_value)|Q(Type_of_Book__startswith=search_value.title())
        book = Books.myObjects.filter(q1|q2|q3).values()
    return render(request, 'updatebook.html', {'datas':book, 'search_value':search_value})

def display(request):
    content={}
    content['datas']=Books.myObjects.all()
    #content['data']=Books.myObjects.filter(is_deleted="n")
    return render(request,'updatebook.html', content)

def delete(request, did):
    record_to_be_deleted=Books.myObjects.filter(id=did)
    record_to_be_deleted.update(is_deleted="y")
    datas=Books.myObjects.filter(is_deleted="n")
    data={"datas":datas}
    return render(request,'updatebook.html', context=data)
                
def htol(request): #price
    datas=Books.myObjects.order_by('-price')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def ltoh(request):#price
    datas=Books.myObjects.order_by('price')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def AtoZ(request):#book
    datas=Books.myObjects.order_by('book_name')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def ZtoA(request):#book
    datas=Books.myObjects.order_by('-book_name')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def AatoZz(request):#author
    datas=Books.myObjects.order_by('author_name')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def ZztoAa(request):#author
    datas=Books.myObjects.order_by('-author_name')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def lowtohigh(request):#id
    datas=Books.myObjects.order_by('id')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def hightolow(request):#id
    datas=Books.myObjects.order_by('-id')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def CAtoZ(request):#category
    datas=Books.myObjects.order_by('type_of_book')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def CZtoA(request):#category
    datas=Books.myObjects.order_by('-type_of_book')
    data={"datas":datas}
    return render(request,'updatebook.html',context=data)

def catfilter(request,cat):#filter category
    content={}
    content['datas']=Books.myObjects.filter(Type_of_Book=cat)
    return render(request,'updatebook.html',content)
