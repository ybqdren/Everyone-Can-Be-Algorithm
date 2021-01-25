# -*- coding:utf-8 -*-
# Created by ZhaoWen on 2021/1/25

'''
Python实现 广度优先搜索
摘自《算法图解》
'''

from collections import deque

def person_is_seller(name):
    return name[-1] == name

# 实现BFS 广度优先搜索
def search(name):
    # 实现图 每一个key值对应这一个列表（数组）
    graph = {}
    graph["you"] = ["alice","bob","claire"]
    graph["bob"] = ["anuj","peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom","jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    # 创建一个双端队列
    search_queue = deque()

    # 将指定key的数组加入搜索队列中
    search_queue += graph[name]

    # 创建一个搜索过的队列 防止重复搜索同一个人
    searched = []

    while search_queue:
        # 获取队列中的第一个人
        person = search_queue.popleft()

        # 这个人也没有被搜索过
        if person not in searched:
            # 并且这个是我们的目标
            if person_is_seller(person):
                print(person +"is a mongo seller！")
                return True
            else:
                # 如果不是 就将这个人所对应的列表加入到搜索队列中
                search_queue += graph[person]
            # 将这个person加入已被搜索的队列中
            searched.append(person)
    return False



if __name__=="__main__":
    search("you")