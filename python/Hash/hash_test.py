# -*- coding:utf-8 -*-
# Created by ZhaoWen on 2021/1/26

def hash(name,phone):
    # 创建一个电话簿 -> 新建一个散列表
    phone_book = dict()

    '''
    Python提供了一种创建散列表的快捷方式 -> 使用一对大括号
    phone_book = {}
    '''

    # 在这个电话簿中添加一些联系人的电话号码
    phone_book["Alice"] = 334455
    phone_book["Alisa"] = 336666

    # 判断是否重复
    if phone_book.get(name):
        print("用户重复")
    else:
        phone_book[name] = phone
        print("修改成功")

if __name__ == "__main__":
    hash("Alic","334455")