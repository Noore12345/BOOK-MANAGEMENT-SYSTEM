from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from . import models
from .models import book
from .models import Member,Record
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


# Create your views here
#animation section
def Animation(request):
    return render(request,'amimation.html')

#-----------------------AUTHENTICATION SECTION-------
def signup(request):
    if request.method =='POST':
         form=SignUpForm(request.POST)
         if form.is_valid():
              messages.success(request,'Account Created successfully ')
              form.save()
    else:
         form=SignUpForm()
    return render (request,'sig.html',{'form':form})
#login

def userlogin(request):
    if request.method =='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            userobj=authenticate(username=uname,password=upass)
            if userobj is not None:
                    login(request,userobj)
                    return HttpResponseRedirect('/index/')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/amimation/')

#-------------------BOOK SECTION---------

def home2(request):
    return render(request,"index.html")

def home(request):
    return render(request,"addbook.html")

def addbook(request):
    data=dict(request.GET)
    ID=int(data['book_id'][0])
    Book_name=data['book_name'][0]
    subject=data['subject'][0]
    author=data['author'][0]
    quantity=int(data['quantity'][0])
    data1=models.book(ID,Book_name,subject,author,quantity)
    data1.save()
    return redirect("/seeallbook")

def seeallbook(request):
    data=models.book.objects.all().values()
    data1=list(data)
    return render(request,"seeallbook.html",{"data1":data1})


def bookdelete(request,book_id):
    data=models.book.objects.get(pk=book_id)
    data.delete()
    # bookdata=models.book.objects.all()
    # return render(request,'seeallbook.html',{'bookdata':bookdata})
    return redirect('/seeallbook')

def update(request, book_id):
    bookobject = book.objects.get(pk=book_id)
    if request.method == 'POST':
        bookobject.book_name = request.POST['book_name']
        bookobject.subject = request.POST['subject']
        bookobject.author = request.POST['author']
        bookobject.quantity=request.POST['quantity']
        bookobject.save()
        return redirect('/seeallbook')
    return render(request, 'updatebook.html', {'book': bookobject})

#----------------------------MEMBER SECTION---------------------------------

def base(request):
    return render(request,"base.html")

def home1(request):
    return render(request,"member.html")

def addmember(request):
    data=dict(request.GET)
    print(data)
    member_id=int(data['member_id'][0])
    member_name=data['member_name'][0]
    mobile=int(data['mobile'][0])
    semester=int(data['semester'][0])
    branch=data['branch'][0]
    data1=models.Member(member_id,member_name,mobile,semester,branch)
    data1.save()
    return redirect("/member")

def seeallmember(request):
    data=models.Member.objects.all().values()
    datalist=list(data)
    return render(request,'seeallmember.html',{'datalist':datalist})

def deletemember(request,member_id):
    data=models.Member.objects.get(pk=member_id)
    data.delete()
    # data2=models.Member.objects.all()
    # return render(request,"seeallmember.html",{'data1':data2})
    return redirect('/member')

def updatemember(request,member_id):
    data1=Member.objects.get(pk=member_id)
    if request.method=='POST':
        data1.member_name=request.POST['member_name']
        data1.mobile=request.POST['mobile']
        data1.semester=request.POST['semester']
        data1.branch=request.POST['branch']
        data1.save()
        return redirect('/member')
    return render(request,'updatamember.html',{'data1':data1})


    # upd(request,member_id):
    # #  data=Member.objects.filter(id=member_id)
    #  if request.method=='POST':
    #       name=request.POST['member_name']
    #       mobile=request.POST['mobile']
    #       semester=request.POST['semester']
    #       branch=request.POST['branch']
    #       data1=Member.objects.filter(id=member_id).update(member_name=name,mobile=mobile,semester=semester,branch=branch)
    #       return redirect('/')
    #  else:
    #      return render(request,"upda.html")
#-------------------RECORD SECTION-----------

def home3(request):
    return render(request,'issues.html')

def issues(request):
    data=dict(request.GET)
    book_id=data['bookid'][0]
    member_id=data['memberid'][0]
    issuesid=data['Issuesid'][0]
    issuesdate=data['issuesdate'][0]
    returndate=data['returndate'][0]
    date1=models.Record(book_id,member_id,issuesid,issuesdate,returndate)
    book_object=models.book.objects.get(pk=book_id)
    if book_object.quantity>0:
        book_object.quantity -=1
        book_object.save()
        date1=models.Record(book_id,member_id,issuesid,issuesdate,returndate)

        date1.save()
        return redirect("/all")

def deleteissues(request, issusID):
    data=models.Record.objects.get(pk=issusID)
    data.delete()
    return redirect("/all")

# def issuesupdate(request, issusID):
#     data=Record.objects.get(pk= issusID)
#     if request.method=='POST':
#        data.book=request.POST['book_id'][0]
#        data.Member=request.POST['member_id'][0]
#        data.issusID=request.POST['issusID'][0]
#        data.issudate=request.POST['issudate'][0]
#        data.returndate=request.POST['returndate'][0]
#        data.save()
#        return redirect('/all')
#     return render(request,'issuesupdate.html',{'data':data})     



def allrecord(request):
    data=models.Record.objects.all().values()
    data1=  list(data)

    data2=[]
    for i in data1:
        i['issudate'] = str(i['issudate'])
        i['returndate']=str(i['returndate'])
        data2.append(i)
        


    return render(request,'issuesd.html',{'data1':data2})



    

         


