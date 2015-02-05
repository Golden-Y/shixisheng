#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse as TR
from django.forms.models import modelform_factory
from django.template import RequestContext
from django.db.models import Q
import datetime
from .models import Company,Before,Text,TIntr,SIntr,Process,head,Problem,collective,live_img,project_img



def home(request):
	head_r=Text.objects.filter(category="home_roll")
	company=Company.objects.filter(order='1')
	teacher=TIntr.objects.all()

	dict_a={"head_r":head_r,"teacher":teacher,"company":company}

	t=Text.objects.all()
	for i in t:
		dict_a[i.category]=i
	
	return render_to_response('index4.html',dict_a)
	#return render_to_response('index4.html',context_instance=RequestContext(request))


def test(request):
	return TR(request,'test.html')

def test2(request):
	s=Before(name = request.POST["bname1"],simg = request.POST["simg1"],limg = request.POST["limg1"]).save()
	s2=SIntr(order = request.POST["sorder"],name = request.POST["sname"],level = request.POST["slevel"],sex = request.POST["ssex"],grade = request.POST["sgrade"],place = request.POST["splace"],position = request.POST["sposition"],salary = request.POST["ssalary"],contact = request.POST["scontact"],intr = request.POST["sintr"],img = request.POST["simg"],date = str(datetime.datetime.now())).save()
	s3=Company(order = request.POST["corder"],name = request.POST["cname"],categories = request.POST["categories"],salary = request.POST["csalary"],place = request.POST["cplace"],number = request.POST["cnumber"],position = request.POST["cposition"],describe = request.POST["cdescribe"],log = request.POST["clog"],img = request.POST["cimg"],img2 = request.POST["cimg2"],date = str(datetime.datetime.now())).save()
	s4=TIntr(name = request.POST["pname"],company = request.POST["pcompany"],intr = request.POST["pintr"],img = request.POST["pimg"]).save()
	s5=TIntr(name = request.POST["pname2"],company = request.POST["pcompany2"],intr = request.POST["pintr2"],img = request.POST["pimg2"]).save()
	s6=Text(category = request.POST["tcategory"],name = request.POST["tname"],intr = request.POST["tintr"]).save()
	s7=Text(category = request.POST["tcategory2"],name = request.POST["tname2"],intr = request.POST["tintr2"]).save()
	s8=Text(category = request.POST["tcategory3"],name = request.POST["tname3"],intr = request.POST["tintr3"]).save()
	s9=Text(category = request.POST["tcategory4"],name = request.POST["tname4"],intr = request.POST["tintr4"]).save()
	s10=Text(category = request.POST["tcategory5"],name = request.POST["tname5"],intr = request.POST["tintr5"]).save()
	s11=Text(category = request.POST["tcategory6"],name = request.POST["tname6"],intr = request.POST["tintr6"]).save()
	s12=Text(category = request.POST["tcategory7"],name = request.POST["tname7"],intr = request.POST["tintr7"]).save()
	s13=Text(category = request.POST["tcategory8"],name = request.POST["tname8"],intr = request.POST["tintr8"]).save()
	s14=Text(category = request.POST["tcategory9"],name = request.POST["tname9"],intr = request.POST["tintr9"]).save()
	s15=Text(category = request.POST["tcategory10"],name = request.POST["tname10"],intr = request.POST["tintr10"]).save()
	s16=Text(category = request.POST["tcategory11"],name = request.POST["tname11"],intr = request.POST["tintr11"]).save()
	s17=Text(category = request.POST["tcategory12"],name = request.POST["tname12"],intr = request.POST["tintr12"]).save()
	s18=Text(category = request.POST["tcategory13"],name = request.POST["tname13"],intr = request.POST["tintr13"]).save()

	return HttpResponse('ok')

def old(request):
	before=Before.objects.all()
	dict_b={"before":before}
	return TR(request,'old.html',dict_b)
def third(request):
	p=SIntr.objects.filter(order="1")
	dict_c={"p":p}
	return TR(request,'third.html',dict_c)
