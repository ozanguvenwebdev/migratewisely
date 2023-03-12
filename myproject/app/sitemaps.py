from django.contrib.sitemaps import Sitemap
from .models import Content, Country, Tag, Category
from django.urls import reverse

class ContentSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Content.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.create_date
        
    def location(self,obj):
        return '/post/%s' % (obj.url_name)

class CountrySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return Country.objects.filter(status=True)

    # def lastmod(self, obj):
    #     return obj.create_date
        
    def location(self,obj):
        return '/country/%s' % (obj.url_name)

class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Tag.objects.filter(status=True)

    # def lastmod(self, obj):
    #     return obj.create_date
        
    def location(self,obj):
        return '/tag/%s' % (obj.url_name)

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Category.objects.filter(status=True)

    # def lastmod(self, obj):
    #     return obj.create_date
        
    def location(self,obj):
        return '/category/%s' % (obj.url_name)


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return ['app:homepage',]

    def location(self, item):
        return reverse(item)