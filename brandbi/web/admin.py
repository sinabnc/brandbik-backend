from django.contrib import admin
from .models import Portfolio,Service,Category,About,Profile,Blog

# Register your models here.

@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ("name",)



@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    prepopulated_fields = {'slug': ('title',)} 

admin.site.register(About)


