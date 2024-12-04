from django.shortcuts import render,get_object_or_404
from .models import Portfolio,Service,Category,Profile,Blog

# Create your views here.
def index(request):
    services=Service.objects.all()
    context={
    'services':services
   }
    return render(request,"web/index.html",context)


def about(request):
    abouts=Service.objects.all()
    profiles=Profile.objects.all()
    context={
    'abouts':abouts,
    'profiles':profiles
   }
    return render(request,"web/about.html",context)


def contact(request):
    return render(request,"web/contact-us.html")


def portfolio(request):
     port=Portfolio.objects.all()
     categories = Category.objects.all()
     context={
    'port':port,
    'categories': categories,

   }
     return render(request,"web/portfolio.html",context)
   

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    portfolios = category.portfolios.all()
    services = category.services.all()

    context = {
        'category': category,
        'portfolios': portfolios,
        'services': services,
    }
    return render(request, 'web/category_detail.html', context)


def blog(request):
    blogs = Blog.objects.all()
    context = {"is_blog": True,
               "blogs": blogs}
    return render(request, "web/blog.html", context)

def blog_detail(request,slug):
    blog = Blog.objects.get(slug=slug)
    other_blogs = Blog.objects.all().exclude(slug=slug)
    context = {"is_blog": True,
               "blog": blog,
               "other_blogs": other_blogs}
    
    return render(request, "web/blog-single.html", context)



def service(request):
    services = Service.objects.all()
    context = {"is_service": True,
               "services": services
               }
    return render(request, "web/services.html", context)

def service_detail(request,slug):
    service = Service.objects.get(slug=slug)
    other_services = Service.objects.all().exclude(slug=slug)
    context = {"is_service": True,
               "service": service,
               "other_services": other_services,
               }
    return render(request, "web/service-single.html", context)