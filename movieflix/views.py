from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
from movieflix.forms import UserForm, UserProfileForm
def index(request):
    return HttpResponse('Hello')

# Returns personal detail page
def profile(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

def watchlist(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

def mycomments(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

def detail(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

#
# def login(request):
#     context_dict = {}
#     return render(request, 'profile.html', context=context_dict)

# Returns to the front page when loging out
def logout(request):
    return render(request, '<index file>')

# 这里是登陆函数
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect(reverse('rango:index'))
#             else:
#                 return HttpResponse("Your Rango account is disabled.")
#         else:
#             print(f"Invalid login details: {username}, {password}")
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render(request, 'rango/login.html')

# 这里是注册函数
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})