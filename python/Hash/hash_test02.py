# -*- coding:utf-8 -*-
# Created by ZhaoWen on 2021/1/27
# 网站数据缓存案例

def get_data_from_server(url):
    return url

def hash_cache():
    cache = {}
    def get_page(url):
        if cache.get(url):
            return cache[url]
        else:
            data = get_data_from_server(url)
            cache[url] = data
            return data

if __name__ == "__main__":
    hash_cache()