from django.urls import path
from . import views
app_name='shopapp'
urlpatterns = [

    path('',views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name='productsbycategory'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='procatdetail')
    ]