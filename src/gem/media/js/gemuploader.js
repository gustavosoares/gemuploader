
$(document).ready(function() {
  
/*
Documentation for the fileuploader plugin http://valums.com/ajax-upload/
*/
	var uploader = new qq.FileUploader({
		element: document.getElementById('file-uploader'),
		allowedExtensions: [],
		action: '/uploader'
	});
	
});