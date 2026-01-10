from django.urls import path,include
from Editor import views
app_name="Editor"
urlpatterns = [
    path("Homepage/",views.Homepage,name="Homepage"),

    path("MyProfile/",views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),

    path('ViewVerifiednews/',views.ViewVerifiednews,name="ViewVerifiednews"),
    path('PublishedNews/<int:pid>',views.PublishedNews,name="PublishedNews"),
    path('FPublishedNews/<int:fid>',views.FPublishedNews,name="FPublishedNews"),

    path('NewsUpdatesR/<int:nid>',views.NewsUpdatesR,name="NewsUpdatesR"),
    path('ViewFiles/<int:nid>',views.ViewFiles,name="ViewFiles"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('Logout/',views.Logout,name='Logout'),
]