# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from docView.form_transcriptr import TranscriptrForm
from django.http import HttpResponseRedirect
from docView.models import Transcriptions 
from datetime import datetime
from django.contrib.auth.decorators import login_required

def docViewer(request):
	if request.method == 'POST':
		form = TranscriptrForm(request.POST)
		if form.is_valid():
			#Here comes the stuff to save the content to the db
			ct = request.POST.get('content')
			dt = datetime.now()
			tr = Transcriptions(content = ct, date_created=dt)
			tr.save()
			print 'Saved transcription to database!'
			return HttpResponseRedirect('/docViewer/confirmation/')
	else:
		form = TranscriptrForm()


	return render_to_response('docviewer.html', {'form': form})
	#return HttpResponse("Hello! This is the Document Viewer!")

def confirmation(request):
	return render_to_response('confirmation.html')
                
                
from django import forms
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        rg_form = UserCreationForm(request.POST)
        if rg_form.is_valid():
            new_user = rg_form.save()
            return HttpResponseRedirect("/docViewer/confirmation")
    else:
        rg_form = UserCreationForm()
    return render_to_response("registration.html", {'form': rg_form,})

from django.contrib import auth

"""def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/docViewer/confirmation")
    return HttpResponseRedirect("/docViewer/invaliduser")
"""
def test_login(request):
    return render_to_response('signin/signin.html')

@login_required
def projects(request):
    userid = request.user.id 
    print request.user.email
    theuser = request.user.username
    return render_to_response('accounts/profile/project_overview.html', {'user': theuser})
