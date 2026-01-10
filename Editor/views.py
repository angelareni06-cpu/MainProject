from django.shortcuts import render,redirect
from Admin.models import *
from Reporter.models import *
from Editor.models import *
from User.models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def Homepage(request):
    if "Eid" in request.session:
        return render(request,'Editor/Homepage.html')
    else:
        return render(request,'Guest/Login.html')

def MyProfile(request):
    if "Eid" in request.session:
        editordata=tbl_editor.objects.get(id=request.session["Eid"])
        return render(request,'Editor/MyProfileE.html',{"editordata": editordata})   
    else:
        return render(request,'Guest/Login.html')     

def EditProfile(request):
    if "Eid" in request.session:
        editordata=tbl_editor.objects.get(id=request.session["Eid"])
        if request.method=='POST':
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")

            editordata.editor_name=name
            editordata.editor_email=email
            editordata.editor_contact=contact
            editordata.save()
            return render(request,'Editor/EditProfile.html',{'msg':'updated'})
        else:
            return render(request,'Editor/EditProfile.html',{"editordata": editordata})
    else:
        return render(request,'Guest/Login.html')        

def ChangePassword(request): 
    if "Eid" in request.session:
        editordata=tbl_editor.objects.get(id=request.session["Eid"])
        editorpassword=editordata.editor_password
        if request.method=='POST':
            oldpassword=request.POST.get("txt_old")
            newpassword=request.POST.get("txt_new")
            confirm=request.POST.get("txt_confirm")
            if editorpassword==oldpassword:
                if newpassword==confirm:
                    editordata.editor_password=newpassword
                    editordata.save()
                    return render(request,'Editor/ChangePassword.html',{'msg':'Password Updated'})
                else:
                    return render(request,'Editor/ChangePassword.html',{'msg1':'Password Mismatch'})
            else:
                return render(request,'Editor/ChangePassword.html',{'msg1':'Password Incorrect'})
        else:
            return render(request,'Editor/ChangePassword.html')  
    else:
        return render(request,'Guest/Login.html')          

def ViewVerifiednews(request):
    if "Eid" in request.session:
        reporterdata=tbl_reporter.objects.all()
        reporternews=tbl_news.objects.filter(news_status=1,reporter__in=reporterdata)
        userdata=tbl_user.objects.all()
        freelancernews=tbl_news.objects.filter(news_status=1,user__in=userdata)
        return render(request,'Editor/ViewVerifiednews.html',{'reporternews':reporternews,'freelancernews':freelancernews})
    else:
        return render(request,'Guest/Login.html')     

def PublishedNews(request,pid):
    publishdata=tbl_news.objects.get(id=pid)
    publishdata.news_status=3
    publishdata.save()  
    return redirect('Editor:ViewVerifiednews')   

def FPublishedNews(request,fid):
    fpublishdata=tbl_news.objects.get(id=fid)     
    fpublishdata.news_status=3
    fpublishdata.save()
    return redirect('Editor:ViewVerifiednews')

def NewsUpdatesR(request,nid):
    newsdata=tbl_news.objects.get(id=nid)
    NewsUpdatesR=tbl_newsupdatesr.objects.filter(news=newsdata)
    if request.method=='POST':
        remarks=request.POST.get("txt_remarks")
        editorId= tbl_editor.objects.get(id=request.session['Eid'])
        tbl_newsupdatesr.objects.create(newsupdatesr_remarks=remarks,news=newsdata,editor=editorId)
        return render(request,'Editor/NewsUpdatesR.html',{'msg':'data inserted','nid':nid})
    else:
        return render(request,'Editor/NewsUpdatesR.html',{'newsdata':newsdata,'NewsUpdatesR':NewsUpdatesR,'nid':nid})

def ViewFiles(request,nid):
    reporterdata=tbl_reporter.objects.all()
    uploaddata=tbl_uploadfiles.objects.filter(news=nid)
    return render(request,'Editor/ViewFiles.html',{'uploaddata':uploaddata,'nid':nid})

def ViewRAccept(request,aid,nid):
    acceptdata=tbl_uploadfiles.objects.get(id=aid)
    acceptdata.upload_status=1
    acceptdata.editor=tbl_editor.objects.get(id=request.session['Eid'])
    acceptdata.save()
    return redirect('Editor:ViewFiles',nid)

def ViewRReject(request,rid,nid):
    rejectdata=tbl_uploadfiles.objects.get(id=rid)
    rejectdata.upload_status=2
    rejectdata.save()
    return redirect('Editor:ViewFiles',nid)   

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Editor/Chat.html",{"user":user})

def ajaxchat(request):
    from_editor = tbl_editor.objects.get(id=request.session["Eid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),editor_from=from_editor,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Editor/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    editor = tbl_editor.objects.get(id=request.session["Eid"])
    chat_data = tbl_chat.objects.filter((Q(editor_from=editor) | Q(editor_to=editor)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Editor/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(editor_from=request.session["aid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(editor_to=request.session["aid"]))).delete()
    return render(request,"Editor/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def chatpager(request,id):
    reporter  = tbl_reporter.objects.get(id=id)
    return render(request,"Editor/ChatR.html",{"reporter":reporter})

def ajaxchatr(request):
    from_editor = tbl_editor.objects.get(id=request.session["Eid"])
    to_reporter = tbl_reporter.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),editor_from=from_editor,reporter_to=to_reporter,chat_file=request.FILES.get("file"))
    return render(request,"Editor/ChatR.html")

def ajaxchatviewr(request):
    tid = request.GET.get("tid")
    editor = tbl_editor.objects.get(id=request.session["Eid"])
    chat_data = tbl_chat.objects.filter((Q(editor_from=editor) | Q(editor_to=editor)) & (Q(reporter_from=tid) | Q(reporter_to=tid))).order_by('chat_time')
    return render(request,"Editor/ChatViewR.html",{"data":chat_data,"tid":int(tid)})

def clearchatr(request):
    tbl_chat.objects.filter(Q(editor_from=request.session["aid"]) & Q(reporter_to=request.GET.get("tid")) | (Q(reporter_from=request.GET.get("tid")) & Q(editor_to=request.session["aid"]))).delete()
    return render(request,"Editor/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})  

def PublishedNews(request):
    if "Eid" in request.session:
        reporterdata=tbl_reporter.objects.all()
        publishdata=tbl_news.objects.all()
        NewsData=tbl_news.objects.filter(news_status=3,reporter__in=reporterdata)
        return render(request,'Editor/PublishedNews.html',{"NewsData": NewsData,'reporterdata':reporterdata})
    else:
        return render(request,'Guest/Login.html')   
    
def FPublishedNews(request):
    if "Eid" in request.session:    
        userdata=tbl_user.objects.all()
        fpublishdata=tbl_news.objects.all()
        NewsData=tbl_news.objects.filter(news_status=3,user__in=userdata)
        return render(request,'Editor/FPublishedNews.html',{"Newsdata":NewsData,'userdata':userdata})
    else:
        return render(request,'Guest/Login.html')     

def Logout(request):
    del request.session["Eid"]       
    return redirect("Guest:Login")  