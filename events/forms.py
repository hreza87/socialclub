from django import forms
from django.forms import ModelForm
from .models import Venue, Event

#Create a venue form

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','venue','manager','attendees','description')
        labels = {
            'name': '' ,
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'select Venue',
            'manager': 'choose Management',
            'attendees': 'Add attendees',
            'description': 'Add Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Event date'}),
            'venue': forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'manager': forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),



        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','zip_code','phone','web','email_address')
        labels = {
            'name': '' ,
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control','placeholder':'webaddress'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),



        }