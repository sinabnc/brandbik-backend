from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('category_detail', kwargs={'slug': self.slug})

class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolios')
    image = models.ImageField(upload_to="portfolios/")
    name = models.CharField(max_length=200)
    description= models.CharField(max_length=200)  # Corrected spelling

    def __str__(self):
        return self.name

class Services(models.Model):
    image = models.ImageField(upload_to="services/")
    image2 = models.ImageField(upload_to="services/", blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)  # Corrected spelling

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to="about/")
 

class Profile(models.Model):
    image = models.ImageField(upload_to="services/")
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)  

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    content = HTMLField()
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(auto_now_add=True)
    meta_title = models.CharField(max_length=150)  # New field for meta title
    meta_description = models.TextField()  # New field for meta description
    alt_text = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse_lazy("blog_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('date',)
        verbose_name = ('Blog')
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)  # Title of the service
    slug = models.SlugField(unique=True, max_length=100, blank=True)  # For SEO-friendly URLs
    description = HTMLField()  # Detailed description of the service
    image = models.ImageField(upload_to='service_images/')  # Service image

    date_added = models.DateField(auto_now_add=True)  # Auto-set date of addition
    meta_title = models.CharField(max_length=150)  # For SEO meta title
    meta_description = models.TextField()  # For SEO meta description
    alt_text = models.CharField(max_length=150)  # Alt text for the image

    def get_absolute_url(self):
        return reverse_lazy("service_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('date_added',)
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title