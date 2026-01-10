from django.urls import path,include
from Reporter import views
app_name="Reporter"
urlpatterns = [
    path("Homepage/",views.Homepage,name="Homepage"),

    path("MyProfile/",views.MyProfile,name="MyProfile"),
    path("EditProfile/",views.EditProfile,name="EditProfile"),
    path("ChangePassword/",views.ChangePassword,name="ChangePassword"),

    path("AddNews/",views.AddNews,name="AddNews"),
    path('delnews/<int:id>',views.delnews,name="delnews"),

    path('UploadFiles/<int:nid>',views.UploadFiles,name="UploadFiles"),
    path('delfile/<int:id>/<int:nid>',views.delfile,name="delfile"),

    path('ViewUpdates/<int:nid>',views.ViewUpdates,name="ViewUpdates"),

    path('Complaint/',views.Complaint,name="Complaint"),
    path('delcomplaint/<int:id>',views.delcomplaint,name="delcomplaint"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('Logout/',views.Logout,name='Logout'),
]