#coding:utf-8
from django.db import models

class Text(models.Model):
	category = models.CharField(max_length=30)
	name     = models.CharField(max_length=30) 
	intr     = models.TextField(blank=True)

class Company(models.Model):
	order      = models.CharField(max_length=64,blank=True) 			#标记
	name       = models.CharField(max_length=64) 						#公司名称
	categories = models.CharField(max_length=30,blank=True) 			#公司类别
	salary	   = models.CharField(max_length=30)  						#薪资范围
	place	   = models.CharField(max_length=128)						#工作地点
	number	   = models.CharField(max_length=20)  						#招聘人数
	position   = models.CharField(max_length=128)						#公司招聘职位	
	describe   = models.TextField()				 						#岗位描述
	log        = models.ImageField(upload_to='./img',blank=True) 		#公司log
	img        = models.ImageField(upload_to='./img',blank=True) 		#公司图片
	img2       = models.ImageField(upload_to='./img',blank=True) 		#公司图片2
	date	   = models.CharField(max_length=30)  						#生成时间
class Before(models.Model):
	name  = models.CharField(max_length=512) 		#图片信息
	simg  = models.ImageField(upload_to='./img') 	#往期照片小
	limg  = models.ImageField(upload_to='./img') 	#往期照片大

class TIntr(models.Model):
	name     = models.CharField(max_length=30) 
	company  = models.CharField(max_length=60,blank=True) 
	intr     = models.TextField()
	img  = models.ImageField(upload_to='./img/teacher')

class SIntr(models.Model):
	order      = models.CharField(max_length=64,blank=True)  	#标记
	name       = models.CharField(max_length=30)  				#学生姓名
	level      = models.CharField(max_length=30,blank=True)  	#等级
	sex        = models.CharField(max_length=30)  				#性别
	grade      = models.CharField(max_length=30)  				#年级
	place	   = models.CharField(max_length=128) 				#期望工作地点
	position   = models.CharField(max_length=128) 				#适合职位
	salary	   = models.CharField(max_length=30)  				#期望薪资
	contact	   = models.CharField(max_length=30)  				#联系方式
	intr       = models.TextField()
	img        = models.ImageField(upload_to='./img/student',blank=True)
	date	   = models.CharField(max_length=30)  				#生成时间

class Process(models.Model):						#实习流程表
	name = models.CharField(max_length = 100)  		#标题
	intr = models.CharField(max_length = 300)  		#内容
	img = models.ImageField(upload_to = "./img") 	#图片
 
class head(models.Model):
	order     = models.CharField(max_length=64,blank=True) 
	name      = models.CharField(max_length=30)  				
	intr      = models.CharField(max_length=30)  
	img       = models.ImageField(upload_to='./img/head')

class Problem(models.Model):
	order     = models.CharField(max_length=64,blank=True) 
	problem   = models.CharField(max_length=512)  				
	answer    = models.TextField() 
	 
class collective(models.Model): 							#往期实习表
	Name			= models.CharField(max_length = 20)			#名称/期数
	Img				= models.ImageField(upload_to = './img')	#集体照片
	Amount			= models.CharField(max_length = 20)			#人数
	Course 			= models.CharField(max_length = 50)			#课程
	project_name	= models.CharField(max_length = 50)			#项目名称
	project_text    = models.TextField(blank=True)				#项目介绍
	project_link	= models.CharField(max_length = 20)			#项目链接

class live_img(models.Model):								#生活照
	Pid				= models.CharField(max_length = 50)					#次级ID 例如collective_Name
	Name 			= models.CharField(max_length = 20,blank=True)					#图片标题
	Img				= models.ImageField(upload_to = './img',blank=True)	#生活图片
	Text			= models.TextField(blank=True)								#文本内容
	#日期

class project_img(models.Model):	
	Pid				= models.CharField(max_length = 50)					#次级ID 例如collective_Name
	Name 			= models.CharField(max_length = 50,blank=True)					#项目标题
	Img				= models.ImageField(upload_to = './img',blank=True)	#项目图片