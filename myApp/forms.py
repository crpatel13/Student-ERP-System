from django import forms
from myApp.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields =['subject','intro_course','time','avg_age']
        widgets = {'time': forms.RadioSelect()}
        labels = {'time':'Preferred Time', 'intro_course':'This should be an introductory level course', 'avg_age':'What is your age?'}


class InterestForm(forms.Form):

    #interested = forms.IntegerField(default=1, choices=Interested_Choice, widget=forms.RadioSelect(), label='Interested')
    interested = forms.ChoiceField(widget=forms.RadioSelect(), label='Interested', choices=((0,'No'),(1,'Yes')))
    age = forms.IntegerField(initial=20, label='Age')
    comments = forms.CharField(widget=forms.Textarea, label='Additional Comments', required=False)