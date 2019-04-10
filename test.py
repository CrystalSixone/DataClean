# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:44:59 2018

@author: Administrator
"""


import json
instance_name = 'instances_train2017.json'
valname = 'instances_val2017.json'
afterclean1 = 'afterclean_train2017_new.json'
afterclean2 = 'afterclean_val2017_new.json'
#indoor =[44,46,47,48,49,50,51,62,63,64,65,67,70,72,73,74,75,76,78,79,80,81,82,84,85,86,87,88,89,90]
'''indoor = ['1','17','18','23','27','28',
          '31','32','33','34','35','36',
          '37','38','39','40','41','42',
          '43','44','46','47','48','49',
          '50','51','52','53','54','55',
          '56','57','58','59','60','61',
          '62','63','64','65','67','70',
          '72','73','74','75','76','77',
          '78','79','80','81','82','84',
          '85','86','87','88','89','90']'''
indoor = [1,17,18,28,27,31,32,33,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,
          62,63,64,65,67,70,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90]

dic = {"annotaions":[]}
table = []

#创建list
def createtable():
    for i in range(len(indoor)):
        new = {'category_id':indoor[i],'times':0}
        table.append(new)

#主程序
def main():
    with open(valname, 'r',encoding='utf-8') as f:
        objects = json.loads(f.read())
        cleaning(objects)


#看种类
def category(object):
    print(object['categories'])

def creatjson():
    annokey = {"annotations":[]}
    test = {"good":"good"}
    #injson = json.dump(annokey)
    with open('test.json','w')as g:
        json.dump(annokey,g)
        json.dump(test,g)

def creatdic():
    test = {"test":"test"}
    test2 = {"test2":"test2"}
    dic["annotaions"].append(test)
    dic["annotaions"].append(test2)
    print(dic)

#填写list并清洗
def cleaning(object):
    with open(afterclean2,'a')as g:
        for category in object['annotations']:
            if category['category_id'] in indoor:
                for id in table:
                    if category['category_id'] == id['category_id']:
                       id['times'] += 1
                dic["annotaions"].append(category)
        json.dump(dic,g)

#打印id和次数
def printtable():
    print('id:')
    for i in range(len(table)):
        print(str(table[i]['category_id']))
    print('times:')
    for i in range(len(table)):
        print(str(table[i]['times']))

createtable()
main()
printtable()
#creatjson()


