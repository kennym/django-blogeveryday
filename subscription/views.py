from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from google.appengine.api import users

from subscription.forms import SubscriberForm

def show_index(request, template_file="subscription/index.html"):
    user = users.get_current_user()
    if user:
        login_user = user.nickname()
        login_url = users.create_logout_url(reverse('show_index'))
    else:
        login_user = None
        login_url = users.create_login_url(reverse('show_index'))

    form = SubscriberForm()

    return render_to_response(
        template_file, 
        {
            "form": form,
            "login_user": login_user,
            "login_url": login_url,
        },
        context_instance=RequestContext(request)
    )

def submit_form(request, template_file="subscription/success.html"):
    user = users.get_current_user()
    if not user:
        login_url = users.create_logout_url(reverse('show_index'))
        return HttpResponseRedirect(login_url)

    if request.method == "POST":
        form = SubscriberForm(request.POST)
        user = users.get_current_user()
        if user is not None:
            if form.is_valid():
                form.save()
        else:
            return HttpResponseRedirect(reverse('show_index'))

    return render_to_response(
        template_file,
        context_instance=RequestContext(request)
    )
