#coding utf-8
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Login.models import Users,SaleD,ShopList


import os
import xlrd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import time
from time import strftime,gmtime
from pylab import *
from pandas.core.frame import DataFrame
mpl.rcParams['font.sans-serif'] = ['SimHei']

def FirstPage(request):
#    return HttpResponse('111111')
    return render(request,'LoginPage.html')

def HomePage(request):
#    return HttpResponse('111111')
    return render(request,'index.html')

@csrf_exempt                      #保证表单可以使用
def loginCheck(request):
    Uname = request.POST['username']
    Upassword = request.POST['password']
    a = list(Users.objects.values_list().filter(name = Uname))
    if a.__len__() != 0:  #找到记录   a = [(1,'name','password')]
        print('找到记录')
        if a[0][2] == Upassword:
            print('登入成功')
            return render(request, 'index.html')
        else:
            print('登入失败')
            err = '密码错误！'
            return render(request, 'LoginPage.html',{'err':err})
    else:
        print('登入失败')
        err = '账号错误！'
        return render(request, 'LoginPage.html', {'err':err})

def aSum(SaleDStruct):
    a = SaleDStruct.Gapple+SaleDStruct.Gorange+SaleDStruct.Gbowl+\
        SaleDStruct.Gchopstick+SaleDStruct.Grag+SaleDStruct.Gtissue+SaleDStruct.Gnoddle+SaleDStruct.Gham
    return a

def DrawHisgram(request):
    print('柱状图')
#    os.chdir('C:\\Users\\ZHOU\\Desktop\\Django')
#    salesdata = pd.DataFrame(pd.read_excel('1.xlsx', sheet_name=1))

    LineData = list(SaleD.objects.all().order_by('Gdate'))
    apple = list()
    orange = list()
    bowl = list()
    chopstick = list()
    rag = list()
    tissue = list()
    noddle = list()
    ham = list()
    date = list()
    count = list()
    for i in range(0,12):
        apple.append(LineData[i].Gapple)
        orange.append(LineData[i].Gorange)
        bowl.append(LineData[i].Gbowl)
        chopstick.append(LineData[i].Gchopstick)
        rag.append(LineData[i].Grag)
        tissue.append(LineData[i].Gtissue)
        noddle.append(LineData[i].Gnoddle)
        ham.append(LineData[i].Gham)
        date.append(LineData[i].Gdate)
        count.append(aSum(LineData[i]))

    GdateSet = {"日期": date, "苹果": apple, "橘子": orange, "碗": bowl, "筷子": chopstick, "抹布": rag, "纸巾": tissue,
                '方便面': noddle, '火腿肠': ham,'count':count}
    salesdata = DataFrame(GdateSet)
    salesdata = salesdata.groupby('日期')['count'].agg(sum)
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.xticks(a, ('1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'))
    plt.bar(a, salesdata, color='#99CC01')
    plt.xlabel(u'月份')
    plt.ylabel(u'金额/元')
    plt.title(u'2016年各月销售额统计')
    plt.legend([u'销售额'], loc='upper right')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.plot()
    picName = time.strftime("%Y_%m_%d_%H_%M_%S")
    path = 'C:/Users/ZHOU/Desktop/Django/MartM/Login/static/img/' + picName + 'His.png'
    plt.savefig(path)
    path = '../static/img/' + picName + 'His.png'
    plt.close('all')
    return render(request,'Hisgram.html',{'path':path})

def DrawLine(request):
    print('折线图')
#    os.chdir('C:\\Users\\ZHOU\\Desktop\\Django')
#    salesdata = pd.DataFrame(pd.read_excel('1.xlsx'))

    LineData = list(SaleD.objects.all().order_by('Gdate'))
    apple = list()
    orange = list()
    bowl = list()
    chopstick = list()
    rag = list()
    tissue = list()
    noddle = list()
    ham = list()
    date = list()
    for i in range(0,12):
        apple.append(LineData[i].Gapple)
        orange.append(LineData[i].Gorange)
        bowl.append(LineData[i].Gbowl)
        chopstick.append(LineData[i].Gchopstick)
        rag.append(LineData[i].Grag)
        tissue.append(LineData[i].Gtissue)
        noddle.append(LineData[i].Gnoddle)
        ham.append(LineData[i].Gham)
        date.append(LineData[i].Gdate)
    GdateSet = {"日期":date,"苹果":apple,"橘子":orange,"碗":bowl,"筷子":chopstick,"抹布":rag,"纸巾":tissue,'方便面':noddle,'火腿肠':ham}
    salesdata = DataFrame(GdateSet)
    # 绘图
    salesdata = salesdata.set_index('日期')
    names = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    x = range(len(names))
    y1 = salesdata['苹果']
    y2 = salesdata['橘子']
    y3 = salesdata['碗']
    y4 = salesdata['筷子']
    y5 = salesdata['抹布']
    y6 = salesdata['纸巾']
    y7 = salesdata['方便面']
    y8 = salesdata['火腿肠']

    plt.xticks(x, names)
    plt.plot(x, y1, marker='*', ms=5, mec='r', label=u'苹果')
    plt.plot(x, y2, marker='*', ms=5, label=u'橘子')
    plt.plot(x, y3, marker='*', ms=5, label=u'碗')
    plt.plot(x, y4, marker='*', ms=5, label=u'筷子')
    plt.plot(x, y5, marker='*', ms=5, label=u'抹布')
    plt.plot(x, y6, marker='*', ms=5, label=u'纸巾')
    plt.plot(x, y7, marker='*', ms=5, label=u'方便面')
    plt.plot(x, y8, marker='*', ms=5, label=u'火腿肠')
    plt.legend()
    plt.xlabel(u"月份")
    plt.ylabel(u"销售额")
    plt.title("超市2016年度销售走势图")
    plt.plot()
    picName = time.strftime("%Y_%m_%d_%H_%M_%S")
    path = 'C:/Users/ZHOU/Desktop/Django/MartM/Login/static/img/' + picName + 'Line.png'
    plt.savefig(path)
    path = '../static/img/' + picName + 'Line.png'
    plt.close('all')
    return render(request, 'LineGraph.html', {'path': path})


