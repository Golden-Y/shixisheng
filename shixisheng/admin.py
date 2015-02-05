from django.contrib import admin
from .models import  Text , Company , Before ,TIntr ,SIntr,Process,head,Problem,collective,live_img,project_img

class TextInfoAdmin(admin.ModelAdmin):
	list_display = ("id","name",)

class CompanyInfoAdmin(admin.ModelAdmin):
	list_display = ("id","name",)

class BeforeInfoAdmin(admin.ModelAdmin):
	list_display = ("id","name",)

class TIntrInfoAdmin(admin.ModelAdmin):
	list_display = ("id","name",)

class SIntrInfoAdmin(admin.ModelAdmin):
	list_display = ("id","name",)

class ProcessInfoAdmin(admin.ModelAdmin):
	list_display = ("id","name",)

class headInfoAdmin(admin.ModelAdmin):
	list_display = ("id","name",)

class ProblemInfoAdmin(admin.ModelAdmin):
	list_display = ("id","problem",)
#-------------img-----------------
class collectiveInfoAdmin(admin.ModelAdmin):		
	list_display = ('id','Name','Amount','Course','Img','project_name','project_link',)

class live_imgInfoAdmin(admin.ModelAdmin):		
	list_display = ('id','Pid','Name','Img','Img','Text',)

class project_imgInfoAdmin(admin.ModelAdmin):	
	list_display = ('id','Pid','Name','Img',)






admin.site.register(Problem,ProblemInfoAdmin)
admin.site.register(head,headInfoAdmin)
admin.site.register(Process,ProcessInfoAdmin)
admin.site.register(Text,TextInfoAdmin)
admin.site.register(Company,CompanyInfoAdmin)
admin.site.register(Before,BeforeInfoAdmin)
admin.site.register(TIntr,TIntrInfoAdmin)
admin.site.register(SIntr,SIntrInfoAdmin)
#----------------img-----------------
admin.site.register(collective,collectiveInfoAdmin)
admin.site.register(live_img,live_imgInfoAdmin)
admin.site.register(project_img,project_imgInfoAdmin)


