from datetime import datetime
from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Reporter.models import *
from Editor.models import *
from User.models import *
from django.db.models import Q
# Create your views here.

def Homepage(request):
    if "Rid" in request.session:
        rep=tbl_reporter.objects.get(id=request.session['Rid'])
        return render(request,'Reporter/HomePage.html',{"rep":rep})
    else:
        return render(request,'Guest/Login.html')    
    
def MyProfile(request):
    if "Rid" in request.session:
        reporterdata=tbl_reporter.objects.get(id=request.session["Rid"])
        return render(request,'Reporter/MyProfileR.html',{"reporterdata": reporterdata})
    else:
        return render(request,'Guest/Login.html')     
    
def EditProfile(request):
    if "Rid" in request.session:
        reporterdata=tbl_reporter.objects.get(id=request.session["Rid"])
        if request.method=='POST':
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")
            address=request.POST.get("txt_address")

            reporterdata.reporter_name=name
            reporterdata.reporter_email=email
            reporterdata.reporter_contact=contact
            reporterdata.reporter_address=address
            reporterdata.save()
            return render(request,'Reporter/EditProfile.html',{'msg':'updated'})
        else:
            return render(request,'Reporter/EditProfile.html',{'reporterdata': reporterdata})
    else:
        return render(request,'Guest/Login.html')         

def ChangePassword(request):
    if "Rid" in request.session: 
        reporterdata=tbl_reporter.objects.get(id=request.session["Rid"])
        reporterpassword=reporterdata.reporter_password
        if request.method=='POST':
            oldpassword=request.POST.get("txt_old")
            newpassword=request.POST.get("txt_new")
            confirm=request.POST.get("txt_confirm")
            if reporterpassword==oldpassword:
                if newpassword==confirm:
                    reporterdata.reporter_password=newpassword
                    reporterdata.save()
                    return render(request,'Reporter/ChangePassword.html',{'msg':'Password Updated'})
                else:
                    return render(request,'Reporter/ChangePassword.html',{'msg1':'Password Mismatch'})
            else:
                return render(request,'Reporter/ChangePassword.html',{'msg1':'Password Incorrect'})
        else:
            return render(request,'Reporter/ChangePassword.html') 
    else:
        return render(request,'Guest/Login.html')           

def AddNews(request):
    if "Rid" in request.session:
        category=tbl_category.objects.all()
        subcategory=tbl_subcategory.objects.all()
        reporterdata=tbl_reporter.objects.get(id=request.session["Rid"])
        NewsData=tbl_news.objects.filter(reporter=request.session['Rid'])
        if request.method=='POST':
            title=request.POST.get("txt_title")    
            content=request.POST.get("txt_content")
            image=request.FILES.get("file_image")
            subcategory=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory"))
            tbl_news.objects.create(news_title=title,news_content=content,news_image=image,subcategory=subcategory,reporter=reporterdata)
            return render(request,'Reporter/AddNews.html',{'msg':'data inserted'})
        else:
            return render(request,'Reporter/AddNews.html',{'category':category,'subcategory':subcategory,'NewsData':NewsData})
    else:
        return render(request,'Guest/Login.html')             

def AjaxSubcategory(request):
    category=tbl_category.objects.get(id=request.GET.get("cid"))
    subcategory=tbl_subcategory.objects.filter(category=category)
    return render(request,'User/AjaxSubcategory.html',{'subcategory':subcategory})         

def delnews(request,id):
    tbl_news.objects.get(id=id).delete()
    return redirect("Reporter:AddNews")

def UploadFiles(request,nid):
    newsdata=tbl_news.objects.get(id=nid)
    uploaddata=tbl_uploadfiles.objects.filter(news=nid)
    if request.method=='POST':
        UploadFiles=request.FILES.get("file_upload")
        tbl_uploadfiles.objects.create(upload_files=UploadFiles,news=newsdata)
        return render(request,'Reporter/Upload.html',{'msg':'data inserted','nid':nid})
    else:
        return render(request,'Reporter/Upload.html',{'uploaddata':uploaddata,'nid':nid})

def delfile(request,id,nid):
    tbl_uploadfiles.objects.get(id=id).delete()
    return redirect("Reporter:UploadFiles",nid)  

def ViewUpdates(request,nid):
    newsdata=tbl_news.objects.get(id=nid)
    updatedata=tbl_newsupdatesr.objects.filter(news=nid)
    return render(request,'Reporter/ViewUpdates.html',{'news':newsdata,'updates':updatedata,'nid':nid})

def Complaint(request):
    if "rid" not in request.session:
        reporterdata=tbl_reporter.objects.get(id=request.session["Rid"])
        complaintdata=tbl_complaint.objects.filter(reporter_id=request.session["Rid"])
        if request.method=='POST':
            title=request.POST.get("txt_title")
            content=request.POST.get("txt_content")
            tbl_complaint.objects.create(complaint_title=title,complaint_content=content,reporter_id=reporterdata)   
            return render(request,'Reporter/Complaint.html',{'msg':'data inserted'})
        else:
            return render(request,'Reporter/Complaint.html',{'reporterdata':reporterdata,'complaintdata':complaintdata})
    else:
        return render(request,'Guest/Login.html')         

def delcomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()  
    return redirect("Reporter:Complaint")   

def MyNews(request):
    if "Rid" in request.session:
        newsdata = tbl_news.objects.filter(reporter=request.session['Rid'],news_status__gte=1).exclude(news_status=2)
        
        return render(request,'Reporter/MyNews.html',{'newsdata':newsdata})
    else:
        return render(request,'Guest/Login.html')

def chatpage(request,id):
    editor  = tbl_editor.objects.get(id=id)
    return render(request,"Reporter/Chat.html",{"editor":editor})

def ajaxchat(request):
    from_reporter = tbl_reporter.objects.get(id=request.session["Rid"])
    to_editor = tbl_editor.objects.get(id=request.POST.get("tid"))
    print(to_editor)
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),reporter_from=from_reporter,editor_to=to_editor,chat_file=request.FILES.get("file"))
    return render(request,"Reporter/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    reporter = tbl_reporter.objects.get(id=request.session["Rid"])
    chat_data = tbl_chat.objects.filter((Q(reporter_from=reporter) | Q(reporter_to=reporter)) & (Q(editor_from=tid) | Q(editor_to=tid))).order_by('chat_time')
    return render(request,"Reporter/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(reporter_from=request.session["Rid"]) & Q(editor_to=request.GET.get("tid")) | (Q(editor_from=request.GET.get("tid")) & Q(reporter_to=request.session["Rid"]))).delete()
    return render(request,"Reporter/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def EditNews(request,nid):
    category=tbl_category.objects.all()
    NewsData=tbl_news.objects.get(id=nid)
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
        return render(request,'Reporter/EditNews.html',{'msg':'data inserted'})
    else:
        return render(request,'Reporter/EditNews.html',{'category':category,'NewsData':NewsData})      

def Logout(request):
    del request.session["Rid"]       
    return redirect("Guest:Login")      