def DrawPai(request):
    print('饼图')
#    data = xlrd.open_workbook('C:\\Users\\ZHOU\\Desktop\\Django\\1.xlsx')
#    sheet1 = data.sheet_by_name(u'Sheet3')
    X = []
    Gtitle = ['Gapple','Gorange','Gbowl','Gchopstick','Grag','Gtissue','Gnoddle','Gham']
    for i in range(0, 8):
        temp = Gtitle[i]
        X.append(sum(list(SaleD.objects.values_list(temp,flat=True))))
    print(X)
    Y = ['苹果', '橘子', '碗', '筷子', '抹布', '纸巾', '方便面', '火腿肠']
    print(Y)
    fig = plt.figure()
    plt.pie(X, labels=Y, autopct='%1.2f%%')
    plt.title("2016年超市销售额饼图")
    plt.plot()
    picName = time.strftime("%Y_%m_%d_%H_%M_%S")
    path = 'C:/Users/ZHOU/Desktop/Django/MartM/Login/static/img/' + picName + 'Pai.png'
    plt.savefig(path)
    path = '../static/img/' + picName + 'Pai.png'
    plt.close('all')
    return render(request, 'PaiGraph.html', {'path': path})



def load_data_set():  # 读入数据库。
#    F1 = open(r"C:\Users\Administrator\Desktop\1.txt", "r")
#    List_row = F1.readlines()
    Glist = list(ShopList.objects.all())
    list_source = []
    for i in range(Glist.__len__()):
        column_list = Glist[i].ListContent.strip().split("|")
        list_source.append(column_list)
    return list_source


# 生成1项集C1
def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


# 判断是否满足先验性质
def is_apriori(Ck_item, Lksub1):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True


# 连接Lk-1，生成Ck，剪枝
def create_Ck(Lksub1, k):
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k - 2] == l2[0:k - 2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                # pruning
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


# 筛选，扫描数据库，生成频繁k项集Lk
def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


# 所有频繁项集L
def generate_L(data_set, k, min_support):
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k + 1):
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data

    # 生成强关联项
def generate_big_rules(L, support_data, min_conf):
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in big_rule_list:
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list

def Apriori(request):
    data_set = load_data_set()
    L, support_data = generate_L(data_set, k=3, min_support=0.2)
    big_rules_list = generate_big_rules(L, support_data, min_conf=0.7)
    print("=" * 50)
    print("频繁项集")
    print('**' * 30)
    freqList = []
    for Lk in list(L):
        for freq_set in Lk:
            print(list(freq_set), "支持度：", support_data[freq_set])
            if support_data[freq_set]>=0.4:
                freqList.append(' 和 '.join(list(freq_set)) + "  支持度：  " + repr(support_data[freq_set])+'             建议加大进货力度')
            else:
                freqList.append(' 和 '.join(list(freq_set)) + "  支持度：  " + repr(support_data[freq_set]))
        freqList.append('*************************************')
    print("=" * 50)
    ContactList = []
    print("强关联项")
    for item in big_rules_list:
        print(list(item[0]), "=>", list(item[1]), "置信度: ", item[2])
        ContactList.append(' 和 '.join(list(item[0])) + " => "+' 和 '.join(list(item[1])) + " 置信度: " + repr(item[2]))

    return render(request,'Apriori.html',{"freqList":freqList,"ContactList":ContactList})


def DataDisp(request):
    DataDispSet = list(SaleD.objects.all().order_by('Gdate'))
    ShoppingList = list(ShopList.objects.all())
    return render(request,'DataDisplay.html',{"cols":DataDispSet,"shopList":ShoppingList})