from django import forms
from .models import EbookModel,FeedBack,EbookModel2,EbookModel3,EbookModel4



class UploadPdf(forms.ModelForm):
	class Meta:
		model=EbookModel
		fields=('title','pdf',)

class uploadpdf2(forms.ModelForm):
	class Meta:
		model=EbookModel2
		fields=('title','pdf',)

class uploadpdf3(forms.ModelForm):
	class Meta:
		model=EbookModel3
		fields=('title','pdf',)

class uploadpdf4(forms.ModelForm):
	class Meta:
		model=EbookModel4
		fields=('title','pdf',)


class Feed(forms.ModelForm):
	class Meta:
		model=FeedBack
		fields=('name','feedback',)