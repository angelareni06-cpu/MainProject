from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Reporter.models import *
from Editor.models import *
from User.models import *
# Create your views here.
def HomePage(request):
    if "aid" in request.session:
        return render(request,'Admin/HomePage.html')
    else:
        return render(request,'Guest/Login.html')
    

def AdminRegistration(request):
    if "aid" in request.session:
        data=tbl_admin.objects.all()
        if request.method=='POST':
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            password=request.POST.get("txt_password")
            tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
            return render(request,'Admin/AdminRegistration.html',{'msg':'data inserted'})
        else:
            return render(request,'Admin/AdminRegistration.html',{'AdminRegistration':data})
    else:
        return render(request,'Guest/Login.html')         

def deladmin(request,id):
    tbl_admin.objects.get(id=id).delete()
    return redirect("Admin:AdminRegistration") 

def editadmin(request,id):
    editdata=tbl_admin.objects.get(id=id)
    data=tbl_admin.objects.all() 
    if request.method=='POST':
        name=request.POST.get("txt_name")
        editdata.admin_name=name
        email=request.POST.get("txt_email")
        editdata.admin_email=email
        password=request.POST.get("txt_password")
        editdata.admin_password=password
        editdata.save()
        return redirect('Admin:AdminRegistration')
    else:
        return render(request,'Admin/AdminRegistration.html',{'editdata':editdata,'AdminRegistration':data})    


def District(request):
    if "aid" in request.session:
        data=tbl_district.objects.all()
        if request.method=='POST':
            district=request.POST.get("txt_district")  
            tbl_district.objects.create(district_name=district)
            return render(request,'Admin/District.html',{'msg':'data inserted'})    
        else:
            return render(request,'Admin/District.html',{'district':data}) 
    else:
        return render(request,'Guest/Login.html')

def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:District") 

def editdistrict(request,id):
    editdata=tbl_district.objects.get(id=id)
    data=tbl_district.objects.all()
    if request.method=='POST':
        district=request.POST.get("txt_district")
        editdata.district_name=district
        editdata.save()
        return redirect('Admin:District')
    else:    
        return render(request,'Admin/District.html',{'editdata':editdata,'distict':data})          

def Category(request):
    if "aid" in request.session:
        data=tbl_category.objects.all()
        if request.method=='POST':
            category=request.POST.get("txt_category")      
            tbl_category.objects.create(category_name=category)    
            return render(request,'Admin/Category.html',{'msg':'data inserted'})   
        else:
            return render(request,'Admin/Category.html',{'category':data})   
    else:
        return render(request,'Guest/Login.html')    

def delcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category")  

def editcategory(request,id):
    editdata=tbl_category.objects.get(id=id)  
    data=tbl_category.objects.all()
    if request.method=='POST':
        category=request.POST.get("txt_category")    
        editdata.category_name=category
        editdata.save()
        return redirect('Admin:category')   
    else:   
        return render(request,'Admin/Category.html',{'editdata':editdata,'category':data})

def Place(request):
    if "aid" in request.session:
        data=tbl_district.objects.all()
        placedata=tbl_place.objects.all()
        if request.method=='POST':
            place=request.POST.get("txt_place")
            district=tbl_district.objects.get(id=request.POST.get("sel_district"))
            tbl_place.objects.create(place_name=place,district=district)
            return render(request,'Admin/Place.html',{'msg':'data inserted'})
        else:
            return render(request,'Admin/Place.html',{'district':data,'place':placedata})    
    else:
        return render(request,'Guest/Login.html')

def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")       

def editplace(request,id):
    district=tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=id)
    if request.method=='POST':
        place=request.POST.get("txt_place")
        editdata.district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        editdata.place_name=place
        editdata.save()
        return redirect("Admin:place")
    else:
        return render(request,'Admin/Place.html',{'editdata':editdata,'district':district})   

def Subcategory(request):
    if "aid" in request.session:
        catdata=tbl_category.objects.all()
        subdata=tbl_subcategory.objects.all()
        if request.method=='POST':
            subcategory=request.POST.get("txt_subcategory")
            category=tbl_category.objects.get(id=request.POST.get("sel_category"))
            tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
            return render(request,'Admin/Subcategory.html',{'msg':'data inserted'})
        else:
            return render(request,'Admin/Subcategory.html',{'category':catdata,'subcategory':subdata})    
    else:
        return render(request,'Guest/Login.html')         

