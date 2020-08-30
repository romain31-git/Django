from django.forms.models import ModelForm
from .models import Student, Presence

class StudentForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Student

    # liste des champs A Editer
    fields  = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    )
class PresenceForm(ModelForm):
  
  class Meta(ModelForm):
    model = Presence

    fields = (
      
      "reason",
      "ismissing",
      "Date",
      "Student",
      
    )

