from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ContentSitemap, StaticSitemap, CountrySitemap, TagSitemap, CategorySitemap
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name = "app"

sitemaps = {
    'post':ContentSitemap,
    'country':CountrySitemap,
    'static':StaticSitemap,
    'tag':TagSitemap,
    'category':CategorySitemap,
}

urlpatterns = [
    
    path('', views.homepage, name="homepage"),
    path('random-article/', views.randomArticle, name="randomArticle"),
    # path('wall/', views.wall, name="wall"),
    path('hot-topics/', views.HotTopics.as_view(), name="hotTopics"),
    path('forum/', views.EntryList.as_view(), name="allEntries"),
    path('error/', views.underconstruction, name="underConstruction"),
    path('contact/', views.contact, name="contact"),
    path('country/<str:url_name>', views.country, name="country"),
    path('category/<str:url_name>', views.category),
    path('tag/<str:url_name>', views.tag),
    path('post/<str:url_name>', views.post, name="post"),
    path('entry/<str:pkey>', views.entryDetail, name="entry"),
    path('start-entry/', views.startEntry, name="start-entry"),



    path('profile/<str:pkey>', views.profile, name="profile"),
    path('bookmarked/<str:id>', views.bookmarked, name="bookmarked"),
    path('settings/<str:pkey>', views.settings, name="settings"),
    path('send-change-email/<str:pkey>', views.sendChangeEmailCode, name="sendChangeEmailCode"),
    path('send-refresh-mail-form/', views.sendChangeEmailRefreshPage, name="sendChangeEmailRefreshPage"),
    path('send-change-password/<str:pkey>/', views.sendChangePasswordCode, name="sendChangePasswordCode"),
    # Change Password
    path('change-password/<str:pkey>/',auth_views.PasswordChangeView.as_view(template_name='dj-change-password.html',success_url = '/'),name='change_password'),





    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    
    path('registration/', views.registerPage, name="registerUser"),
    path('login/', views.loginPage, name='loginUser'),
    path('logout/', views.logoutUser, name="logoutUser"),



######  POLICIES ######
    path('privacy-policy/', views.privacyPolicy, name="privacy-policy"),
    path('user-agreement-policy/', views.userAgreementPolicy, name="user-agreement-policy"),
    path('content-policy/', views.contentPolicy, name="content-policy"),
    path('cookie-policy/', views.cookiePolicy, name="cookie-policy"),
######  POLICIES ######

    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),  #add the robots.txt file
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

htmx_urlpatterns = [
    path('search-content/', views.search_content, name="search-content"),
    path('search-content_wall/', views.search_content_wall, name="search-content-wall"),
    path('post/<str:url_name>/add-to-favorites/', views.addToFavorites, name="add-to-favorites"),
    path('post/<str:url_name>/remove-from-favorites/', views.removeFromFavorites, name="remove-from-favorites"),
    
]

urlpatterns += htmx_urlpatterns