# -*- coding:utf-8 -*-
# Created by ZhaoWen on 2021/1/28


def greedy():
    # 传入一个数组 ， 将其转换为集合
    # 此处 我们使用集合来表示要覆盖的州。集合类似于列表，只是同样的元素只能出现依次，即`集合不能包含重复元素`
    states_needed = set(["mt","wa","or","id","nv","uv","ca","az"])

    # 提供可供选择的广播台清单 此处选择使用散列表来表示 表示：广播台 -> 覆盖的州 缩写
    stations = {}
    stations["kone"] = set(["id","nv","ut"])
    stations["ktwd"] = set(["wa","id","mt"])
    stations["kthree"] = set(["or","nv","ca"])
    stations["kfour"] = set(["nv","ut"])
    stations["kfive"] = set(["ca","az"])

    # 使用一个集合来存储最终选择的广播台
    final_stations = set()

    # 设定贪婪算法计算答案
    while states_needed:
        # 正确的解可能有多个，需要我们遍历所有的广播台，从中选择覆盖了最多的未覆盖州的广播台
        best_station = None
        # 一个集合 包含该广播台覆盖的所有未覆盖的州
        states_covered = set()
        # for循环迭代每个广播台 并确定它是否是最佳的广播台
        for station, states_for_station in stations.items():
            # 计算交集 要覆盖的州 & 当前电视台覆盖的州 -> 集合类似于列表 只是不能包含重复的元素 可以执行一些有趣的集合运算 如并集、交集和差集
            covered = states_needed & states_for_station
            # 检查覆盖的州是否比未覆盖的州 多
            if len(covered) > len(states_covered):
                # best_station表示当前的最佳选择
                best_station = station
                states_covered = covered
        # 更新states_needed 由于该广播台覆盖了一些州 因此不用覆盖这些州
        states_needed -= states_covered
        final_stations.add(best_station)

if __name__ == "__main__":
    greedy()