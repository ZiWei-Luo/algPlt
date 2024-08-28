
import time
from algMag.models import GenResult
from django.utils import timezone

def main(**para):
    a=para.get('a')
    b=para.get('b')
    s=para.get('time')
    prob=para.get('prob')
    alg_name=para.get('alg_name')
    runID=para.get('run_id')
    start_time = time.time()
    i=0
    x=1
    y=0
    current_time = time.time()
    spend_time = current_time - start_time

    while spend_time <= s/1000:
        y=a*x+b
        x=x+1
        current_time=time.time()
        spend_time = current_time - start_time
        print(f'algorithm_name={alg_name},coding=[{x}],gen_num={i},obj_value={y},problem_instance_name={prob.prob_name},run_id={runID},end_time={timezone.now().strftime("%Y-%m-%d %H:%M:%S")}')
        GenResult.objects.create(algorithm_name=alg_name,coding=[x],gen_num=i,obj_value=y,problem_instance_name=prob.prob_name,run_id=runID,end_time=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
        i=i+1


