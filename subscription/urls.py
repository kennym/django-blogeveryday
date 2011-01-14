from django.conf.urls.defaults import *

urlpatterns = patterns('subscription.views',
    url(r'submit_form/$', "submit_form", name="submit_form"),
    url(r'$', "show_index", name="show_index"),
)
