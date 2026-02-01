from django.urls import path,include
from Verifier import views
app_name="Verifier"
urlpatterns = [
    path("Homepage/",views.Homepage,name="Homepage"),

    path("MyProfile/",views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),

    path('ViewNewsF/',views.ViewNewsF,name="ViewNewsF"),
    path('ViewAccept/<int:aid>',views.ViewAccept,name="ViewAccept"),
    path('ViewReject/<int:rid>',views.ViewReject,name="ViewReject"),
    
    path('ViewNewsR/',views.ViewNewsR,name="ViewNewsR"),
    path('ViewRAccept/<int:aid>',views.ViewRAccept,name="ViewRAccept"),
    path('ViewRReject/<int:rid>',views.ViewRReject,name="ViewRReject"),

    path('Complaint/',views.Complaint,name="Complaint"),
    path('delcomplaint/<int:id>',views.delcomplaint,name="delcomplaint"),

    path('ViewAdvertisement/',views.ViewAdvertisement,name="ViewAdvertisement"),
    path('AdvAccept/<int:aid>',views.AdvAccept,name="AdvAccept"),
    path('AdvReject/<int:rid>',views.AdvReject,name="AdvReject"),

    path('Logout/',views.Logout,name='Logout'),
]