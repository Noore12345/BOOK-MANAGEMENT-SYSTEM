from django.urls import path
from . import views

urlpatterns=[
    path('amimation/',views.Animation,),
    path('',views.base),
    path('singup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('index/',views.home2),
    path('h/',views.home,name="h"),
    path('addbook/',views.addbook),
    path("seeallbook/",views.seeallbook),
    path('delete/<int:book_id>/', views.bookdelete,name="deletebook"),
    path('update/<int:book_id>/', views.update, name='update'),
    path('home/',views.home1,name="home"),
    path('addmember/',views.addmember),
    path('member/',views.seeallmember,),
    path('delet/<int:member_id>/',views.deletemember,name="deletemember"),
    path('updatem/<int:member_id>/',views.updatemember,name="updatemember"),
    path('issues/',views.home3,name="issues"),
    path('allre/',views.issues ,name="allre"),
    path('deleteissues/<int:issusID>/',views.deleteissues,name="deleteissues"),
    path('all/',views.allrecord),

]