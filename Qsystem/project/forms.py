# coding=utf-8
from django import forms

class changedesignForm(forms.Form):
	content=forms.CharField(required=True,error_messages={'invalid':u'变更内容不能为空'})
	dpath = forms.CharField(required=True,error_messages={'invalid':u'设计图地址不能为空'})
	changeid = forms.IntegerField(required=True)


class delayprojectForm(forms.Form):
	delay_date=forms.DateField(required=True,error_messages={'invalid':u'延期日期不能为空'})
	delay_reason = forms.CharField(required=True,error_messages={'invalid':u'延期理由不能为空'})
	delayid = forms.IntegerField(required=True)
