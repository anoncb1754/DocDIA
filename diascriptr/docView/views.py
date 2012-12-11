# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from docView.form_transcriptr import TranscriptrForm, ProjectForm
from django.http import HttpResponseRedirect
from docView.models import Transcriptions, Project, Page
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

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
            doc_1 = Page(page=request.POST.FILES['doc1'], date_created=date_created
                    project=project)

            #doc_2 = request.FILES['doc2']
            print 'THE DOCS:', doc_1
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
    user = request.user
    theuser = request.user.username
    project_list = Project.objects.filter(user=user)
    page_list = Page.objects.all()
    print page_list
    print 'THE PAGE LIST END'
    print project_list
    return render_to_response('accounts/profile/project_overview.html', 
            {'user': theuser, 'project_list': project_list, 'page_list': page_list})


@login_required
def create_project(request):
    user = request.user
    print 'testcall'
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project_name = request.POST.get('project_name')
            project_description = request.POST.get('project_description')
            visibility = int(request.POST.get('status'))
            date_created = datetime.now()
            project = Project(user=user, project_name=project_name, 
                    project_description=project_description,
                    visibility=visibility)
            project.save()
            print 'Project saved to db...'
            doc_1 = Page(page=request.FILES['doc_1'], date_created=date_created,
                    project=project)
            doc_1.save()
            print 'Doc saved to db...'

            #doc_2 = request.FILES['doc2']
            #print 'THE DOCS:', doc_1
            #project_list = Project.objects.filter(user=user)
            return HttpResponseRedirect("/accounts/profile/")
    else:
        print 'testcall2'
        form = ProjectForm()
        print 'testcall3'
    return render_to_response("accounts/profile/create_project.html", {'form': form})
