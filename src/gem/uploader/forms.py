from django import forms

class UploadFileForm(forms.Form):
	#title = forms.CharField(widget=forms.TextInput(attrs={'size':'50'}))
	#file  = forms.Field(widget=forms.FileInput, required=True)
	#file  = forms.FileField()
	file01  = forms.Field(widget=forms.FileInput, required=True, label="File - 1")
	file02  = forms.Field(widget=forms.FileInput, required=False, label="File - 2")
	file03  = forms.Field(widget=forms.FileInput, required=False, label="File - 3")
	file04  = forms.Field(widget=forms.FileInput, required=False, label="File - 4")
	file05  = forms.Field(widget=forms.FileInput, required=False, label="File - 5")
	file06  = forms.Field(widget=forms.FileInput, required=False, label="File - 6")
	file07  = forms.Field(widget=forms.FileInput, required=False, label="File - 7")
	file08  = forms.Field(widget=forms.FileInput, required=False, label="File - 8")
	file09  = forms.Field(widget=forms.FileInput, required=False, label="File - 9")
	file10  = forms.Field(widget=forms.FileInput, required=False, label="File - 10")