def delsub(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory")       

def editsub(request,id):
    category=tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=id)
    if request.method=='POST':
        subcategory=request.POST.get("txt_subcategory")
        editdata.category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        editdata.subcategory_name=subcategory
        editdata.save()
        return redirect("Admin:subcategory")
    else:
        return render(request,'Admin/Subcategory.html',{'editdata':editdata,'category':category})  

def Reporterverification(request):
    if "aid" in request.session:
        pending=tbl_reporter.objects.filter(reporter_status = 0)
        accept=tbl_reporter.objects.filter(reporter_status = 1)
        reject=tbl_reporter.objects.filter(reporter_status = 2)
        return render(request,'Admin/ReporterVerification.html',{'pending':pending,'accept':accept,'reject':reject})
    else:
        return render(request,'Guest/Login.html')    

def ReporterAccept(request,aid):
    acceptdata=tbl_reporter.objects.get(id=aid)
    acceptdata.reporter_status=1
    acceptdata.save()
    return redirect('Admin:reporterverification')

def ReporterReject(request,rid):
    rejectdata=tbl_reporter.objects.get(id=rid)
    rejectdata.reporter_status=2
    rejectdata.save()
    return redirect('Admin:reporterverification')    

def FreelancerType(request):
    if "aid" in request.session:
        freelancerdata=tbl_freelancertype.objects.all()
        if request.method=='POST':
            freelancertype=request.POST.get("txt_type")  
            tbl_freelancertype.objects.create(freelancer_type=freelancertype)
            return render(request,'Admin/FreelancerType.html',{'msg':'data inserted'})    
        else:
            return render(request,'Admin/FreelancerType.html',{'freelancer':freelancerdata})
    else:
        return render(request,'Guest/Login.html')        

def delfreelancer(request,id):
    tbl_freelancertype.objects.get(id=id).delete()
    return redirect("Admin:freelancertype")          

def SkillType(request):
    if "aid" in request.session:
        freelancerdata=tbl_freelancertype.objects.all()
        skilldata=tbl_skilltype.objects.all()
        if request.method=='POST':
            skilltype=request.POST.get("txt_skill")
            freelancer=tbl_freelancertype.objects.get(id=request.POST.get("sel_freelancertype"))
            tbl_skilltype.objects.create(skill_type=skilltype,freelancer_type=freelancer)
            return render(request,'Admin/Skill.html',{'msg':'data inserted'})    
        else:
            return render(request,'Admin/Skill.html',{'freelancer':freelancerdata,'skilltype':skilldata})
    else:
        return render(request,'Guest/Login.html')         

def delskill(request,id):
    tbl_skilltype.objects.get(id=id).delete()
    return redirect("Admin:SkillType")  

def Userverification(request):
    if "aid" in request.session:
        pending=tbl_user.objects.filter(user_status = 0)
        accept=tbl_user.objects.filter(user_status = 1)
        reject=tbl_user.objects.filter(user_status = 2)
        return render(request,'Admin/UserVerification.html',{'pending':pending,'accept':accept,'reject':reject})
    else:
        return render(request,'Guest/Login.html')     

def UserAccept(request,aid):
    acceptdata=tbl_user.objects.get(id=aid)
    acceptdata.user_status=1
    acceptdata.save()
    return redirect('Admin:userverification')

def UserReject(request,rid):
    rejectdata=tbl_user.objects.get(id=rid)
    rejectdata.user_status=2
    rejectdata.save()
    return redirect('Admin:userverification')  

