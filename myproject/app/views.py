from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from django.core import serializers
import math
from .decorators import unauthenticated_user,allowed_users
from .forms import CreateUserForm
from .tools import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.views.generic import ListView
from django.db.models import Q
import random
from django.core.files import File
from django.core.files.storage import FileSystemStorage
# Create your views here.
import datetime, pytz


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip





def homepage(request):
    posts = Content.objects.filter(active=True,)[::-1]
    last_posts = Content.objects.filter(active=True,)[::-1][:3]
    categories = Category.objects.filter(status=True,)
    tags = Tag.objects.filter(status=True,)
    quick_infos = QuickInfo.objects.filter(active=True)
    ip = get_client_ip(request)

    if request.method=="POST" and 'footerSubscribe' in request.POST:
        try:
            email = request.POST.get("email")
            FooterSubscribe.objects.create(email=email,ip=ip)
            messages.success(request, 'You have been subscribed successfully.')
        except:
            messages.error(request, 'Invalid post request.')

    if request.method=="POST" and 'footerMessage' in request.POST:
        try:
            message = request.POST.get("message")
            FooterMessage.objects.create(message=message, ip=ip)
            messages.success(request, 'You have been subscribed successfully.')
        except:
            messages.error(request, 'Invalid post request.')

    context = {'posts': posts,'last_posts': last_posts,'categories': categories,'quick_infos': quick_infos,'tags':tags,}
    return render(request, 'index.html', context)


def search_content(request):
    search_text = request.POST.get("search")
    results = Content.objects.filter(Q(header__icontains=search_text) | Q(expl__icontains=search_text) | Q(country__name__icontains=search_text))
    return render(request,'tags/search-results.html',{'results':results,})


def randomArticle(request):
    articles = Content.objects.filter(active=True)
    randomArticleUrl = random.choice(articles).url_name
    messages.success(request, "You've been redirected successfully...")
    return redirect('app:post', url_name=randomArticleUrl)
    






def country(request,url_name):
    country = Country.objects.get(status=True,url_name=url_name)
    relatedComments = Comment.objects.filter(active=True,country=country,secondComment=False,)
    secondComments = Comment.objects.filter(active=True,)
    posts = Content.objects.filter(active=True,country=country)[::-1]
    last_posts = Content.objects.filter(active=True,)[::-1][:3]
    categories = Category.objects.filter(status=True,)
    tags = Tag.objects.filter(status=True)
    if request.method == "POST" and 'countryPageComment' in request.POST:
        message = request.POST.get('message')
        newComment = Comment.objects.create(message=message,country=country,profile=request.user.access_profile)
        newComment.save()
        messages.success(request, 'Comment has been saved successfully.')
    if request.method == "POST" and 'countryPageSecondComment' in request.POST:
        message = request.POST.get('message')
        commentId = request.POST.get('specificCommentId')
        specificComment = Comment.objects.get(id=commentId)
        newSecondComment = Comment.objects.create(message=message,country=country,profile=request.user.access_profile,secondComment=True,comment=specificComment)
        messages.success(request, 'Comment has been saved successfully.')
    return render(request, 'country.html', {'secondComments':secondComments,'relatedComments':relatedComments,'country':country,'posts': posts,'last_posts': last_posts,'categories': categories,'tags': tags,})


def tag(request,url_name):
    tag = Tag.objects.get(status=True,url_name=url_name)
    last_posts = Content.objects.filter(active=True,)[::-1][:3]
    categories = Category.objects.filter(status=True,)
    tags = Tag.objects.filter(status=True)
    all_posts = Content.objects.filter(active=True)
    posts_of_tag = []
    for post in all_posts:
        tags_of_post = [ each_tag for each_tag in post.tag.all() ]
        if tag in tags_of_post:
            posts_of_tag.append(post)
    return render(request, 'tag.html', {'tag':tag,'all_posts': all_posts,'last_posts': last_posts,'categories': categories,'tags': tags,'posts_of_tag':posts_of_tag,})


