from django.db import models
from image_optimizer.fields import OptimizedImageField
from ckeditor.fields import RichTextField
import datetime
import time
from datetime import datetime, date, time, timedelta
from django.contrib.auth.models import User
from encrypted_id.models import EncryptedIDModel

# Create your models here.
def return_date_time():
    now = datetime.now() + timedelta(hours=3)
    return now


class Navigation(models.Model):
    
    name              = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık")
    nameEs            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Es")
    nameFr            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Fr")
    nameTr            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Tr")
    nameHi            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Hi")
    nameVi            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Vi")
    nameAr            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Ar")
    nameFa            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Fa")
    nameUr            = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Ur")

    url_name        = models.SlugField(max_length=500, blank=True, help_text='This will be filled automatically', verbose_name='Sayfa Uzantısı')
    status          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Kullan")
    order           = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Sıralama')

    class Meta:
        verbose_name_plural = "Navigasyonlar"
        verbose_name = "Navigasyon"
        ordering = ['order']

    def __str__(self):
        return self.name



class Category(models.Model):

    name          = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı")
    nameEs        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Es")
    nameFr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Fr")
    nameTr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Tr")
    nameHi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Hi")
    nameVi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Vi")
    nameAr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Ar")
    nameFa        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Fa")
    nameUr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kategori Adı Ur")

    description   = models.TextField(blank=True,null=True, verbose_name="Google SEO Description", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionEs = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Es", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionFr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fr", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionTr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Tr", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionHi = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Hi", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionVi = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Vi", help_text="max 160 karakterli bir seo açıklaması")
    descriptionAr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ar", help_text="max 160 karakterli bir seo açıklaması")
    descriptionFa = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fa", help_text="max 160 karakterli bir seo açıklaması")
    descriptionUr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ur", help_text="max 160 karakterli bir seo açıklaması")

    keywords      = models.TextField(blank=True,null=True, verbose_name="Keywords", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsEs    = models.TextField(blank=True,null=True, verbose_name="Keywords Es", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsFr    = models.TextField(blank=True,null=True, verbose_name="Keywords Fr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsTr    = models.TextField(blank=True,null=True, verbose_name="Keywords Tr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsHi    = models.TextField(blank=True,null=True, verbose_name="Keywords Hi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsVi    = models.TextField(blank=True,null=True, verbose_name="Keywords Vi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsAr    = models.TextField(blank=True,null=True, verbose_name="Keywords Ar", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsFa    = models.TextField(blank=True,null=True, verbose_name="Keywords Fa", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsUr    = models.TextField(blank=True,null=True, verbose_name="Keywords Ur", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    
    expl          = RichTextField(null=True,blank=True, verbose_name="Açıklama")
    explEs        = RichTextField(null=True,blank=True, verbose_name="Açıklama Es")
    explFr        = RichTextField(null=True,blank=True, verbose_name="Açıklama Fr")
    explTr        = RichTextField(null=True,blank=True, verbose_name="Açıklama Tr")
    explHi        = RichTextField(null=True,blank=True, verbose_name="Açıklama Hi")
    explVi        = RichTextField(null=True,blank=True, verbose_name="Açıklama Vi")
    explAr        = RichTextField(null=True,blank=True, verbose_name="Açıklama Ar")
    explFa        = RichTextField(null=True,blank=True, verbose_name="Açıklama Fa")
    explUr        = RichTextField(null=True,blank=True, verbose_name="Açıklama Ur")

    url_name    = models.SlugField(max_length=500, blank=True, help_text='This will be filled automatically', verbose_name='Sayfa Uzantısı')
    popular     = models.BooleanField(blank=True, null=True, default=False, verbose_name="Popüler Kategori mi?")
    status      = models.BooleanField(blank=True, null=True, default=True, verbose_name="Kullan")
    
    class Meta:
        verbose_name_plural = "Kategoriler"
        verbose_name = "Kategori"

    def __str__(self):
        return self.name



class Tag(models.Model):

    name          = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı")
    nameEs        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Es")
    nameFr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Fr")
    nameTr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Tr")
    nameHi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Hi")
    nameVi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Vi")
    nameAr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Ar")
    nameFa        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Fa")
    nameUr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Etiket Adı Ur")

    description   = models.TextField(blank=True,null=True, verbose_name="Google SEO Description", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionEs = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Es", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionFr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fr", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionTr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Tr", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionHi = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Hi", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionVi = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Vi", help_text="max 160 karakterli bir seo açıklaması")
    descriptionAr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ar", help_text="max 160 karakterli bir seo açıklaması")
    descriptionFa = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fa", help_text="max 160 karakterli bir seo açıklaması")
    descriptionUr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ur", help_text="max 160 karakterli bir seo açıklaması")

    keywords      = models.TextField(blank=True,null=True, verbose_name="Keywords", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsEs    = models.TextField(blank=True,null=True, verbose_name="Keywords Es", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsFr    = models.TextField(blank=True,null=True, verbose_name="Keywords Fr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsTr    = models.TextField(blank=True,null=True, verbose_name="Keywords Tr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsHi    = models.TextField(blank=True,null=True, verbose_name="Keywords Hi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsVi    = models.TextField(blank=True,null=True, verbose_name="Keywords Vi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsAr    = models.TextField(blank=True,null=True, verbose_name="Keywords Ar", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsFa    = models.TextField(blank=True,null=True, verbose_name="Keywords Fa", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsUr    = models.TextField(blank=True,null=True, verbose_name="Keywords Ur", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    
    url_name    = models.SlugField(max_length=500, blank=True, help_text='This will be filled automatically', verbose_name='Sayfa Uzantısı')
    popular     = models.BooleanField(blank=True, null=True, default=False, verbose_name="Popüler Etiket mi?")
    status      = models.BooleanField(blank=True, null=True, default=True, verbose_name="Kullan")
    
    class Meta:
        verbose_name_plural = "Etiketler"
        verbose_name = "Etiket"

    def __str__(self):
        return self.name


class Continent(models.Model):

    name          = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı")
    nameEs        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Es")
    nameFr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Fr")
    nameTr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Tr")
    nameHi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Hi")
    nameVi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Vi")
    nameAr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Ar")
    nameFa        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Fa")
    nameUr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Kıta Adı Ur")
    order         = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Sıralama')

    class Meta:
        verbose_name_plural = "Kıtalar"
        verbose_name = "Kıta"
        ordering = ["order"]

    def __str__(self):
        return self.name


class Country(models.Model):

    name          = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı")
    nameEs        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Es")
    nameFr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Fr")
    nameTr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Tr")
    nameHi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Hi")
    nameVi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Vi")
    nameAr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Ar")
    nameFa        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Fa")
    nameUr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Ülke Adı Ur")

    expl          = RichTextField(null=True, blank=True, )
    explEs        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Es")
    explFr        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Fr")
    explTr        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Tr")
    explHi        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Hi")
    explVi        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Vi")
    explAr        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Ar")
    explFa        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Fa")
    explUr        = RichTextField(null=True, blank=True, verbose_name="Ülke Adı Ur")

    description   = models.TextField(blank=True,null=True, verbose_name="Google SEO Description", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionEs = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Es", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionFr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fr", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionTr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Tr", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionHi = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Hi", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionVi = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Vi", help_text="max 160 karakterli bir seo açıklaması")
    descriptionAr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ar", help_text="max 160 karakterli bir seo açıklaması")
    descriptionFa = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fa", help_text="max 160 karakterli bir seo açıklaması")
    descriptionUr = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ur", help_text="max 160 karakterli bir seo açıklaması")

    keywords      = models.TextField(blank=True,null=True, verbose_name="Keywords", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsEs    = models.TextField(blank=True,null=True, verbose_name="Keywords Es", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsFr    = models.TextField(blank=True,null=True, verbose_name="Keywords Fr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsTr    = models.TextField(blank=True,null=True, verbose_name="Keywords Tr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsHi    = models.TextField(blank=True,null=True, verbose_name="Keywords Hi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsVi    = models.TextField(blank=True,null=True, verbose_name="Keywords Vi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsAr    = models.TextField(blank=True,null=True, verbose_name="Keywords Ar", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsFa    = models.TextField(blank=True,null=True, verbose_name="Keywords Fa", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")
    keywordsUr    = models.TextField(blank=True,null=True, verbose_name="Keywords Ur", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")

    continent   = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True)
    flag        = OptimizedImageField(blank=True,null=True,upload_to="blogs/",optimized_image_output_size=(200, 200),optimized_image_resize_method='cover',verbose_name="Ülke bayrağı'",help_text="kare")
    url_name    = models.SlugField(max_length=500, blank=True, help_text='This will be filled automatically', verbose_name='Sayfa Uzantısı')
    popular     = models.BooleanField(blank=True, null=True, default=False, verbose_name="Popüler Ülke mi?")
    status      = models.BooleanField(blank=True, null=True, default=True, verbose_name="Kullan")
    
    class Meta:
        verbose_name_plural = "Ülkeler"
        verbose_name = "Ülke"
        ordering = ["name"]

    def __str__(self):
        return self.name







class Content(models.Model):
    
    header          = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık")
    headerEs        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Es")
    headerFr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Fr")
    headerTr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Tr")
    headerHi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Hi")
    headerVi        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Vi")
    headerAr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Ar")
    headerFa        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Fa")
    headerUr        = models.CharField(null=True, blank=True, max_length=500, verbose_name="Başlık Ur")

    short_expl        = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama")
    short_explEs      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Es")
    short_explFr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Fr")
    short_explTr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Tr")
    short_explHi      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Hi")
    short_explVi      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Vi")
    short_explAr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Ar")
    short_explFa      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Fa")
    short_explUr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Ur")

    description       = models.TextField(blank=True,null=True, verbose_name="Google SEO Description", help_text="max 160 karakterli bir seo açıklaması")  
    descriptionEs     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Es", help_text="max 160 karakterli bir seo açıklaması Es")  
    descriptionFr     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fr", help_text="max 160 karakterli bir seo açıklaması Fr")  
    descriptionTr     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Tr", help_text="max 160 karakterli bir seo açıklaması Tr")  
    descriptionHi     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Hi", help_text="max 160 karakterli bir seo açıklaması Hi")  
    descriptionVi     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Vi", help_text="max 160 karakterli bir seo açıklaması Vi")  
    descriptionAr     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ar", help_text="max 160 karakterli bir seo açıklaması Ar")  
    descriptionFa     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Fa", help_text="max 160 karakterli bir seo açıklaması Fa")  
    descriptionUr     = models.TextField(blank=True,null=True, verbose_name="Google SEO Description Ur", help_text="max 160 karakterli bir seo açıklaması Ur")  

    keywords          = models.TextField(blank=True,null=True, verbose_name="Keywords", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın")  
    keywordsEs        = models.TextField(blank=True,null=True, verbose_name="Keywords Es", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Es")  
    keywordsFr        = models.TextField(blank=True,null=True, verbose_name="Keywords Fr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Fr")  
    keywordsTr        = models.TextField(blank=True,null=True, verbose_name="Keywords Tr", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Tr")  
    keywordsHi        = models.TextField(blank=True,null=True, verbose_name="Keywords Hi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Hi")  
    keywordsVi        = models.TextField(blank=True,null=True, verbose_name="Keywords Vi", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Vi")  
    keywordsAr        = models.TextField(blank=True,null=True, verbose_name="Keywords Ar", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Ar")  
    keywordsFa        = models.TextField(blank=True,null=True, verbose_name="Keywords Fa", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Fa")  
    keywordsUr        = models.TextField(blank=True,null=True, verbose_name="Keywords Ur", help_text="5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Ur")  
    
    expl              = RichTextField(null=True,blank=True)
    explEs            = RichTextField(null=True,blank=True, verbose_name="Keywords Es",)
    explFr            = RichTextField(null=True,blank=True, verbose_name="Keywords Fr",)
    explTr            = RichTextField(null=True,blank=True, verbose_name="Keywords Tr",)
    explHi            = RichTextField(null=True,blank=True, verbose_name="Keywords Hi",)
    explVi            = RichTextField(null=True,blank=True, verbose_name="Keywords Vi",)
    explAr            = RichTextField(null=True,blank=True, verbose_name="Keywords Ar",)
    explFa            = RichTextField(null=True,blank=True, verbose_name="Keywords Fa",)
    explUr            = RichTextField(null=True,blank=True, verbose_name="Keywords Ur",)

    url_name        = models.SlugField(max_length=500, blank=True, help_text='This will be filled automatically', verbose_name='Sayfa Uzantısı')
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Kullan")
    detail_image    = OptimizedImageField(blank=True,null=True,upload_to="blogs/",optimized_image_output_size=(1200, 662),optimized_image_resize_method='cover',verbose_name="Detay Sayfa Resmi'",help_text="1200x662")
    homepage_image  = OptimizedImageField(blank=True,null=True,upload_to="blogs/",optimized_image_output_size=(550, 465),optimized_image_resize_method='cover',verbose_name="Detay Sayfa Resmi'",help_text="1200x662")
    tag             = models.ManyToManyField(Tag, verbose_name="Alakalı Etiketler", blank=True)
    country         = models.ForeignKey(Country, verbose_name="Alakalı Ülke", blank=True,null=True, on_delete=models.CASCADE,)
    category        = models.ManyToManyField(Category, verbose_name="Alakalı Kategoriler", blank=True)
    create_date     = models.DateField(default=return_date_time, verbose_name='Tarih')
    order           = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Sıralama')

    class Meta:
        verbose_name_plural = "Yazılar"
        verbose_name = "Yazı"
        ordering = ['-order']

    def __str__(self):
        return self.header



class QuickInfo(models.Model):

    short_expl        = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama")
    short_explEs      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Es")
    short_explFr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Fr")
    short_explTr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Tr")
    short_explHi      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Hi")
    short_explVi      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Vi")
    short_explAr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Ar")
    short_explFa      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Fa")
    short_explUr      = models.TextField(blank=True,null=True, verbose_name="Kısa Açıklama Ur")
    
    expl              = RichTextField(null=True, verbose_name="Kısa Açıklama")
    explEs            = RichTextField(null=True, verbose_name="Kısa Açıklama Es")
    explFr            = RichTextField(null=True, verbose_name="Kısa Açıklama Fr")
    explTr            = RichTextField(null=True, verbose_name="Kısa Açıklama Tr")
    explHi            = RichTextField(null=True, verbose_name="Kısa Açıklama Hi")
    explVi            = RichTextField(null=True, verbose_name="Kısa Açıklama Vi")
    
    active            = models.BooleanField(blank=True, null=True, default=True, verbose_name="Kullan")

    class Meta:
        verbose_name_plural = "Anasayfa Kutular"
        verbose_name = "Anasayfa Kutu"

    def __int__(self):
        return self.id




class FooterSubscribe(models.Model):
    email           = models.EmailField(blank=True,null=True, verbose_name="E-Mail")
    ip              = models.CharField(max_length=200, null=True, blank=False, verbose_name='IP')
    create_date     = models.DateField(default=return_date_time, verbose_name='Tarih')
    class Meta:
        verbose_name_plural = "Footer Subscribes"
        verbose_name = "Footer Subscribe"
    def __int__(self):
        return self.id


class FooterMessage(models.Model):
    message         = models.TextField(blank=True,null=True, verbose_name="Message")
    ip              = models.CharField(max_length=200, null=True, blank=False, verbose_name='IP')
    create_date     = models.DateField(default=return_date_time, verbose_name='Tarih')
    class Meta:
        verbose_name_plural = "Footer Messages"
        verbose_name = "Footer Message"
    def __int__(self):
        return self.id


class Contact(models.Model):
    note         = models.TextField(blank=True,null=True, verbose_name="Message")
    ip           = models.CharField(max_length=200, null=True, blank=False, verbose_name='IP')
    email        = models.CharField(max_length=200, null=True, blank=False, verbose_name='Email')
    name         = models.CharField(max_length=200, null=True, blank=False, verbose_name='İsim')
    create_date  = models.DateField(default=return_date_time, verbose_name='Tarih')
    
    class Meta:
        verbose_name_plural = "Contact Records"
        verbose_name = "Contact Record"
    def __int__(self):
        return self.name












class Profile(models.Model):

    user            = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True,verbose_name="User Model", related_name='access_profile')
    name            = models.CharField(max_length=200, null=True, blank=True,verbose_name="Profile Name")
    surname         = models.CharField(max_length=200, null=True, blank=True,verbose_name="Profile Surname")
    description     = models.CharField(max_length=150, null=True, blank=True,verbose_name="Profile Description")
    profile_pic     = OptimizedImageField(blank=True,null=True,upload_to="profilephotos/",optimized_image_output_size=(600, 600),optimized_image_resize_method='cover',verbose_name="Profil Resmi'",help_text="600x600")
    default_pic     = OptimizedImageField(blank=True,null=True,default="/static/assets/images/defaultprofile.jpg",optimized_image_output_size=(600, 600),optimized_image_resize_method='cover',verbose_name="Profil Resmi'",help_text="600x600")
    email           = models.EmailField(max_length=200, null=True, blank=False)
    date_created    = models.DateTimeField(default=return_date_time, verbose_name='Profile Creation Date',null=True, blank=True,)
    encrypted_id    = models.ForeignKey('Foo', related_name="foo_of_profile" ,on_delete=models.CASCADE, null=True)
    notified        = models.BooleanField(blank=True, null=True, default=False, verbose_name="Subscribed?")
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Active?")

    def __str__(self):
        return self.user.username




class Entry(models.Model):

    heading         = models.CharField(max_length=200,blank=True,null=True, verbose_name="Topic Heading")
    message         = models.TextField(blank=True,null=True, verbose_name="Content")
    profile         = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    country         = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(default=return_date_time, verbose_name='Comment Date',null=True, blank=True,)
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Active?")
    
    class Meta:
        verbose_name_plural = "Entries"
        verbose_name = "Entry"
        ordering=["-date_created"]
        
    def __str__(self):
        return self.heading



class HotTopic(models.Model):

    heading         = models.CharField(max_length=200,blank=True,null=True, verbose_name="Topic Heading")
    message         = RichTextField(null=True,blank=True)
    date_created    = models.DateTimeField(default=return_date_time, verbose_name='Date',null=True, blank=True,)
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Active?")
    
    class Meta:
        verbose_name_plural = "Hot Topics"
        verbose_name = "Hot Topic"
        ordering=["-date_created"]
        
    def __str__(self):
        return self.heading





class Comment(models.Model):

    message         = models.TextField(blank=True,null=True, verbose_name="Comment")
    profile         = models.ForeignKey(Profile,related_name="profile_of_comment", on_delete=models.CASCADE, null=True)
    entry           = models.ForeignKey(Entry,related_name="entry_of_comment", on_delete=models.CASCADE, null=True, blank=True)
    comment         = models.ForeignKey('Comment',related_name="comment_of_comment", on_delete=models.CASCADE, null=True, blank=True)
    country         = models.ForeignKey(Country,related_name="country_of_comment", on_delete=models.CASCADE, null=True, blank=True)
    post            = models.ForeignKey(Content,related_name="content_of_comment", on_delete=models.CASCADE, null=True, blank=True)
    category        = models.ForeignKey(Category,related_name="category_of_comment", on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(default=return_date_time, verbose_name='Comment Date',null=True, blank=True,)
    secondComment   = models.BooleanField(blank=True, null=True, default=False, verbose_name="Second Comment")
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Active?")

    class Meta:
        ordering=["-date_created"]
    def __str__(self):
        return self.message



class Foo(EncryptedIDModel):
    text = models.TextField()
    def __str__(self):
        return self.text
    


class ExpireCode(models.Model):
    profile         = models.ForeignKey(Profile,related_name="profile_of_expirecode", on_delete=models.CASCADE, null=True)
    date_created    = models.DateTimeField(default=return_date_time, verbose_name='Code Creation Date',null=True, blank=True,)
    encrypted_id    = models.ForeignKey('Foo', related_name="foo_of_expirecode" ,on_delete=models.CASCADE, null=True)
    expired         = models.BooleanField(blank=True, null=True, default=False, verbose_name="Expired")

    class Meta:
        ordering=["-date_created"]

    def __str__(self):
        return str(self.encrypted_id.text)



class Favorite(models.Model):
    post = models.ForeignKey(Content,related_name="post_of_favorite", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,related_name="user_of_favorite", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id)




















class Policy(models.Model):

    heading         = models.CharField(max_length=200,blank=True,null=True, verbose_name="İsim")
    text            = RichTextField(null=True,blank=True)
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Active?")
    
    class Meta:
        verbose_name_plural = "Sözleşme"
        verbose_name = "Sözleşmeler"
        
    def __str__(self):
        return self.heading