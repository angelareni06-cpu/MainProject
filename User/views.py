from datetime import datetime
from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Reporter.models import *
from Editor.models import *
from django.db.models import Q
# Create your views here.

def Homepage(request):
    if "uid" in request.session:
        return render(request,'User/Homepage.html')
    else:
        return render(request,'Guest/Login.html') 

def MyProfile(request):
    if "uid" in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        return render(request,'User/MyProfile.html',{"userdata": userdata})
    else:
        return render(request,'Guest/Login.html')

def EditProfile(request):
    if "uid" in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        if request.method=='POST':
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")
            address=request.POST.get("txt_address")

            userdata.user_name=name
            userdata.user_email=email
            userdata.user_contact=contact
            userdata.user_address=address
            userdata.save()
            return render(request,'User/EditProfile.html',{'msg':'updated'})
        else:
            return render(request,'User/EditProfile.html',{'userdata': userdata})
    else:
        return render(request,'Guest/Login.html')        

def ChangePassword(request): 
    if "uid" in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        userpassword=userdata.user_password
        if request.method=='POST':
            oldpassword=request.POST.get("txt_old")
            newpassword=request.POST.get("txt_new")
            confirm=request.POST.get("txt_confirm")
            if userpassword==oldpassword:
                if newpassword==confirm:
                    userdata.user_password=newpassword
                    userdata.save()
                    return render(request,'User/ChangePassword.html',{'msg':'Password Updated'})
                else:
                    return render(request,'User/ChangePassword.html',{'msg1':'Password Mismatch'})
            else:
                return render(request,'User/ChangePassword.html',{'msg1':'Password Incorrect'})
        else:
            return render(request,'User/ChangePassword.html')
    else:
        return render(request,'Guest/Login.html') 


def UploadNews(request):
    if "uid" in request.session:
        category=tbl_category.objects.all()
        subcategory=tbl_subcategory.objects.all()
        user=tbl_user.objects.get(id=request.session["uid"])
        Newsdata=tbl_news.objects.filter(user=request.session['uid'])
        if request.method=='POST':
            title=request.POST.get("txt_title")    
            content=request.POST.get("txt_content")
            image=request.FILES.get("file_image")
            subcategory=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory"))
            tbl_news.objects.create(news_title=title,news_content=content,news_image=image,subcategory=subcategory,user=user)
            return render(request,'User/UploadNews.html',{'msg':'data inserted'})
        else:
            return render(request,'User/UploadNews.html',{'category':category,'subcategory':subcategory,'Newsdata':Newsdata})  
    else:
        return render(request,'Guest/Login.html')         

def AjaxSubcategory(request):
    category=tbl_category.objects.get(id=request.GET.get("cid"))
    subcategory=tbl_subcategory.objects.filter(category=category)
    return render(request,'User/AjaxSubcategory.html',{'subcategory':subcategory})        

def delnews(request,id):
    tbl_news.objects.get(id=id).delete()
    return redirect("User:UploadNews") 

def UploadF(request,fid):
    newsdata=tbl_news.objects.get(id=fid)
    fdata=tbl_uploadfiles.objects.filter(news=fid)
    if request.method=='POST':
        UploadF=request.FILES.get("file_extra")
        tbl_uploadfiles.objects.create(upload_files=UploadF,news=newsdata)
        return render(request,'User/UploadF.html',{'msg':'data inserted','fid':fid})
    else:         
        return render(request,'User/UploadF.html',{'fdata':fdata,'fid':fid}) 

def delfile(request,id,fid):
    tbl_uploadfiles.objects.get(id=id).delete()
    return redirect("User:UploadF",fid)    

def ViewUpdatesF(request,fid):
    newsdata=tbl_news.objects.get(id=fid)
    updatedataf=tbl_newsupdatesr.objects.filter(news=fid)
    return render(request,'User/ViewUpdatesF.html',{'news':newsdata,'updates':updatedataf,'fid':fid})    

def Complaint(request):
    if "uid" in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        complaintdata=tbl_complaint.objects.filter(user_id=request.session["uid"])
        if request.method=='POST':  
            title=request.POST.get("txt_title")
            content=request.POST.get("txt_content")
            tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user_id=userdata)     
            return render(request,'User/Complaint.html',{'msg':'data inserted'}) 
        else:
            return render(request,'User/Complaint.html',{'userdata':userdata,'complaintdata':complaintdata})   
    else:
        return render(request,'Guest/Login.html') 

def delcomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("User:Complaint")                     

def MyNews(request):
    if "uid" in request.session:
        # paymentdata=tbl_payment.objects.filter(news__user=request.session['uid'])
        newsdata = tbl_news.objects.filter(user=request.session['uid'],news_status__gte=1).exclude(news_status=2)
        
        return render(request,'User/MyNews.html',{'newsdata':newsdata})
    else:
        return render(request,'Guest/Login.html')     

def chatpage(request,id):
    editor  = tbl_editor.objects.get(id=id)
    return render(request,"User/Chat.html",{"editor":editor})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_editor = tbl_editor.objects.get(id=request.POST.get("tid"))
    print(to_editor)
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,editor_to=to_editor,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(editor_from=tid) | Q(editor_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(editor_to=request.GET.get("tid")) | (Q(editor_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


def EditNews(request,fid):
    category=tbl_category.objects.all()
    NewsData=tbl_news.objects.get(id=fid)
    if request.method=='POST':
        title=request.POST.get("txt_title")    
        content=request.POST.get("txt_content")
        image=request.FILES.get("file_image")
        subcategory=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory"))

        NewsData.news_title=title
        NewsData.news_content=content
        NewsData.news_image=image
        NewsData.subcategory=subcategory
        NewsData.save()
        return render(request,'User/EditNews.html',{'msg':'data inserted'})
    else:
        return render(request,'User/EditNews.html',{'category':category,'NewsData':NewsData})
    
def Advertisement(request):
    if "uid" in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        Advdata=tbl_advertisement.objects.all()
        if request.method=='POST':
            title=request.POST.get("txt_title")  
            content=request.POST.get("txt_content") 
            file=request.POST.get("txt_file") 
            tbl_advertisement.objects.create(advertisement_title=title,advertisement_content=content,advertisement_file=file,user_id=userdata)
            return render(request,'User/Advertisement.html',{'msg':'data inserted'})    
        else:
            return render(request,'User/Advertisement.html',{'Advdata':Advdata,'userdata':userdata}) 
    else:
        return render(request,'Guest/Login.html')

def delAdv(request,id):
    tbl_advertisement.objects.get(id=id).delete()
    return redirect("User:Advertisement") 

def MyAdvertisement(request):
    if "uid" in request.session:
        # paymentdata=tbl_payment.objects.filter(news__user=request.session['uid'])
       AdvData = tbl_advertisement.objects.filter(user_id=request.session['uid'],advertisement_status__gte=3).exclude(advertisement_status=1) 
       return render(request,'User/MyAdvertisement.html',{'AdvData':AdvData})
    else:
       return render(request,'Guest/Login.html')

def Payment(request,pid):
    data=tbl_payment.objects.get(id=pid)
    amt=data.payment_amount
    if request.method=='POST':
        data.payment_status=3
        data.save()
        return redirect("User:loader")
    else:
        return render(request,'User/Payment.html',{'total':amt})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")


def Logout(request):
    del request.session["uid"]       
    return redirect("Guest:Login")     