def category(request,url_name):
    category = Category.objects.get(status=True,url_name=url_name)
    relatedComments = Comment.objects.filter(active=True,category=category,secondComment=False,)
    secondComments = Comment.objects.filter(active=True,)
    posts = Content.objects.filter(active=True,category=category)[::-1]
    last_posts = Content.objects.filter(active=True,)[::-1][:3]
    categories = Category.objects.filter(status=True,)
    tags = Tag.objects.filter(status=True)
    if request.method == "POST" and 'categoryPageComment' in request.POST:
        message = request.POST.get('message')
        newComment = Comment.objects.create(message=message,category=category,profile=request.user.access_profile)
        newComment.save()
        messages.success(request, 'Comment has been saved successfully.')
    if request.method == "POST" and 'categoryPageSecondComment' in request.POST:
        message = request.POST.get('message')
        commentId = request.POST.get('specificCommentId')
        specificComment = Comment.objects.get(id=commentId)
        newSecondComment = Comment.objects.create(message=message,category=category,profile=request.user.access_profile,secondComment=True,comment=specificComment)
        messages.success(request, 'Comment has been saved successfully.')
    return render(request, 'category.html', {'secondComments':secondComments,'relatedComments':relatedComments,'category':category,'posts': posts,'last_posts': last_posts,'categories': categories,'tags': tags,})



def post(request,url_name):
    post = Content.objects.get(url_name=url_name)
    try:
        favorites = Favorite.objects.filter(user=request.user, post=post)
    except:
        favorites = None
    tags_of_post = [ each_tag for each_tag in post.tag.all() ]
    relatedComments = Comment.objects.filter(active=True,post=post,secondComment=False,)
    secondComments = Comment.objects.filter(active=True,)
    if request.method == "POST" and 'postPageComment' in request.POST:
        message = request.POST.get('message')
        newComment = Comment.objects.create(message=message,post=post,profile=request.user.access_profile)
        newComment.save()
        messages.success(request, 'Comment has been saved successfully.')
    if request.method == "POST" and 'postPageSecondComment' in request.POST:
        message = request.POST.get('message')
        commentId = request.POST.get('specificCommentId')
        specificComment = Comment.objects.get(id=commentId)
        newSecondComment = Comment.objects.create(message=message,post=post,profile=request.user.access_profile,secondComment=True,comment=specificComment)
        messages.success(request, 'Comment has been saved successfully.')
    return render(request, 'post.html', {'post':post,'tags_of_post':tags_of_post,'relatedComments':relatedComments,'secondComments':secondComments,'favorites':favorites,})

def addToFavorites(request, url_name):
    post = Content.objects.get(url_name=url_name)
    newFavObject = Favorite.objects.create(post=post,user=request.user)
    return render(request, 'favorite/addedToFavs.html', {'post':post,})

def removeFromFavorites(request, url_name):
    post = Content.objects.get(url_name=url_name)
    favObjects = Favorite.objects.filter(post=post,user=request.user)
    favObjects.delete()
    return render(request, 'favorite/removedFromFavs.html', {'post':post,})






def profile(request,pkey):
    fooObject=Foo.objects.get_by_ekey(pkey)
    profile = Profile.objects.get(encrypted_id=fooObject)
    profileComments = Comment.objects.filter(profile=profile,active=True)
    profileEntries = Entry.objects.filter(profile=profile, active=True)

    if request.method == "POST" and 'deleteEntry' in request.POST:
        entryId = int(request.POST.get("deleteEntry"))
        deactivateEntry = Entry.objects.get(id=entryId)
        deactivateEntry.active = False
        deactivateEntry.save()
        relatedComments = Comment.objects.filter(entry=deactivateEntry)
        for comment in relatedComments:
            comment.active = False
            comment.save()
        relatedSecondComments = Comment.objects.filter(comment__entry=deactivateEntry)
        for comment in relatedSecondComments:
            comment.active = False
            comment.save()
        messages.success(request, 'Your entry has been deleted successfully.')

    if request.method == "POST" and 'deleteComment' in request.POST:
        commentId = int(request.POST.get("deleteComment"))
        deactivateComment = Comment.objects.get(id=commentId)
        deactivateComment.active = False
        deactivateComment.save()
        relatedSecondComments = Comment.objects.filter(comment=deactivateComment)
        for comment in relatedSecondComments:
            comment.active = False
            comment.save()
        messages.success(request, 'Your comment has been deleted successfully.')

    if request.method == 'POST' and 'updateProfile' in request.POST:
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        try:
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save('documents/'+ file.name, file)
        except:
            try:
                filename = profile.profile_pic
            except:
                filename = None
        profile.name = name
        profile.surname = surname
        profile.profile_pic = filename
        profile.save()
    return render(request, 'profile.html', {'profile':profile,'profileComments':profileComments,'profileEntries':profileEntries,})



