from django.conf.urls.defaults import *

urlpatterns = patterns('mailng.extensions.amavis_quarantine.main',
                       (r'^$', 'index'),
                       (r'^listing/$', '_listing'),
                       (r'^getmailcontent/(?P<mail_id>[\w\-\+]+)/$', 'getmailcontent'),
                       (r'^(?P<mail_id>[\w\-\+]+)/headers/$', 'viewheaders'),
                       (r'^process/$', 'process'),
                       (r'^delete/(?P<mail_id>[\w\-\+]+)/$', 'delete'),
                       (r'^release/(?P<mail_id>[\w\-\+]+)/$', 'release'),
                       (r'^search/', 'search'),
                       (r'^(?P<mail_id>[\w\-\+]+)/$', 'viewmail'), 
                       )
