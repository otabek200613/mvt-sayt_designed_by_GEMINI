from django.db import models
from django.contrib.auth.models import User


class HomePage(models.Model):
    icon = models.ImageField(upload_to='images/',blank=True,null=True,verbose_name='Icon')
    page_title = models.CharField(max_length=200,blank=True,verbose_name='Page Title')
    logo = models.CharField(max_length=15,blank=True,verbose_name="Logo uchun so'z")
    photo = models.ImageField(upload_to='images/',verbose_name="Home page uchun rasm")
    job= models.CharField(max_length=50,verbose_name="Kasb")
    language = models.CharField(max_length=50,verbose_name="Dasturlash tillari")
    full_name = models.CharField(max_length=50,verbose_name="Ism va familiya")
    description = models.TextField(verbose_name="Qisqacha ma'lumot")
    address = models.CharField(max_length=50,blank=True,verbose_name="Kontakt uchun Adress")
    email = models.EmailField(max_length=50,blank=True,verbose_name="Kontakt uchun Email")

    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name

class HomeLink(models.Model):
    home_page = models.ForeignKey(HomePage,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.title
class AboutPage(models.Model):
    photo = models.ImageField(upload_to='images/',blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,verbose_name="About uchun so'z")
    description = models.TextField(verbose_name="Qisqacha ma'lumot")
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Skill(models.Model):
    aboout = models.ForeignKey(AboutPage,on_delete=models.CASCADE)
    emoji = models.CharField(max_length=50,blank=True,verbose_name="Emoji")
    skill = models.CharField(max_length=50,blank=True,verbose_name="Skill")
    description = models.TextField(verbose_name="Qisqacha ma'lumot")
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.skill

class Blog(models.Model):
    photo = models.ImageField(upload_to='images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50,blank=True,verbose_name="Blog kategoriyasi")
    title = models.CharField(max_length=200,blank=True,verbose_name="Blog nomi ")
    detail_title = models.CharField(max_length=50,blank=True,verbose_name="Detail sahifa uchun nom")
    body = models.TextField(blank=True,verbose_name="Blog haqida umumiy ma'lumot")
    url = models.URLField(blank=True,null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png')
    full_name = models.CharField(max_length=50,blank=True,null=True)
    username = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)


    def __str__(self):
        return f"{self.user.username} profili"






























