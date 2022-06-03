from datetime import datetime
from importlib.resources import path
start_time = datetime.now()
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 14:32:30 2022

@author: shoho
"""
import xlrd
lista=[]
def salom(path):
    book = xlrd.open_workbook(path)
    sinf1=book.sheet_by_name('1')
    data1 = [[sinf1.cell_value(r, c) for c in range(sinf1.ncols)] for r in range(sinf1.nrows)]
    sinf2=book.sheet_by_name('2')
    data2 = [[sinf2.cell_value(r, c) for c in range(sinf2.ncols)] for r in range(sinf2.nrows)]
    sinf3=book.sheet_by_name('3')
    data3 = [[sinf3.cell_value(r, c) for c in range(sinf3.ncols)] for r in range(sinf3.nrows)]
    sinf4=book.sheet_by_name('4')
    data4 = [[sinf4.cell_value(r, c) for c in range(sinf4.ncols)] for r in range(sinf4.nrows)]
    sinf5=book.sheet_by_name('5')
    data5 = [[sinf5.cell_value(r, c) for c in range(sinf5.ncols)] for r in range(sinf5.nrows)]
    sinflar={0:data1,
            1:data2,
            2:data3,
            3:data4,
            4:data5
            }
    hatolar=[]
    for j in range(1+len(sinflar[0])-int(15*len(sinflar[0])/100)):
        qismlar85=[]
        qismlar15=[]
        jam=[]
        for a in range(5):
           sinf=sinflar[a][:]# sinfni yana dastlabki holiga qaytarish uchun chunki pop() funksiyasi elementlarni suigirib olgan so`ng elementlar kmayib qoladi
           qism15=[]
           qism85=[]
           for i in range(j,int(len(sinflar[a])*15//100)+j):
               qism15.append((sinf.pop(j)))
           qismlar15.append(qism15)
           qismlar85.append(sinf)

        for b in range(len(qismlar15)):
            hatolik=0
            qism15=qismlar15[b]
            baholar1=[]
            for c  in range(len(qismlar85)):
                qism85=qismlar85[c]
                summa=[]

                for i in range(len(qism15)):
                    summ1=[]
                    for j in range(len(qism85)):
                        binar=[]
                        for a in range(6):

                            if qism15[i][a]==0 and qism85[j][a]==0:
                                binar.append(0)
                            elif qism15[i][a] - qism85[j][a]==0:
                                binar.append(1)
                            else:
                                binar.append(0)
                        summ1.append(sum(binar))#bu qism15 ni 1ta obyectiga qism85  1 ta obyecti bergan bahosi bergan bahosi
                    summa.append(sum(summ1)) #bu qism15 ni 1ta obyectiga qism85 ni bergan bahosi
                baholar1.append(summa)#bu qism 15 ga  har bir qism 85 ni bergan baholari

            for i in range(len(summa)):
                baho1=[]
                for j in range(len(baholar1)):
                  baho1.append(baholar1[j][i])
                if baho1[b]==max(baho1):
                    hatolik=hatolik+0
                else:
                    hatolik=hatolik+(len(sinf[0])/100)
            hatolar.append(hatolik)
    list6=[]
    # list8=[]
    for j in range(5):
        hato=[]
        for i in range(j,len(hatolar),5):
            hato.append(hatolar[i])
            a=round(sum(hato),2)
            list6.append(a)
        # print(sum(hato))
        lista.append({'sinf':j+1,'qiymat':a})
        list7=sum(lista[i]['qiymat'] for i in range(1,len(lista))) / len(lista)
        # for i in range(len(lista)):
        #     lista[i]['lolo']=list7
        # list8.append(sum(float(i) for i in list6))
    return lista

# print(salom(r'/home/intech/Shahobiddinoka/media/excel/2022/06/02/l9.xls'))

    #                # jam=[] # bu royhat har bir ajratib olingan  % larni umumiy baholarini toplash uchun ochil
