from django.shortcuts import render, redirect
from django.http import HttpResponse
from rbac.models import UserInfo, Role, Permission
from rbac.mymethod import get_roles_by_user_id
import datetime


# Create your views here.

def checkLogin(func):
    def warpper(request, *args, **kwargs):
        if request.session.get('is_login'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/login')

    return warpper


@checkLogin
def index(request):
    id = request.session.get('user_id')
    user = UserInfo.objects.get(ID=id)
    request.session.set_expiry(30)
    if user.ID == 1:
        data = {
            'username': user.UserName,
            'realname': user.RealName,
            'userlist': UserInfo.objects.all(),
            'rolelist': Role.objects.all(),
            'perlist': Permission.objects.all(),
            'isAdmin': user.ID == 1
        }
    else:
        data = {
            'username': user.UserName,
            'realname': user.RealName,
            'rolelist': get_roles_by_user_id(user_id=user.ID),
            'isAdmin': user.ID == 1
        }
    return render(request, 'include.html', data)

# @checkLogin
# def default(request):
#     id = request.session.get('user_id')
#     user = UserInfo.objects.get(ID=id)
#     request.session.set_expiry(1)
#     if user.ID == 1:
#         data = {
#             'username': user.UserName,
#             'realname': user.RealName,
#             'userlist': UserInfo.objects.all(),
#             'rolelist': Role.objects.all(),
#             'perlist': Permission.objects.all(),
#             'isAdmin': user.ID == 1
#         }
#     else:
#         data = {
#             'username': user.UserName,
#             'realname': user.RealName,
#             'rolelist': get_roles_by_user_id(user_id=user.ID),
#             'isAdmin': user.ID == 1
#         }
#     return render(request, 'include.html', data)


def login(request):
    if request.method == 'POST':
        params = request.POST
        name = params.get('username')
        password = params.get('password')
        user = UserInfo.objects.filter(UserName=name, PassWord=password)
        if user:
            request.session['is_login'] = True
            request.session['user_id'] = user[0].ID
            # request.session['username'] = user[0].UserName
            return redirect("/index")
        else:
            # return HttpResponse("<h1 style='margin-top:200px;text-align:center'>用户名或密码错误！<h1>")
            return redirect("/")
    else:
        if request.session.get('is_login'):
            return redirect('/index')
        return render(request, 'login.html')


@checkLogin
def logout(request):
    id = request.session.get('user_id')
    user = UserInfo.objects.get(ID=id)
    user.LastLogin = datetime.datetime.now()
    user.save()
    request.session.clear()
    return redirect('/login')


@checkLogin
def userinfo(request):
    id = request.session.get('user_id')
    userinfo = UserInfo.objects.get(ID=id)
    data = {
        'userinfo': userinfo
    }
    return render(request, 'userinfo.html', data)


@checkLogin
def userlist(request):
    userlist = UserInfo.objects.all()
    return render(request, 'userlist.html', {
        'isAdmin': True,
        'userlist': userlist
    })

@checkLogin
def myperssion(request):
    if request.session.get('user_id') == 1:
        data = {'isAdmin':True}
    return render(request, 'permission.html', data)


def safe_set(request):
    return render(request, 'safe_set.html')


def role_list(request):
    roles = Role.objects.all()
    role = {
        'roles': roles
    }
    return render(request, 'role.html', role)


def per_list(request):
    permission = Permission.objects.all()
    perdata = {
        'permissions': permission
    }
    return render(request, 'permission.html', perdata)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@checkLogin
def delete(request, id):
    user_id = int(id)
    if user_id != 1:
        # return {"msg": "删除成功！"}
        # UserInfo.objects.get(ID=user_id).delete()
        return HttpResponse("删除成功！")
    else:
        return HttpResponse("管理员无法删除！")
