from django.template import Library
from django import template

register = Library()

from app.models import *


@register.filter(name = 'count_items')
def count_items(id):

    category = Category.objects.get(id=id)
    
    category_related_content    = []  
    for item in Content.objects.filter(active=True,):
        if category in item.category.all():
            category_related_content.append(item)               

    count_content = len(category_related_content)

    return count_content

def SliderTag(context):
    return {}
register.inclusion_tag('tags/slider.html', takes_context=True)(SliderTag)


def RightSideTag(context):

    request     = context['request']
    all_nav     = Navigation.objects.filter(status=True).order_by('order')
    continents  = Continent.objects.all()
    last_posts = Content.objects.filter(active=True,)[::-1][:3]
    countries   = Country.objects.filter(status=True)
    categories  = Category.objects.filter(status=True,)
    tags        = Tag.objects.filter(status=True)

    return {'all_nav': all_nav, 'request':request, 'last_posts':last_posts, 'continents':continents, 'countries': countries, 'categories':categories, 'tags':tags,}

register.inclusion_tag('tags/rightside.html', takes_context=True)(RightSideTag)


def LeftSideTag(context):

    request     = context['request']
    all_nav     = Navigation.objects.filter(status=True).order_by('order')
    last_posts  = Content.objects.filter(active=True,)[::-1][:3]
    categories  = Category.objects.filter(status=True,)
    countries   = Country.objects.filter(status=True,)
    tags        = Tag.objects.filter(status=True)

    return {'all_nav': all_nav, 'request':request, 'last_posts':last_posts,'countries':countries, 'categories': categories,'tags':tags,}

register.inclusion_tag('tags/leftsidewall.html', takes_context=True)(LeftSideTag)



def InnerNavbarTag(context):

    request = context['request']
    all_nav = Navigation.objects.filter(status=True).order_by('order')
    continents  = Continent.objects.all()
    countries   = Country.objects.filter(status=True)
    categories  = Category.objects.filter(status=True,)
    userGroup = None
    try:
        userGroup = request.user.groups.all()[0].name
    except:
        pass
    try:
        favorites = Favorite.objects.filter(user=request.user)
    except:
        favorites = None

    return {'favorites':favorites,'all_nav': all_nav, 'request':request, 'continents':continents, 'countries': countries, 'categories':categories,'userGroup':userGroup,}

register.inclusion_tag('tags/innernavbar.html', takes_context=True)(InnerNavbarTag)


def FooterTag(context):

    request = context['request']
    all_nav = Navigation.objects.filter(status=True).order_by('order')
    popular_categories = Category.objects.filter(status=True,popular=True)
    popular_tags = Tag.objects.filter(status=True,popular=True)
    popular_countries = Country.objects.filter(status=True,popular=True)

    return {'all_nav': all_nav, 'request':request, 'popular_categories':popular_categories, 'popular_tags':popular_tags, 'popular_countries': popular_countries,}

register.inclusion_tag('tags/footer.html', takes_context=True)(FooterTag)












@register.simple_tag
def CategoryEntryAmountTag(id):
    category = Category.objects.get(id=id)
    relatedEntries = Entry.objects.filter(category=category).count()
    return relatedEntries


@register.simple_tag
def NumberOfComments(id):
    numberOfComments = Comment.objects.filter(entry__id=id).count()
    return numberOfComments

