from django.contrib import admin
from .models import HomePage,AboutPage,Skill,Blog,Contact,HomeLink






class HomeLinkInline(admin.TabularInline):
    model = HomeLink
    extra = 1

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('full_name','is_active')
    list_editable = ('is_active',)
    inlines = [HomeLinkInline]


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    inlines = [SkillInline]





@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','message','is_read',)
    list_editable = ('is_read',)