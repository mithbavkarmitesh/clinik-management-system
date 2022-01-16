
from django.contrib.auth import authenticate
from .models import blooddonation, criticalpatient, medicine,patient,notes
from django.contrib.auth.forms import AuthenticationForm
from django import forms



class UserLoginForm(AuthenticationForm):    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'unmae'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'pass',
        }
))

class medicineregister(forms.ModelForm):
    class Meta:
        model=medicine
        fields='__all__'
        widgets={
            'medicinename':forms.TextInput(attrs={'class':'form-control','placeholder':'Medicine Name'}),
            'brandname':forms.TextInput(attrs={'class':'form-control','placeholder':'Brandname'}),
            'medicinequantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'medicineprice':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price'}),
        }


class patientregister(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'
        widgets={
            'patient_firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName'}),
            'patient_middlename':forms.TextInput(attrs={'class':'form-control','placeholder':'MiddleName'}),
            'patient_lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'LastName'}),
            'patient_address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'patient_mobileno':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobileno' }),

        }



class notesregister(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'desc':forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
          
        }





class bloodregister(forms.ModelForm):
    class Meta:
        model=blooddonation
        fields='__all__'
        widgets={
            'patient_firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName'}),
            'patient_middlename':forms.TextInput(attrs={'class':'form-control','placeholder':'MiddleName'}),
            'patient_lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'LastName'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Addresss'}),
            'mobileno':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobileno'}),
            # 'bloodgroup':forms.TextInput(attrs={'class':'form-control','placeholder':'BloodGroup'}),
            'healthissue':forms.TextInput(attrs={'class':'form-control','placeholder':'HealthIssue'}),

        }





class criticalpatientregister(forms.ModelForm):
    class Meta:
        model=criticalpatient
        fields='__all__'
        widgets={
            'patient_firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName'},),
            'patient_middlename':forms.TextInput(attrs={'class':'form-control','placeholder':'MiddleName'}),
            'patient_lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'LasrName'}),
            'patient_address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'patient_mobileno':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobileno'}),
            'prescribedoctorname':forms.TextInput(attrs={'class':'form-control','placeholder':'PrescribeDoctor'}),
            'healthproblem':forms.TextInput(attrs={'class':'form-control','placeholder':'HealthProblem'}),

        }

        