def EditorRegistration(request):
    if "aid" in request.session:
        district=tbl_district.objects.all()
        place=tbl_place.objects.all()
        editorData=tbl_editor.objects.all()
        if request.method=='POST':
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")
            photo=request.FILES.get("file_photo")
            proof=request.FILES.get("file_proof")
            password=request.POST.get("txt_password")
            place=tbl_place.objects.get(id=request.POST.get("sel_place"))
            tbl_editor.objects.create(editor_name=name,editor_email=email,editor_contact=contact,editor_photo=photo,editor_proof=proof,editor_password=password,place=place) 
            return render(request,'Admin/EditorRegistration.html',{'msg':'data inserted'})
        else:
            return render(request,'Admin/EditorRegistration.html',{'district':district,'place':place,'editorData':editorData})
    else:
        return render(request,'Guest/Login.html')         

def deleditor(request,id):
    tbl_editor.objects.get(id=id).delete()
    return redirect("Admin:editorregistration")   

def VerifierRegistration(request):
    if "aid" in request.session:
        district=tbl_district.objects.all()
        place=tbl_place.objects.all()
        verifierData=tbl_verifier.objects.all()
        if request.method=='POST':
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")
            photo=request.FILES.get("file_photo")
            proof=request.FILES.get("file_proof")
            password=request.POST.get("txt_password")
            place=tbl_place.objects.get(id=request.POST.get("sel_place"))
            tbl_verifier.objects.create(verifier_name=name,verifier_email=email,verifier_contact=contact,verifier_photo=photo,verifier_proof=proof,verifier_password=password,place=place)
            return render(request,'Admin/VerifierRegistration.html',{'msg':'data inserted'})
        else:
            return render(request,'Admin/VerifierRegistration.html',{'district':district,'place':place,'verifierData':verifierData})
    else:
        return render(request,'Guest/Login.html')         

def delverifier(request,id):
    tbl_verifier.objects.get(id=id).delete()
    return redirect("Admin:verifierregistration")  

def PublishedNews(request):
    if "aid" in request.session:
        reporterdata=tbl_reporter.objects.all()
        publishdata=tbl_news.objects.all()
        NewsData=tbl_news.objects.filter(news_status=3,reporter__in=reporterdata)
        return render(request,'Admin/PublishedNews.html',{"NewsData": NewsData,'reporterdata':reporterdata})
    else:
        return render(request,'Guest/Login.html')     

def FPublishedNews(request):
    if "aid" in request.session:    
        userdata=tbl_user.objects.all()
        fpublishdata=tbl_news.objects.all()
        NewsData=tbl_news.objects.filter(news_status=3,user__in=userdata)
        return render(request,'Admin/FPublishedNews.html',{"Newsdata":NewsData,'userdata':userdata})
    else:
        return render(request,'Guest/Login.html')     

def ViewFiles(request,fid):
    UploadF=tbl_uploadfiles.objects.filter(news=fid,upload_status=1)
    return render(request,'Admin/ViewFiles.html',{'UploadF':UploadF})

def ViewComplaints(request):
    if "aid" in request.session:
        userdata=tbl_user.objects.all()
        reporterdata=tbl_reporter.objects.all()
        complaintdata=tbl_complaint.objects.filter(user_id__in=userdata)
        Complaintdata=tbl_complaint.objects.filter(reporter_id__in=reporterdata)
        return render(request,'Admin/ViewComplaints.html',{'complaintdata':complaintdata,'Complaintdata':Complaintdata}) 
    else:
        return render(request,'Guest/Login.html')     
           
def Reply(request,id):
    userdata=tbl_user.objects.all()
    complaintdata=tbl_complaint.objects.get(id=id)
    if request.method=='POST':
        reply=request.POST.get("txt_reply") 
        complaintdata.complaint_reply=reply
        complaintdata.complaint_status=1
        complaintdata.save()
        return render(request,'Admin/Reply.html',{'msg':'data inserted'})
    else:
        return render(request,'Admin/Reply.html',{'complaintdata':complaintdata,'userdata':userdata})

def Payment(request,fid):
    newsdata=tbl_news.objects.get(id=fid)
    if request.method=='POST':
        amount=request.POST.get("txt_amount")  
        tbl_payment.objects.create(payment_amount=amount,news=newsdata,payment_status=1)
        return render(request,'Admin/Payment.html',{'msg':'data inserted'})
    else:
        return render(request,'Admin/Payment.html',{'newsdata':newsdata})

def Logout(request):
    del request.session["aid"]       
    return redirect("Guest:Login") 