def pin(request):
	d={}
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	return TR(request,"recruitment.html",d)
def zhaopin(request):
	d={}
	if request.POST["name"]=="":
		d['a']="请输入企业名称"
		return TR(request,'recruitment.html',d)
	if request.POST["gangwei"]=="":
		d['b']="请输入岗位名称"
		d['mingcheng']=request.POST["name"]
		return TR(request,'recruitment.html',d)
	if request.POST["xinzi"]=="":
		d['c']="请输入薪资范围"
		d['mingcheng']=request.POST["name"]
		d['gangwei']=request.POST["gangwei"]
		return TR(request,'recruitment.html',d)
	if request.POST["didian"]=="":
		d['d']="请输入工作地点"
		return TR(request,'recruitment.html',d)
	if request.POST["renshu"]=="":
		d['e']="请输入招聘人数"
		return TR(request,'recruitment.html',d)
	if request.POST["jianjie"]=="":
		d['f']="请输入岗位介绍"
		d['mingcheng']=request.POST["name"]
		d['gangwei']=request.POST["gangwei"]
		return TR(request,'recruitment.html',d)
	Company(name = request.POST["name"],position = request.POST["gangwei"],salary = request.POST["xinzi"],place = request.POST["didian"],number = request.POST["renshu"],describe = request.POST["jianjie"],date = str(datetime.datetime.now())).save()
	ac=Company.objects.all()[::-1]
	d={'ac':ac}
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	return TR(request,"AllCompany.html",d)
def liucheng(request):
	p=Process.objects.all()
	p={"p":p}
	t=Text.objects.all()
	for i in t:
		p[i.category]=i
	return TR(request,"process.html",p)
def jianli(request):
	d={}
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	return TR(request,"resume.html",d)
def jltj(request):
	d={}
	if request.POST["name"]=="":
		d['a']="请输入姓名"
		return TR(request,'resume.html',d)
	if request.POST["zhuanye"]=="":
		d['b']="请输入专业"
		d['xingming']=request.POST["name"]
		return TR(request,'resume.html',d)
	if request.POST["xinzi"]=="":
		d['c']="请输入期望薪资"
		return TR(request,'resume.html',d)
	if request.POST["didian"]=="":
		d['d']="请输入工作地点"
		return TR(request,'resume.html',d)
	if request.POST["lianxi"]=="":
		d['e']="请输入联系方式"
		d['xingming']=request.POST["name"]
		d['zhuanye']=request.POST["zhuanye"]
		return TR(request,'resume.html',d)
	if request.POST["nianji"]=="":
		d['e']="请输入学历/年级"
		d['xingming']=request.POST["name"]
		d['zhuanye']=request.POST["zhuanye"]
		d['lianxi']=request.POST["lianxi"]
		return TR(request,'resume.html',d)
	if request.POST["jieshao"]=="":
		d['f']="请输入自我介绍"
		d['xingming']=request.POST["name"]
		d['zhuanye']=request.POST["zhuanye"]
		d['lianxi']=request.POST["lianxi"]
		d['nianji']=request.POST["nianji"]
		return TR(request,'resume.html',d)
	SIntr(order = "-1",name = request.POST["name"], sex= request.POST["xingbie"], grade= request.POST["nianji"], place = request.POST["didian"], position= request.POST["zhuanye"],salary = request.POST["xinzi"],contact = request.POST["lianxi"],intr = request.POST["jieshao"],date = str(datetime.datetime.now())).save()
	stu=SIntr.objects.filter(Q(order='1') | Q(order='0'))
	dict_d={"stu":stu}
	t=Text.objects.all()
	for i in t:
		dict_d[i.category]=i
	return TR(request,"youxiu.html",dict_d)
def allcompany(request):
	ac=Company.objects.all()[::-1]
	d={'ac':ac}
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	return TR(request,"AllCompany.html",d)
def youxiu(request):
	stu=SIntr.objects.filter(Q(order='1') | Q(order='0'))
	dict_d={"stu":stu}
	t=Text.objects.all()
	for i in t:
		dict_d[i.category]=i
	return TR(request,"youxiu.html",dict_d)
def faq(request):
	d={}
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	p=Problem.objects.all()
	d["p"]=p
	return TR(request,"FAQ.html",d)
def x(request):
	t=head.objects.all()
	d={"t":t}
	return TR(request,"x.html",d)

def be(request,id = 1):
	s = collective.objects.all()
	d = {"collective":s}
	s = collective.objects.get(id = int(id))
	d.setdefault("s",s)
	s1 = project_img.objects.filter(Pid = s.Name)
	d.setdefault('s1',s1)
	s2 = live_img.objects.filter(Pid = s.Name)
	d.setdefault('s2',s2)
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	return render_to_response("befores.html",d)
def grjl(request,sid):
	s = SIntr.objects.get(id = sid)
	d={"s":s}
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	return TR(request,"gerenjianli.html",d)
def zpxx(request,cid):
	c = Company.objects.get(id = cid)
	d={"c":c}
	t=Text.objects.all()
	for i in t:
		d[i.category]=i
	return TR(request,"zhaopinxinxi.html",d)
