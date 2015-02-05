from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shixisheng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'shixisheng.views.home'),
    url(r'^test.html$', 'shixisheng.views.test'),
    url(r'^test2.html$', 'shixisheng.views.test2'),
    url(r'^old.html$', 'shixisheng.views.old'),
    url(r'^third.html$', 'shixisheng.views.third'),
    url(r'^pin.html$', 'shixisheng.views.pin'),
    url(r'^zhaopin$', 'shixisheng.views.zhaopin'),
    url(r'^liucheng$', 'shixisheng.views.liucheng'),
    url(r'^jianli$', 'shixisheng.views.jianli'),
    url(r'^jltj$', 'shixisheng.views.jltj'),
    url(r'^allcompany$', 'shixisheng.views.allcompany'),
    url(r'^youxiu$', 'shixisheng.views.youxiu'),
    url(r'^faq$', 'shixisheng.views.faq'),
    url(r'^x$', 'shixisheng.views.x'),
    url(r'^be$', 'shixisheng.views.be'),
    url(r'^be/(\w+)$', 'shixisheng.views.be'),
    url(r'^grjl/(\w+)$', 'shixisheng.views.grjl'),
    url(r'^zpxx/(\w+)$', 'shixisheng.views.zpxx'),






    url(r'^media/(?P<path>.*)$','django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^admin/', include(admin.site.urls)),
)
