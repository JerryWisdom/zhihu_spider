#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import mongoengine

#连接mongodb数据库，创建my_zhihu_data
mongoengine.connect('my_zhihu_data')

class Zhihu_User_Profile(mongoengine.Document):
    user_name = mongoengine.StringField()
    user_be_agreed = mongoengine.StringField()
    user_be_thanked = mongoengine.StringField()
    user_followees = mongoengine.StringField()
    user_followers = mongoengine.StringField()
    user_education_school = mongoengine.StringField()
    user_education_subject = mongoengine.StringField()
    user_employment = mongoengine.StringField()
    user_employment_extra = mongoengine.StringField()
    user_location = mongoengine.StringField()
    user_gender = mongoengine.StringField()
    user_info = mongoengine.StringField()
    user_intro = mongoengine.StringField()
    user_url = mongoengine.StringField()
