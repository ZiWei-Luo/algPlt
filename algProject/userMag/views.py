from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token, rotate_token

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from userMag import models

# Create your views here.
"""登录"""


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'password123':
            response_data = {
                'status': 'success',
                'message': 'Login successful',
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'status': 'failure', 'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'status': 'failure', 'message': 'Only POST method is allowed'}, status=405)


"""插入"""


@csrf_exempt
def insert(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    name = request.POST.get("name")
    password = request.POST.get("password")
    role = request.POST.get("role")
    email = request.POST.get("email")
    print('---------------')
    print(name)

    models.UserInfo.objects.create(name=name, password=password, role=role, email=email)

    return redirect('/userMag/select/list/')


"""删除"""


def delect(request):
    nid = request.GET.get("nid")
    models.UserInfo.objects.filter(id=nid).delete()

    return redirect('/userMag/select/list/')


"""查找"""


def select_list(request):
    data_list2 = models.UserInfo.objects.all()
    # for data_list in data_list2:
    #     print(data_list.id,data_list.name,data_list.password,data_list.role,data_list.email)
    return render(request, 'info.html', {'data_list2': data_list2})


"""更新"""


def edit(request, nid):
    if request.method == 'GET':
        row_object = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'edit.html', {'row_object': row_object})
    name = request.POST.get("name")
    password = request.POST.get("password")
    role = request.POST.get("role")
    email = request.POST.get("email")

    models.UserInfo.objects.filter(id=nid).update(name=name, password=password, role=role, email=email)

    return redirect('/userMag/select/list/')
