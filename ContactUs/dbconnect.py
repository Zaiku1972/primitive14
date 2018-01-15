# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:37:17 2018

@author: Sriram Arvind Lakshmanakumar 

"""
import pymysql 

def getConnection(): 
    connection = pymysql.connect(host='localhost',
                                 port= 3306,
                                 user='root',
                                 password='googleg2',
                                 db='primitive14',
                                 connect_timeout=480,
                                 autocommit=True,
                                 use_unicode=True,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection