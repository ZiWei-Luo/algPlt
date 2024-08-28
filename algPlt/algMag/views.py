import base64
import importlib
import io
import os

from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from matplotlib import pyplot as plt

from algMag import models

# Create your views here.
"""登录"""


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'password123':
            response_data = {
                'status': 'success',
                'message': 'Login successful',
            }
            return HttpResponse(response_data)
        else:
            return HttpResponse({'status': 'failure', 'message': 'Invalid credentials'}, status=401)

    return HttpResponse({'status': 'failure', 'message': 'Only POST method is allowed'}, status=405)


"""插入"""


@csrf_exempt
def user_insert(request):
    if request.method == 'GET':
        return render(request, 'userInsert.html')
    name = request.POST.get("name")
    password = request.POST.get("password")
    role = request.POST.get("role")
    email = request.POST.get("email")
    print(name)
    models.UserInfo.objects.create(name=name, password=password, role=role, email=email)

    return redirect('/user/list/')


"""删除"""


def user_delect(request):
    nid = request.GET.get("nid")
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


"""查找"""


def user_list(request):
    data_list2 = models.UserInfo.objects.all()
    # for data_list in data_list2:
    #     print(data_list.id,data_list.name,data_list.password,data_list.role,data_list.email)
    return render(request, 'userInfo.html', {'data_list2': data_list2})


"""更新"""


def user_update(request, nid):
    if request.method == 'GET':
        row_object = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'userUpdate.html', {'row_object': row_object})
    name = request.POST.get("name")
    password = request.POST.get("password")
    role = request.POST.get("role")
    email = request.POST.get("email")
    models.UserInfo.objects.filter(id=nid).update(name=name, password=password, role=role, email=email)

    return redirect('/user/list/')


@csrf_exempt
def prob_insert(request):
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
    return redirect('/prob/list/')


def prob_delect(request):
    """"删除数据"""
    nid = request.GET.get("nid")
    models.ProbInfo.objects.filter(id=nid).delete()
    return redirect('/prob/list/')


def prob_list(request):
    """" 查询数据 """
    data_list = models.ProbInfo.objects.all()
    return render(request, 'probInfo.html', {'data_list': data_list})


"""修改数据"""


def prob_update(request, nid):
    if request.method == 'GET':
        row_object = models.ProbInfo.objects.filter(id=nid).first()
        return render(request, 'probUpdate.html', {'row_object': row_object})
    name = request.POST.get("name")
    des = request.POST.get("des")
    dim = request.POST.get("dim")
    obj = request.POST.get("obj")
    val = request.POST.get("val")
    weight = request.POST.get("weight")
    models.ProbInfo.objects.filter(id=nid).update(prob_name=name, description=des, dimensions=dim, objectives=obj,
                                                  value_vector=val,
                                                  weight_matrix=weight)

    return redirect('/prob/list/')


"""算法列表"""


def alg_list(request):
    data_list = models.AlgInfo.objects.all()
    return render(request, 'algInfo.html', {'data_list': data_list})


"""参数列表"""


def para_list(request, nid):
    data_list = models.PramInfo.objects.filter(algorithm_id=nid)
    return render(request, 'paraInfo.html', {'data_list': data_list, 'nid': nid})


"""插入参数"""


@csrf_exempt
def para_insert(request, nid):
    if request.method == 'GET':
        return render(request, 'paraInsert.html')
    name = request.POST.get("name")
    type = request.POST.get("type")
    des = request.POST.get("des")
    val = request.POST.get("val")

    models.PramInfo.objects.create(parm_name=name, type=type, description=des, value=val, algorithm_id=nid)
    return redirect(f'/para/{nid}/list/', {'nid': nid})


"""插入算法"""


@csrf_exempt
def alg_insert(request):
    if request.method == 'GET':
        return render(request, 'algInsert.html')
    name = request.POST.get("name")
    des = request.POST.get("des")

    models.AlgInfo.objects.create(alg_name=name, description=des)
    return redirect('/alg/list/')


"""删除算法"""


def alg_delect(request):
    nid = request.GET.get("nid")
    models.AlgInfo.objects.filter(id=nid).delete()

    return redirect('/alg/list/')


"""删除参数"""


def para_delect(request):
    nid = request.GET.get("nid")
    models.PramInfo.objects.filter(id=nid).delete()

    return redirect(f'/para/list/{nid}')


def alg_update(request, nid):
    if request.method == 'GET':
        data_list = models.AlgInfo.objects.filter(id=nid).first()
        return render(request, 'algUpdate.html', {'data_list': data_list})
    name = request.POST.get("name")
    des = request.POST.get("des")

    models.AlgInfo.objects.filter(id=nid).update(alg_name=name, description=des)

    return redirect('/alg/list/')






def para_update(request, nid):
    if request.method == 'GET':
        data_list = models.PramInfo.objects.filter(id=nid).first()
        print(nid)
        print(data_list)
        return render(request, 'paraUpdate.html', {'data_list': data_list})
    name = request.POST.get("name")
    type = request.POST.get("type")
    des = request.POST.get("des")
    val = request.POST.get("val")
    models.PramInfo.objects.filter(id=nid).update(parm_name=name, type=type, description=des, value=val)
    list = models.PramInfo.objects.filter(id=nid).first()
    fId = list.algorithm_id

    return redirect(f'/para/{fId}/list/')





def res_Res(request):
    data_list = models.AlgResult.objects.all()
    return render(request, 'algRes.html', {'data_list': data_list})


