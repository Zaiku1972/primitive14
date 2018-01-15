# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:06:10 2018

@author: Sriram Arvind Lakshmanakumar
""" 
from dbconnect import getConnection 

class ContactUs(object): 
    
    def __init__(self): 
        self.connection = getConnection() 
    
    def submitRequest(self,messageRequest): 
        try:
            with self.connection as cursor: 
                sql = "INSERT INTO `contactus` (firstName,lastName,mobileNo,message) VALUE (%s,%s)"
                cursor.execute(sql,(messageRequest['firstName'],messageRequest['lastName'],messageRequest['mobileNo'],messageRequest['message']))
        except Exception as e: 
            print(e) 

        
        
    

