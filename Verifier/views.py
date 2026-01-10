from django.shortcuts import render,redirect
from Admin.models import *
from Reporter.models import *
# Create your views here.
def Homepage(request):
    if "Vid" in request.session:
        return render(request,'Verifier/HomePage.html')
    else:
        return render(request,'Guest/Login.html')

def MyProfile(request):
    if "Vid" in request.session:
        verifierData=tbl_verifier.objects.get(id=request.session["Vid"])
        return render(request,'Verifier/MyProfile.html',{"verifierData": verifierData})  
    else:
        return render(request,'Guest/Login.html')     

def EditProfile(request):
    if "Vid" in request.session:
        verifierData=tbl_verifier.objects.get(id=request.session["Vid"])
        if request.method=='POST':
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")

            verifierData.Verifier_name=name
            verifierData.Verifier_email=email
            verifierData.Verifier_contact=contact
            verifierData.save()
            return render(request,'Verifier/EditProfile.html',{'msg':'updated'})
        else:
            return render(request,'Verifier/EditProfile.html',{"verifierData": verifierData})
    else:
        return render(request,'Guest/Login.html')

def ChangePassword(request): 
    if "Vid" in request.session:
        verifierData=tbl_verifier.objects.get(id=request.session["Vid"])
        verifierpassword=verifierData.verifier_password
        if request.method=='POST':
            oldpassword=request.POST.get("txt_old")
            newpassword=request.POST.get("txt_new")
            confirm=request.POST.get("txt_confirm")
            if verifierpassword==oldpassword:
                if newpassword==confirm:
                    verifierData.verifier_password=newpassword
                    verifierData.save()
                    return render(request,'Verifier/ChangePassword.html',{'msg':'Password Updated'})
                else:
                    return render(request,'Verifier/ChangePassword.html',{'msg1':'Password Mismatch'})
            else:
                return render(request,'Verifier/ChangePassword.html',{'msg1':'Password Incorrect'})
        else:
            return render(request,'Verifier/ChangePassword.html')  
    else:
        return render(request,'Guest/Login.html')
        
def ViewNews(request):
    NewsData=tbl_news.objects.get(id=request.session["uid"])
    return render(request,'Verifier/ViewNewsF.html',{"NewsData": NewsData})

def ViewNewsF(request):
    if "Vid" in request.session:
        freelancer = tbl_user.objects.all()
        newsdata=tbl_news.objects.filter(user__in=freelancer)
        return render(request,'Verifier/ViewNewsF.html',{'news':newsdata})
    else:
        return render(request,'Guest/Login.html')     

def ViewAccept(request,aid):
    acceptdata=tbl_news.objects.get(id=aid)
    acceptdata.news_status=1
    acceptdata.verifier=tbl_verifier.objects.get(id=request.session['Vid'])
    acceptdata.save()
    return redirect('Verifier:ViewNewsF')

def ViewReject(request,rid):
    rejectdata=tbl_news.objects.get(id=rid)
    rejectdata.news_status=2
    rejectdata.save()
    return redirect('Verifier:ViewNewsF')

def ViewNewsR(request):
    NewsData=tbl_news.objects.get(id=request.session["Rid"])
    return render(request,'Verifier/ViewNewsR.html',{"NewsData": NewsData})

def ViewNewsR(request):
    if "Vid" in request.session:
        Reporter=tbl_reporter.objects.all()
        newsdata=tbl_news.objects.filter(reporter__in=Reporter)
        return render(request,'Verifier/ViewNewsR.html',{'news':newsdata})
    else:
        return render(request,'Guest/Login.html')     

def ViewRAccept(request,aid):
    acceptdata=tbl_news.objects.get(id=aid)
    acceptdata.news_status=1
    acceptdata.verifier=tbl_verifier.objects.get(id=request.session['Vid'])
    acceptdata.save()
    return redirect('Verifier:ViewNewsR')

def ViewRReject(request,rid):
    rejectdata=tbl_news.objects.get(id=rid)
    rejectdata.news_status=2
    rejectdata.save()
    return redirect('Verifier:ViewNewsR')   

def Logout(request):
    del request.session["Vid"]       
    return redirect("Guest:Login")          