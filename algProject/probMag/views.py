from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token, rotate_token

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from probMag import models


@csrf_exempt
def insert(request):
    """  添加数据 """
    if request.method == 'GET':
        return render(request, 'probInsert.html')
    name = request.POST.get("name")
    des = request.POST.get("des")
    dim = request.POST.get("dim")
    obj = request.POST.get("obj")
    val = request.POST.get("val")
    weight = request.POST.get("weight")
    models.ProbInfo.objects.create(prob_name=name, description=des, dimensions=dim, objectives=obj, value_vector=val,
                                   weight_matrix=weight)
    return redirect('/probMag/prob/list/')


def delect(request):
    """"删除数据"""
    nid = request.GET.get("nid")
    models.ProbInfo.objects.filter(id=nid).delete()
    return redirect('/probMag/prob/list/')


def prob_list(request):
    """" 查询数据 """
    data_list = models.ProbInfo.objects.all()
    return render(request, 'probInfo.html', {'data_list': data_list})


"""修改数据"""


def edit(request, nid):
    if request.method == 'GET':
        row_object = models.ProbInfo.objects.filter(id=nid).first()
        return render(request, 'probEdit.html', {'row_object': row_object})
    name = request.POST.get("name")
    des = request.POST.get("des")
    dim = request.POST.get("dim")
    obj = request.POST.get("obj")
    val = request.POST.get("val")
    weight = request.POST.get("weight")
    models.ProbInfo.objects.filter(id=nid).update(prob_name=name, description=des, dimensions=dim, objectives=obj,
                                                  value_vector=val,
                                                  weight_matrix=weight)

    return redirect('/probMag/prob/list/')
