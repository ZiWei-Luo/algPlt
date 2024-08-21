import base64
import io

from django.db.models import Max
from django.shortcuts import render
# from sympy import Max

from resDis import models
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

# Create your views here.

"""算法结果展示"""


def algRes(request):
    data_list = models.AlgResult.objects.all()
    return render(request, 'algResult.html', {'data_list': data_list})


"""折线图"""


def lineChart(request):
    id_list = request.GET.getlist('nid')
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot()
    buffer = io.BytesIO()
    probName = models.AlgResult.objects.filter(run_id=id_list[0]).first().problem_name
    for i in id_list:
        gen_res = models.GenResult.objects.filter(run_id=i).order_by('end_time')
        algName = gen_res.first().algorithm_name
        y = [gen_res.obj_value for gen_res in gen_res]
        x = [gen_res.gen_num for gen_res in gen_res]
        # avg = np.mean(y, axis=0)
        # std = np.std(y, axis=0)
        # r1 = list(map(lambda y: y[0] - y[1], zip(avg, std)))  # 上方差
        # r2 = list(map(lambda y: y[0] + y[1], zip(avg, std)))  # 下方差
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


def boxChart(request):
    id_list = request.GET.getlist('nid')
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot()
    buffer = io.BytesIO()
    res = models.AlgResult.objects.filter(run_id=id_list[0])
    algName = res.first().algorithm_name
    probName = res.first().problem_name
    y = []
    for i in id_list:
        gen_res = models.GenResult.objects.filter(run_id=i).order_by('end_time').aggregate(Max('obj_value'))
        y.append(gen_res.get('obj_value__max'))
        print(y)
    ax.boxplot(y)
    ax.set_xlabel(algName, fontsize=22)
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