def settings(request,pkey):
    fooObject=Foo.objects.get_by_ekey(pkey)
    profile = Profile.objects.get(encrypted_id=fooObject)
    if request.method == "POST" and "updateSettings" in request.POST:
        username = request.POST.get("username")
        try:
            alreadyUser = User.objects.get(username=username)
            if alreadyUser == profile.user:
                pass
            else:
                messages.error(request, 'This username has been already used.')
        except:
            user = profile.user
            user.username = username
            user.save()
            messages.success(request, 'Username has been changed successfully.')

    return render(request, 'settings.html', {'profile':profile,})


from datetime import datetime
def return_date_time():
    now = datetime.now() + timedelta(hours=3)
    return now

def sendChangeEmailCode(request,pkey):
    requestUser = request.user
    fooObject = Foo.objects.get_by_ekey(pkey)
    profile = Profile.objects.get(encrypted_id=fooObject)
    user = profile.user
    if requestUser == profile.user:
        expireCodes = ExpireCode.objects.filter(profile=profile,)
        uniqueChangeEmailCode = str(requestUser.username)+str(return_date_time)                     #UNIQUE CODE
        newFooObject = Foo.objects.create(text=uniqueChangeEmailCode)                               #UNIQUE ENCRYPTED CODE
        uniqueExpireCode = ExpireCode.objects.create(profile=profile,encrypted_id=newFooObject,)
        encryptedString = uniqueExpireCode.encrypted_id.ekey
        sendChangeEmail(profile.id,encryptedString)
        return render(request, 'change-email.html', {'profile':profile,})
    else:
        messages.info(request, 'You are not allowed to see that page.')
        return redirect('/')

def sendChangeEmailRefreshPage(request):
    if request.method == "POST" and "updateEmail" in request.POST:
        newEmail = request.POST.get("new-email")
        newCode = request.POST.get("email-code")
        profile_id = request.POST.get("profile_id")
        profile = Profile.objects.get(id=profile_id)
        profileEkey = Foo.objects.get_by_ekey(profile.encrypted_id.ekey)
        neededExpireCode = ExpireCode.objects.filter(profile=profile,)[0]
        neededExpireCodeHour = neededExpireCode.date_created
        neededExpireCodePlusOneHour = neededExpireCode.date_created + timedelta(hours=24)
        now = pytz.utc.localize(return_date_time())
        try:
            alreadyEmail = User.objects.get(email=newEmail)
            messages.error(request, 'This e-mail has been already exist.')
            return redirect('app:settings', pkey=profileEkey.ekey)
        except:
            if newCode == neededExpireCode.encrypted_id.ekey:
                if neededExpireCodePlusOneHour > now:
                    user = profile.user
                    user.email = newEmail
                    profile.email = newEmail
                    profile.save()
                    user.save()
                    messages.success(request, 'Your e-mail has been changed successfully.')
                    return redirect('app:settings', pkey=profileEkey.ekey)
                else:
                    messages.error(request, 'This code has been expired.')
                    return redirect('app:settings', pkey=profileEkey.ekey)
            else:
                messages.error(request, 'Invalid code.')
                return redirect('app:settings', pkey=profileEkey.ekey)



