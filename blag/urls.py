from django.conf.urls import patterns, include, url
from webapp import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^new$', 'webapp.views.new_post'),
    url(r'signup$', 'webapp.views.signup'),
    url(r'^$', 'webapp.views.all_posts'),
    url(r'^post/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)$', 'webapp.views.single_post'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
