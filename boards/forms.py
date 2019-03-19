from django import forms
from .models import Board
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# form 을 상속받아썼음
# class BoardForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=10,
#                             error_messages={'required': '제목을 반드시 입력해주세요.'})
#     content = forms.CharField(label='내용',
#                             error_messages={'required': '내용을 반드시 입력해주세요.'},
#                             widget=forms.Textarea(attrs={
#                                     'placeholder': '내용을 입력해줘!',
#                                     'class': 'input-box'  
#                                     })
#                             )
                                    
                                    
# modelform
# board를 조작하기 위해서 모델을 사용함.
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields='__all__'
        # fields = ['title','content']
        widgets = {'title' : forms.TextInput(attrs={
                                            'placeholder':'제목을 입력해주세요.',
                                            'class':'title'
                                            }),
                    'content':forms.Textarea(attrs={
                                            'placeholder':'내용을 입력해주세요',
                                            'class':'content'})
                     }
        error_messages = {'title':{
                                'required': '제목을 반드시 입력해주세요'
                            },
                            'content':{
                                'required' : '내용을 반드시 입력해주세요'
                            }
                        }   
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.add_input(Submit('submit', '제출~!'))
            