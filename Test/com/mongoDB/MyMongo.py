#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

conn = MongoClient('192.168.0.113', 27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建
my_set = db.test_set #使用test_set集合，没有则自动创建

#插入数据（insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入）
my_set.insert({"name":"zhangsan","age":18})
#或
my_set.save({"name":"zhangsan","age":18})

