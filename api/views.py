from django.shortcuts import render
from .models import ImportExcel
from django.http import JsonResponse
from .shahobiddin0528 import salom
from django.conf import settings
def index(request):
    context = {}
    con=0
    filename=[]
    if request.method =='POST':
        data1=ImportExcel.objects.all().delete()
        for i in request.FILES:
            file1=str(request.FILES[f'{i}'])
            print(file1)
            filename.append(file1)
            data=ImportExcel.objects.create(fexcel=request.FILES[f'{i}'])
            try:
                a=salom(f"{settings.BASE_DIR}/media/{data.fexcel}")
            except:
                print('xato bor')
            data.save()
            con+=1
    try:
        f = lambda A, n=5: [A[i:i+n] for i in range(0, len(A), n)]
        list1=f(a)
        context['msg']=list1[-con:]
        list3=[]
        list2=list1[-con:]
        for il in list2:
            print(il)
            list3.append(round(sum(float(item['qiymat']) for item in il)/len(il),2))
            print(list3)
            context['lolo']=list3
    except:
        print('jinni bo\'lib qolibdi')
    context['filename']=filename
    return render(request, 'index.html',context)