def sendChangePasswordCode(request,pkey):
    requestUser = request.user
    fooObject = Foo.objects.get_by_ekey(pkey)
    profile = Profile.objects.get(encrypted_id=fooObject)
    user = profile.user
    profileEkey = Foo.objects.get_by_ekey(profile.encrypted_id.ekey)
    if requestUser == profile.user:
        expireCodes = ExpireCode.objects.filter(profile=profile,)
        uniqueChangePasswordCode = str(requestUser.username)+str(return_date_time)                     #UNIQUE CODE
        newFooObject = Foo.objects.create(text=uniqueChangePasswordCode)                               #UNIQUE ENCRYPTED CODE
        uniqueExpireCode = ExpireCode.objects.create(profile=profile,encrypted_id=newFooObject,)
        encryptedString = uniqueExpireCode.encrypted_id.ekey
        sendChangePassword(profile.id,encryptedString)
        messages.info(request, 'We have sent a link to your e-mail.')
        return redirect('app:settings', pkey=profileEkey.ekey)
    else:
        messages.info(request, 'You are not allowed to see that page.')
        return redirect('/')
    












def entryDetail(request,pkey):
    entry = Entry.objects.get(id=pkey,active=True)
    relatedComments = Comment.objects.filter(active=True,entry=entry,secondComment=False,)
    secondComments = Comment.objects.filter(active=True,)
    entryCommentsCount = Comment.objects.filter(active=True,entry=entry).count()
    if request.method == "POST" and 'entryPageComment' in request.POST:
        message = request.POST.get('message')
        newComment = Comment.objects.create(message=message,entry=entry,profile=request.user.access_profile)
        newComment.save()
        messages.success(request, 'Comment has been saved successfully.')
    if request.method == "POST" and 'entryPageSecondComment' in request.POST:
        message = request.POST.get('message')
        commentId = request.POST.get('specificCommentId')
        specificComment = Comment.objects.get(id=commentId)
        newSecondComment = Comment.objects.create(message=message,entry=entry,profile=request.user.access_profile,secondComment=True,comment=specificComment)
        messages.success(request, 'Comment has been saved successfully.')
    return render(request, 'entry.html', {'entryCommentsCount':entryCommentsCount,'entry':entry,'relatedComments':relatedComments,'secondComments':secondComments,})




class EntryList(ListView):
    template_name = 'allEntries.html'
    model = Entry
    context_object_name = 'entries'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['userGroup'] = self.request.user.groups.all().first()
        return context

    def get_template_names(self):
        if self.request.htmx:
            return 'tags/entry-list.html'
        return 'allEntries.html'


class HotTopics(ListView):
    template_name = 'hotTopics.html'
    model = HotTopic
    context_object_name = 'hotTopics'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['userGroup'] = self.request.user.groups.all().first()
        return context

    def get_template_names(self):
        if self.request.htmx:
            return 'tags/topic-list.html'
        return 'hotTopics.html'




def search_content_wall(request):
    search_text = request.POST.get("search")
    results = Entry.objects.filter(Q(heading__icontains=search_text) | Q(message__icontains=search_text) | Q(country__name__icontains=search_text) | Q(category__name__icontains=search_text), active=True)
    return render(request,'tags/search-results-wall.html',{'results':results,})


@allowed_users(allowed_roles=['member'])
def startEntry(request):
    categories = Category.objects.filter(status=True,)
    countries  = Country.objects.filter(status=True,)
    country_names = [country.name for country in countries]
    category_names = [category.name for category in categories]

    if request.method == "POST":
        heading = request.POST.get('heading')
        message = request.POST.get('message')
        try:
            country = request.POST.get('country')
            if country in country_names:
                pass
            else:
                country = None
        except:
            country = None
        try:
            category = request.POST.get('category')
            if category in category_names:
                pass
            else:
                category = None
        except:
            category = None

        if country == None and category == None:
            newEntry = Entry.objects.create(heading=heading,message=message,profile=request.user.access_profile,country=None,category=None)
        elif country == None and category != None:
            newEntry = Entry.objects.create(heading=heading,message=message,profile=request.user.access_profile,country=None,category=Category.objects.get(name=category))
        elif country != None and category == None:
            newEntry = Entry.objects.create(heading=heading,message=message,profile=request.user.access_profile,country=Country.objects.get(name=country),category=None)
        else:
            newEntry = Entry.objects.create(heading=heading,message=message,profile=request.user.access_profile,country=Country.objects.get(name=country),category=Category.objects.get(name=category))
        messages.success(request, 'Your entry has been shared successfully')
        return redirect('app:allEntries')

    return render(request, 'start-entry.html', {'categories':categories,'countries':countries,})



