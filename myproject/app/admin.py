from django.contrib import admin
import admin_thumbnails
from app.models import *
# Register your models here.


@admin_thumbnails.thumbnail('detail_image')
class AdminContent(admin.ModelAdmin):
    list_display = ( "header","detail_image_thumbnail","country","order","create_date","active",)
    search_fields = ["header"]
    list_editable = ('order','active')
    prepopulated_fields = {"url_name": ("header",)}
admin.site.register(Content,AdminContent)

class AdminFavorite(admin.ModelAdmin):
    list_display = ( "id","post","user",)
admin.site.register(Favorite,AdminFavorite)


class AdminNavigation(admin.ModelAdmin):
    list_display    = ('name', 'order', 'status',)
    list_editable = ('order','status')
    prepopulated_fields = {"url_name": ("name",)}
admin.site.register(Navigation, AdminNavigation)





class AdminCategory(admin.ModelAdmin):
    list_display    = ('name', 'status', 'popular',)
    prepopulated_fields = {"url_name": ("name",)}
admin.site.register(Category, AdminCategory)


class AdminTag(admin.ModelAdmin):
    list_display    = ('name', 'status', 'popular',)
    prepopulated_fields = {"url_name": ("name",)}
admin.site.register(Tag, AdminTag)

@admin_thumbnails.thumbnail('flag')
class AdminCountry(admin.ModelAdmin):
    list_display    = ('name', 'flag_thumbnail', 'status', 'popular',)
    prepopulated_fields = {"url_name": ("name",)}
admin.site.register(Country, AdminCountry)


class AdminContinent(admin.ModelAdmin):
    list_display    = ('name', 'order')
    list_editable = ('order',)
admin.site.register(Continent, AdminContinent)


class AdminQuickInfo(admin.ModelAdmin):
    list_display    = ('id', )
admin.site.register(QuickInfo, AdminQuickInfo)



class AdminContact(admin.ModelAdmin):
    list_display    = ('name', 'id', 'email',)
admin.site.register(Contact, AdminContact)

class AdminFooterSubscribe(admin.ModelAdmin):
    list_display    = ('id', 'email',)
admin.site.register(FooterSubscribe, AdminFooterSubscribe)

class AdminFooterMessage(admin.ModelAdmin):
    list_display    = ('id', 'message')
admin.site.register(FooterMessage, AdminFooterMessage)

class AdminProfile(admin.ModelAdmin):
    list_display = ('name','surname','user','email')
admin.site.register(Profile, AdminProfile)

class AdminComment(admin.ModelAdmin):
    list_display = ('message','profile','secondComment')
admin.site.register(Comment, AdminComment)

class AdminEntry(admin.ModelAdmin):
    list_display = ('heading','profile','active',)
admin.site.register(Entry, AdminEntry)

class AdminHotTopic(admin.ModelAdmin):
    list_display = ('heading','date_created')
admin.site.register(HotTopic, AdminHotTopic)

class AdminPolicy(admin.ModelAdmin):
    list_display = ('heading','active')
admin.site.register(Policy, AdminPolicy)












class AdminExpireCode(admin.ModelAdmin):
    list_display = ('encrypted_id','profile',)
admin.site.register(ExpireCode, AdminExpireCode)
