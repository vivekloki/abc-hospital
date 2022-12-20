from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields="__all__"
        widgets={
            'booking_date':DateInput(),
        }
        labels={
            'p_name':"Enter your name",
            'p_phone':"Enter your phone number",
            'p_email':'Enter your email',
            'doc_name':'Doctors name',
            'booking_date':'Booking date',
            'booked_on':'Booked on',
            'dpt_name':'Department',
        }