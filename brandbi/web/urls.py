from django.urls import path
from .views import index, about, contact, portfolio, category_detail,blog,service,service_detail,blog_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path("blog/",blog,name="blog"), 
    path("blog/<slug:slug>/", blog_detail, name="blog_detail"),
    path("service/",service,name="service"), 
    path("service_detail/<slug:slug>/",service_detail,name="service_detail"), 

]
