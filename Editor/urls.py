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
    path('delremarks/<int:nid>',views.delremarks,name="delremarks"),
    path('ViewFiles/<int:nid>',views.ViewFiles,name="ViewFiles"),
    path('ViewRAccept/<int:aid>/<int:nid>',views.ViewRAccept,name="ViewRAccept"),
    path('ViewRReject/<int:rid>/<int:nid>',views.ViewRReject,name="ViewRReject"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('chatpager/<int:id>',views.chatpager,name="chatpager"),
    path('ajaxchatr/',views.ajaxchatr,name="ajaxchatr"),
    path('ajaxchatviewr/',views.ajaxchatviewr,name="ajaxchatviewr"),
    path('clearchatr/',views.clearchatr,name="clearchatr"),

    path('PublishedNews/',views.PublishedNews,name="PublishedNews"),
    path('FPublishedNews/',views.FPublishedNews,name="FPublishedNews"),

    path('Logout/',views.Logout,name='Logout'),
]