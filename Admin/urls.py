from django.urls import path,include
from Admin import views
app_name="Admin"


urlpatterns = [
   path("HomePage/",views.HomePage,name="HomePage"),

   path('AdminRegistration/',views.AdminRegistration,name="AdminRegistration"),
   path('deladmin/<int:id>',views.deladmin,name="deladmin"),
   path('editadmin/<int:id>',views.editadmin,name="editadmin"),

   path('District/',views.District,name="District"),
   path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),
   path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),

   path('Category/',views.Category,name="category"),
   path('delcategory/<int:id>',views.delcategory,name="delcategory"),
   path('editcategory/<int:id>',views.editcategory,name="editcategory"),

   path('Place/',views.Place,name="place"),
   path('delplace/<int:id>',views.delplace,name="delplace"),
   path('editplace/<int:id>',views.editplace,name="editplace"),

   path('Subcategory/',views.Subcategory,name="subcategory"),
   path('delsub/<int:id>',views.delsub,name="delsub"),
   path('editsub/<int:id>',views.editsub,name="editsub"),

   path('Reporterverification/',views.Reporterverification,name="reporterverification"),
   path('ReporterAccept/<int:aid>',views.ReporterAccept,name="ReporterAccept"),
   path('ReporterReject/<int:rid>',views.ReporterReject,name="ReporterReject"),

   path('FreelancerType/',views.FreelancerType,name="freelancertype"),
   path('delfreelancer/<int:id>',views.delfreelancer,name="delfreelancer"),
   
   path('SkillType/',views.SkillType,name="SkillType"),
   path('delskill/<int:id>',views.delskill,name="delskill"),

   path('Userverification/',views.Userverification,name="userverification"),
   path('UserAccept/<int:aid>',views.UserAccept,name="UserAccept"),
   path('UserReject/<int:rid>',views.UserReject,name="UserReject"),

   path('EditorRegistration/',views.EditorRegistration,name="editorregistration"),
   path('deleditor/<int:id>',views.deleditor,name="deleditor"),

   path('VerifierRegistration/',views.VerifierRegistration,name="verifierregistration"),
   path('delverifier/<int:id>',views.delverifier,name="delverifier"),

   path('PublishedNews/',views.PublishedNews,name="PublishedNews"),
   path('FPublishedNews/',views.FPublishedNews,name="FPublishedNews"),
   
   path('ViewFiles/<int:fid>',views.ViewFiles,name="ViewFiles"),

   path('ViewComplaints/',views.ViewComplaints,name="viewComplaints"),
   path('Reply/<int:id>',views.Reply,name="Reply"),

   path('Payment/<int:fid>',views.Payment,name="Payment"),

   path('Plan/',views.Plan,name="Plan"),
   path('delplan/<int:id>',views.delplan,name="delplan"),

   path('Advertisement/',views.Advertisement,name="Advertisement"),
   path('PaymentAdvertisement/<int:id>',views.PaymentAdvertisement,name="PaymentAdvertisement"),

   path('Payment/<int:pid>/',views.Payment,name='Payment'),
   path('loader/',views.loader,name="loader"),
   path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

   path('Logout/',views.Logout,name="Logout"),

]