from django.conf import settings

def handle_uploaded_file(f):
	
	f_name = f.name
	f_size = f.size
	print "Filename: %s -> size: %s" % (f_name, f_size)
	destination = open(settings.FILE_SAVE_DIR + '/' + f.name, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()