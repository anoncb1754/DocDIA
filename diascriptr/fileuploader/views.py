# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from form_file_uploader import UploadFileForm
from models import Document

def fileuploader(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()
			return HttpResponseRedirect('/docViewer/confirmation/')
	else:
		form = UploadFileForm()
	return render_to_response('fileuploader.html', {'form':form})