"""折线图"""
def res_lineChart(request):
    id_list = request.GET.getlist('nid')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot()
    buffer = io.BytesIO()
    probName = models.AlgResult.objects.filter(id=id_list[0]).first().problem_name
    for i in id_list:
        gen_res = models.GenResult.objects.filter(run_id=i).order_by('end_time')
        algName = gen_res.first().algorithm_name
        y = [gen_res.obj_value for gen_res in gen_res]
        x = [gen_res.gen_num for gen_res in gen_res]
        ax.plot(x, y, label=algName, linewidth=3.0)

    ax.grid(False)  # 取消网格
    ax.legend(loc='lower right')
    ax.set_xlabel('gen', fontsize=22)
    ax.set_ylabel('fitness', fontsize=22)
    ax.set_title(probName, fontsize=22)
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the image to base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    # Create the HTML response
    return render(request, 'chart.html', {
        'image_data': image_base64
    })


"""盒图"""
def res_boxChart(request):
    id_list = request.GET.getlist('nid')
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot()
    buffer = io.BytesIO()
    res = models.AlgResult.objects.filter(id=id_list[0])
    algName = res.first().algorithm_name
    probName = res.first().problem_name
    y = []
    for i in id_list:
        gen_res = models.GenResult.objects.filter(id=i).order_by('end_time').aggregate(Max('obj_value'))
        y.append(gen_res.get('obj_value__max'))
        print(y)
    ax.boxplot(y)
    ax.set_xlabel(algName, fontsize=22)
    ax.set_ylabel('fitness', fontsize=22)
    ax.set_title(probName, fontsize=22)
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return render(request, 'chart.html', {
        'image_data': image_base64
    })


"""执行方案管理"""
def plan_list(request):
    data_list = models.Plan.objects.all()
    return render(request, 'planInfo.html', {'data_list': data_list})


@csrf_exempt
def plan_insert(request):
    if request.method == 'GET':
        alg_list = models.AlgInfo.objects.all()
        prob_list = models.ProbInfo.objects.all()
        return render(request, 'planInsert.html', {'alg_list': alg_list, 'prob_list': prob_list})
    name = request.POST.get("name")
    alg = request.POST.get("alg")
    prob = request.POST.get("prob")
    count = request.POST.get("count")
    time = request.POST.get("time")
    models.Plan.objects.create(name=name, algorithms=alg, problems=prob, execution_count=count, start_time=time)
    alg_ids = [int(nid) for nid in alg.split(',')]
    data_list=[]
    for alg_id in alg_ids:
        data=models.AlgInfo.objects.filter(id=alg_id).first()
        data_list.append(data)
    return render(request,'algSelect.html', {'data_list':data_list})


def plan_delect(request):
    nid = request.GET.get('nid')
    models.Plan.objects.filter(id=nid).delete()
    return redirect('/plan/list')


def plan_update(request, nid):
    if request.method == 'GET':
        alg_list = models.AlgInfo.objects.all()
        prob_list = models.ProbInfo.objects.all()
        data_list = models.Plan.objects.filter(id=nid).first()
        alg_ids = [int(nid) for nid in data_list.algorithms.split(',')]
        return render(request, 'planUpdate.html',
                      {'data_list': data_list, 'alg_ids': alg_ids, 'alg_list': alg_list, 'prob_list': prob_list})

    name = request.POST.get("name")
    alg = request.POST.get("alg")
    prob = request.POST.get("prob")
    count = request.POST.get("count")
    time = request.POST.get("time")

    models.Plan.objects.filter(id=nid).update(name=name, algorithms=alg, problems=prob, execution_count=count, start_time=time)
    alg_ids = [int(nid) for nid in alg.split(',')]
    data_list = []
    for alg_id in alg_ids:
        data = models.AlgInfo.objects.filter(id=alg_id).first()
        data_list.append(data)
    return render(request,'algSelect.html', {'data_list':data_list})


def plan_exe(request):
    nid = request.GET.get('nid')
    data_list = models.Plan.objects.filter(id=nid).first()
    alg_ids = [int(nid) for nid in data_list.algorithms.split(',')]
    prob_ids = [int(nid) for nid in data_list.problems.split(',')]
    count = data_list.execution_count
    exe_time = data_list.start_time
    i = 1
    for alg_id in alg_ids:
        alg = models.AlgInfo.objects.filter(id=alg_id).first()
        alg_name = alg.alg_name
        pram_list = models.PramInfo.objects.filter(algorithm_id=alg_id).values('parm_name', 'value')
        pram_dict = {item['parm_name']: item['value'] for item in pram_list}
        pram_dict['time'] = exe_time
        pram_dict['alg_name'] = alg_name
        for prob_id in prob_ids:
            while i <= count:

                prob = models.ProbInfo.objects.filter(id=prob_id).first()

                module_path = os.path.join('algMag/algs', f"{alg_name}.py")
                pram_dict["prob"] = prob

                if os.path.exists(module_path):

                    spec = importlib.util.spec_from_file_location(alg_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if hasattr(module, 'main'):
                        try:
                            start_time_str = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
                            models.AlgResult.objects.create(algorithm_name=alg_name, problem_name=prob.prob_name,
                                                     start_time=start_time_str)
                            currId=models.AlgResult.objects.order_by('id').last().id
                            pram_dict['run_id']=currId
                            module.main(**pram_dict)

                            end_time_str = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
                            models.AlgResult.objects.filter(id=currId).update(end_time=end_time_str)
                        except Exception as e:

                            return HttpResponse(f"Error executing main function in {alg_name}: {e}")
                    else:
                        return HttpResponse(f"Module {alg_name} does not have a main function.")
                else:
                    return HttpResponse(f"Module file {module_path} does not exist.")
                i = i + 1
    return HttpResponse("执行完成")
