from django.urls import path,include
from . views import login_user,signup_user,logout_user

app_name="accounts"
urlpatterns=[
    path("login/",login_user,name="login"),
    path("signup/",signup_user,name="signup"),
    path("logout/",logout_user,name="logout"),

]