@allowed_users(allowed_roles=['member'])
def bookmarked(request, id):
    requestUser = User.objects.get(id=id)
    favourites = Favorite.objects.filter(user=requestUser)
    posts = Content.objects.filter(active=True)
    fav_posts = []
    for fav in favourites:
        for post in posts:
            if post == fav.post:
                fav_posts.append(post)
    return render(request, 'bookmarked.html', {'requestUser':requestUser,'fav_posts':fav_posts,})
    









def underconstruction(request):
    context = {}
    return render(request, 'underconstruction.html', context)


def privacyPolicy(request):
    policy = Policy.objects.get(heading="privacy-policy")
    return render(request, 'policies/privacy-policy.html', {'policy':policy,})

def userAgreementPolicy(request):
    policy = Policy.objects.get(heading="user-agreement")
    return render(request, 'policies/user-agreement-policy.html', {'policy':policy,})

def contentPolicy(request):
    policy = Policy.objects.get(heading="content-policy")
    return render(request, 'policies/content-policy.html', {'policy':policy,})

def cookiePolicy(request):
    policy = Policy.objects.get(heading="cookie-policy")
    return render(request, 'policies/cookie-policy.html', {'policy':policy,})


def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        note = request.POST.get("note")
        ip = get_client_ip(request)
        newRecord = Contact.objects.create(email=email,name=name,note=note,ip=ip)
        messages.success(request, 'Your message has been sent succesfully')
        return redirect('/')

    return render(request, 'contact.html', {})












@unauthenticated_user ### NO PERMISSION FOR AUTHENTICATED USER ###
def loginPage(request):
    
    if request.method == "POST" and "loginUser" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request, 'Welcome, '+username)
            return redirect('app:homepage')
        except:
            try:
                usedUsername = User.objects.get(username=username)
                messages.error(request, 'Wrong password')
                return redirect('app:loginUser')
            except:
                messages.error(request, 'No such user')
                return redirect('app:loginUser')

    if request.method == "POST" and "resetPassword" in request.POST:
        email = request.POST.get("email")
        # try:
        user = User.objects.get(email=email)
        userId = user.id
        sendResetPassword(userId)
        # except:
        #     messages.error(request, 'No such user')




    return render(request,'login.html',{})


@unauthenticated_user ### NO PERMISSION FOR AUTHENTICATED USER ###
def registerPage(request):

    if request.method == "POST":
        groupMember = Group.objects.get(name='member') #GET MEMBER GROUP INDEPENDENTLY
        
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        notified = request.POST.get("notified")
        if notified == "notified":
            notified = True
        else:
            notified = False

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect("app:registerUser")
        else:
            try:
                usedUsername = User.objects.get(username=username)
                messages.error(request, 'This username has been already used.')
                return redirect("app:registerUser")
            except:
                try:
                    usedEmail = User.objects.get(email=email)
                    messages.error(request, 'This e-mail has been already used.')
                    return redirect("app:registerUser")
                except:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.groups.add(groupMember)

                    uniqueCode = str(user.username)+str(user.id)    #UNIQUE ENCRYPTED CODE
                    fooObject = Foo.objects.create(text=uniqueCode)
                    
                    profile = Profile.objects.create(user=user,email=email,encrypted_id=fooObject,notified=notified)
                    profile.save()
                    # sendMail(profile.id)
                    messages.success(request, "You've been registered, " +str(user.username)+ ", successfully")
                    login(request,user)
                    return redirect('app:homepage')
    return render(request,'registration.html',{})


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('app:homepage')



















