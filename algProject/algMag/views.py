from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token, rotate_token

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from algMag import models

"""算法列表"""


def alg_list(request):
    data_list = models.AlgInfo.objects.all()
    return render(request, 'algInfo.html', {'data_list': data_list})


"""参数列表"""


def parm_list(request, nid):
    data_list = models.PramInfo.objects.filter(algorithm_id=nid)
    return render(request, 'pramInfo.html', {'data_list': data_list, 'nid': nid})


"""插入参数"""


@csrf_exempt
def pram_insert(request, nid):
    if request.method == 'GET':
        return render(request, 'pramInsert.html')
    name = request.POST.get("name")
    type = request.POST.get("type")
    des = request.POST.get("des")
    val = request.POST.get("val")

    models.PramInfo.objects.create(parm_name=name, type=type, description=des, value=val, algorithm_id=nid)
    return redirect(f'/algMag/pram/{nid}/list/', {'nid': nid})


"""插入算法"""


@csrf_exempt
def alg_insert(request):
    if request.method == 'GET':
        return render(request, 'algInsert.html')
    name = request.POST.get("name")
    des = request.POST.get("des")

    models.AlgInfo.objects.create(alg_name=name, description=des)
    return redirect('/algMag/alg/list/')


"""删除算法"""


def alg_delect(request):
    nid = request.GET.get("nid")
    models.AlgInfo.objects.filter(id=nid).delete()

    return redirect('/algMag/alg/list/')

"""删除参数"""


def pram_delect(request):
    nid = request.GET.get("nid")
    models.PramInfo.objects.filter(id=nid).delete()

    return redirect('/algMag/pram/list/')


def alg_update(request, nid):
    if request.method == 'GET':
        data_list = models.AlgInfo.objects.filter(id=nid).first()
        return render(request, 'algUpdate.html', {'data_list': data_list})
    name = request.POST.get("name")
    des = request.POST.get("des")

    models.AlgInfo.objects.filter(id=nid).update(alg_name=name, description=des)

    return redirect('/algMag/alg/list/', {'nid': nid})


def pram_update(request, nid):
    if request.method == 'GET':
        data_list = models.PramInfo.objects.filter(id=nid).first()
        return render(request, 'pramUpdate.html', {'data_list': data_list})
    name = request.POST.get("name")
    type = request.POST.get("type")
    des = request.POST.get("des")
    val = request.POST.get("val")
    models.PramInfo.objects.filter(id=nid).update(parm_name=name, type=type, description=des, value=val)
    list = models.PramInfo.objects.filter(id=nid).first()
    fId = list.algorithm_id

    return redirect(f'/algMag/pram/{fId}/list/')
