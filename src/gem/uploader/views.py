# -*- coding: utf-8 -*-
# Create your views here.
import logging
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.conf import settings
from django.shortcuts import render_to_response
from django.core.cache import cache

import os

from gem.uploader.core import handle_uploaded_file
from gem.uploader.forms import *


def index(request):
	
	if request.method == 'POST':
		print "POST: %s" % request.POST
		form = UploadFileForm(request.POST, request.FILES)
		print form
		if form.is_valid():
			print 'form eh valido'
			for key,value in request.POST.items():
				print key
				print value
				#files = request.FILES['file']
				files = request.FILES[key]
				handle_uploaded_file(files)
			return render_to_response("uploader/index.html", {'form': form, 'files' : "Ok"})
	else:
		form = UploadFileForm()
	return render_to_response("uploader/index.html", {'form': form})


"""
def index(request):

	if request.method == 'POST':
		print "POST: %s" % request.POST
		files = request.FILES['qqfile']
		handle_uploaded_file(files)
		return render_to_response("uploader/index.html", {'form': form, 'files' : files})
	else:
		form = UploadFileForm()
	return render_to_response("uploader/index.html", {'form': form})
"""