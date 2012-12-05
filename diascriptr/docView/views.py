# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from docView.form_transcriptr import TranscriptrForm
from django.http import HttpResponseRedirect
from docView.models import Transcriptions 
from datetime import datetime

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