# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:48:10 2018

@author: Sriram Arvind Lakshmanakumar @primitive14 

@source code : REST Service for Contact Us Page

"""
from dbconnect import getConnection 
from flask import Flask,jsonify
from flask import request
from ContactUs import ContactUs
app = Flask(__name__) 


@app.route('/submitRequest',methods=['POST']) 

def submitRequest(): 
    #message data from front end 
    #data format JSON 
    
    input_data = request.get_json(force=True) 
    formData = dict() 
    
    formData['firstName'] = input_data.get('firstName')
    formData['lastName'] = input_data.get('lastName')
#    formData['email'] = input_data.get('email')
    formData['mobileNo'] = input_data.get('mobileNo')
#    formData['ipaddress'] = input_data.get('ipaddress')
    formData['message'] = input_data.get('message')
#    formData['messagedate'] = input_data.get('messagedate')
    
    ContactUsObj = ContactUs() 
    requestResponse = ContactUsObj.submitRequest(formData) 
    
    return jsonify({"Message":requestResponse})
    
    
if __name__ == '__main__':
    app.run(debug=True) 
    
    