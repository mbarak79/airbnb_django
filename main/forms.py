from django import forms
from .models import Property_book
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Property_book
        fields = ["date_from", "date_to", "guest", "children"]

        widgets = {
            'date_to': DateInput(),
            'date_from': DateInput(),
        }
