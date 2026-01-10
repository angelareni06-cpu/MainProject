from django.urls import path,include
from User import views
app_name="User"

urlpatterns = [
    path("Homepage/",views.Homepage,name="Homepage"),

    path("MyProfile/",views.MyProfile,name="MyProfile"),
    path("EditProfile/",views.EditProfile,name="EditProfile"),
    path("ChangePassword/",views.ChangePassword,name="ChangePassword"),

    path("UploadNews/",views.UploadNews,name="UploadNews"),
    path('delnews/<int:id>',views.delnews,name="delnews"),
    path('AjaxSubcategory/',views.AjaxSubcategory,name='AjaxSubcategory'),

    path('UploadF/<int:fid>',views.UploadF,name="UploadF"),
    path('delfile/<int:id>/<int:fid>',views.delfile,name="delfile"),

    path('ViewUpdatesF/<int:fid>',views.ViewUpdatesF,name="ViewUpdatesF"),

    path('Complaint/',views.Complaint,name="Complaint"),
    path('delcomplaint/<int:id>',views.delcomplaint,name="delcomplaint"),

    path('MyNews/',views.MyNews,name="MyNews"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('Logout/',views.Logout,name='Logout'),
]