from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
    path('UserRegistration/',views.UserRegistration,name='UserRegistration'),
    path('Login/',views.Login,name='Login'),
    path('AjaxPlace/',views.AjaxPlace,name='ajaxplace'),
    path('AjaxSkilltype/',views.AjaxSkilltype,name='ajaxskilltype'),
    path('Reporter/',views.Reporter,name='Reporter'),
]