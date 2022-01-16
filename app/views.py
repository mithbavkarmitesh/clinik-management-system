from django.contrib.auth import forms
from django.forms.widgets import Media
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import request,HttpResponseRedirect
from .forms import  criticalpatientregister, medicineregister, notesregister, patientregister,notesregister,UserLoginForm,bloodregister
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from app.models import *
from django.contrib import messages 


# Create your views here.

# ====================================================loginfrom=========================================
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            val2=UserLoginForm(request,data= request.POST)  
            if val2.is_valid():
                uname=val2.cleaned_data['username']
                upas=val2.cleaned_data['password']
                user=authenticate(username=uname,password=upas)
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.INFO,"Login Succesfully to System")
                    return HttpResponseRedirect('/clinik/')
    
        else:
            val2=UserLoginForm()
        return render(request,'app/loginform.html',{'form':val2})
    else:
        return HttpResponseRedirect('/login/') 



def user_logout(request):
    logout(request)
    messages.add_message(request,messages.INFO,"Succesfully Logout")
    return HttpResponseRedirect('/clinik/')



def home(request):
    return render(request,'app/home.html')
    
# =====================================patient section============================================
def patientadd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            val=patientregister(request.POST)
            if val.is_valid():
                pfname=val.cleaned_data['patient_firstname']
                pmname=val.cleaned_data['patient_middlename']
                plname=val.cleaned_data['patient_lastname']
                padd=val.cleaned_data['patient_address']
                pmn=val.cleaned_data['patient_mobileno']
                if len(str(pmn))!=10:
                    messages.error(request,'Invalid Mobile Number')
                    return redirect("/clinik/patientadd")                   
                data=patient(patient_firstname=pfname,patient_middlename=pmname,patient_lastname=plname,patient_address=padd,patient_mobileno=pmn)
                data.save()
                val=patientregister()#when execution done then black form pop up
        else:
            val=patientregister()
        return render(request,'app/patient/patientadd.html',{'fm':val})
    
    else:
        return HttpResponseRedirect('/login')


def patientdetails(request):
    if request.user.is_authenticated:
        pdata=patient.objects.all()
        return render(request,'app/patient/patientdetails.html',{'dt':pdata})
    else:
        return HttpResponseRedirect('/login')

def pdelete(request,id):
    data=patient.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/clinik/patientdetails')


def pupdate(request,id):
    if request.method == 'POST':
        data=patient.objects.get(pk=id)
        fm=patientregister(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
        return redirect("/clinik/patientdetails/")
    else:
        data=patient.objects.get(pk=id)
        
    fm=patientregister(instance=data)
    return render(request,'app/patient/updatep.html',{'form':fm})






# =============================medicine secion===================================================
def medicineadd(request):
    if request.user.is_authenticated:
            if request.method == 'POST':
                val=medicineregister(request.POST)
                if val.is_valid():
                    mname=val.cleaned_data['medicinename']
                    bname=val.cleaned_data['brandname']
                    mqua=val.cleaned_data['medicinequantity']
                    mprice=val.cleaned_data['medicineprice']
                    data=medicine(medicinename=mname,brandname=bname,medicinequantity=mqua,medicineprice=mprice)
                    data.save()
                    val=medicineregister()#when execution done then black form pop up
            else:
                val=medicineregister()
            return render(request,'app/medicine/medicineadd.html',{'fm':val})
    else:
        return HttpResponseRedirect('/login')






def medicinedetails(request):
    if request.user.is_authenticated:
        value=medicine.objects.all()
        return render(request,'app/medicine/medicinedetails.html',{'value':value})
    else:
        return HttpResponseRedirect('/login')

def mdelete(request,id):
    data=medicine.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/clinik/medicinedetails')

def mupdate(request,id):
    if request.method == 'POST':
        data=medicine.objects.get(pk=id)
        fm=medicineregister(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
        return redirect("/clinik/medicinedetails/")
    else:
        data=medicine.objects.get(pk=id)
        
    fm=medicineregister(instance=data)
    return render(request,'app/medicine/updatem.html',{'form':fm})


# ===========================================serach==========================
def search_patient(request):
    if request.method == 'POST':
        searched=request.POST['searchp']
        result=patient.objects.filter(patient_firstname__contains=searched)
        return render(request,'app/patient/search_patient.html',{'result':result})
    else:
        return render(request,'app/patient/search_patient.html')


def search_medicine(request):
    if request.method == 'POST':
        searched=request.POST['searchm']
        result=medicine.objects.filter(medicinename__contains=searched )
        return render(request,'app/medicine/search_medicine.html',{'result':result})
    else:
        return render(request,'app/medicine/search_medicine.html')

def search_bloodcamp(request):
    if request.method == 'POST':
        searched=request.POST['searchb']
        re=blooddonation.objects.filter(bloodgroup__contains=searched)
        # re=blooddonation.objects.filter(__contains=searched)
        
        return render(request,'app/bd/search_b.html',{'re':re})
    else:
        return render(request,'app/bd/search_b.html')

def search_notes(request):
    if request.method == 'POST':
        searched=request.POST['searchn']
        re=notes.objects.filter( title__contains=searched)
        return render(request,'app/note/search_n.html',{'result':re})
    else:
        return render(request,'app/note/search_n.html')


def search_criticalpatient(request):
    if request.method == 'POST':
        searched=request.POST['searchcp']
        re=criticalpatient.objects.filter( patient_firstname__contains=searched)
        return render(request,'app/criticalpatient/search_cp.html',{'result':re})
    else:
        return render(request,'app/criticalpatient/search_cp.html')



def pres_history(request):
    if request.method == 'POST':
        searched=request.POST['searchh']
        re=receiptHistory.objects.filter( username__contains=searched)
        re2=medicineoutsideHistory.objects.filter(time__contains=searched)
        return render(request,'app/prescription/search_h.html',{'result':re,'result2':re2})
    else:
        return render(request,'app/prescription/search_h.html')

# ==========================blood donation===================================
def blood(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            val=bloodregister(request.POST)
            if val.is_valid():
                pfname=val.cleaned_data['patient_firstname']
                pmname=val.cleaned_data['patient_middlename']
                plname=val.cleaned_data['patient_lastname']
                padd=val.cleaned_data['address']
                pmn=val.cleaned_data['mobileno']
                if len(str(pmn))!=10:
                    messages.error(request,'Invalid Mobile Number')
                    return redirect("/clinik/bd")    
                
                phi=val.cleaned_data['healthissue']

    
                data=blooddonation(patient_firstname=pfname,patient_middlename=pmname,patient_lastname=plname,address=padd,mobileno=pmn,healthissue=phi)
                data.save()
                val=bloodregister()#when execution done then black form pop up
        else:
            val=bloodregister()
        return render(request,'app/bd/bd.html',{'fm':val})
    
    else:
        return HttpResponseRedirect('/login')



def bddetails(request):
    if request.user.is_authenticated:
        val=blooddonation.objects.all()
        return render(request,'app/bd/bddetails.html',{'re':val})
    else:
        return HttpResponseRedirect('/login')


def bupdate(request,id):
    if request.method == 'POST':
        data=blooddonation.objects.get(pk=id)
        fm=bloodregister(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
        return redirect("/clinik/bd1/")
    else:
        data=blooddonation.objects.get(pk=id)
    fm=bloodregister(instance=data)
    return render(request,'app/bd/updateb.html',{'form':fm})


def bdelete(request,id):
    data=blooddonation.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/clinik/bd1')


# ===================================notes====================================
def note(request):
    if request.user.is_authenticated:
        bdata=notes.objects.all()
        return render(request,'app/note/notes.html',{'dt':bdata})
    else:
        return HttpResponseRedirect('/login')


def add_note(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            val=notesregister(request.POST)
            if val.is_valid():
                title=val.cleaned_data['title']
                desc=val.cleaned_data['desc']    
                data=notes(title=title,desc=desc)
                data.save()
                val=notesregister()#when execution done then black form pop up
        else:
            val=notesregister()
        return render(request,'app/note/noteadd.html',{'fm':val})
    
    else:
        return HttpResponseRedirect('/login')


def ndelete(request,id):    
    data=notes.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/clinik/notes')


def nupdate(request,id):
    if request.method == 'POST':
        data=notes.objects.get(pk=id)
        fm=notesregister(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
        return redirect("/clinik/notes/")
    else:
        data=notes.objects.get(pk=id)
    fm=notesregister(instance=data)
    return render(request,'app/note/updaten.html',{'form':fm})



# =======   ====================medicineinside and priting recepit=====================================
def print(request):
    bills=receipt.objects.all()
    name=bills[0].username
    outsideBill = medicineoutside.objects.all()
    ddetails=doctorsdetails.objects .all()
    total=sum([i.medicineprice for i in bills])
    para={'bills':bills,'uname':name,'outsideMed':outsideBill,'ddetails':ddetails,'total':total}
    return render(request,'app/prescription/receipt.html',para)

def billprint(request):
    bills=receipt.objects.all()
    outsideBill = medicineoutside.objects.all()
    name = bills[0].username
    return render(request,'app/prescription/bill.html',{'bills':bills,'uname':name,'outsideMed':outsideBill})


def receiptprint(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data=receipt.objects.all()
            data2=medicineoutside.objects.all()
            uname=request.POST.get('username')
            for i in data:
                i.delete()
            for i in data2:
                i.delete()   
            mn1=request.POST.get('med_1')
            mt1=request.POST.get('med_1_time')
            mp1=request.POST.get('price_1')

            mn2=request.POST.get('med_2')
            mt2=request.POST.get('med_2_time')
            mp2=request.POST.get('price_2')

            
            mn3=request.POST.get('med_3')
            mt3=request.POST.get('med_3_time')
            mp3=request.POST.get('price_3')

            
            mn4=request.POST.get('med_4')
            mt4=request.POST.get('med_4_time')
            mp4=request.POST.get('price_4')
            
            out_med_name = request.POST.get("med_5")
            out_med_time = request.POST.get("time_5")
            
            if out_med_name != "":
                obj = medicineoutside(username=uname,ousidemedicinename = out_med_name, ousidemedicinetime = out_med_time)
                obj.save()
            if out_med_name !="":
                obj2 = medicineoutsideHistory(username=uname,ousidemedicinename = out_med_name, ousidemedicinetime = out_med_time)
                obj2.save()

        

            if mn1 !="" :
                re_1=receipt(username=uname,medicinename=mn1,medicinetiming=mt1,medicineprice=mp1)
                re_1.save()
                reH_1=receiptHistory(username=uname,medicinename=mn1,medicinetiming=mt1,medicineprice=mp1)
                reH_1.save()
                
                if mn2 !="" :
                    re_2=receipt(username=uname,medicinename=mn2,medicinetiming=mt2,medicineprice=mp2)
                    re_2.save()

                    reH_2=receiptHistory(username=uname,medicinename=mn2,medicinetiming=mt2,medicineprice=mp2)
                    reH_2.save()
                    
                    if mn3 !="" :
                        re_3=receipt(username=uname,medicinename=mn3,medicinetiming=mt3,medicineprice=mp3)
                        re_3.save()
                        reH_3=receiptHistory(username=uname,medicinename=mn3,medicinetiming=mt3,medicineprice=mp3)
                        reH_3.save()
                        
                        if mn4 !="" :
                            re_4=receipt(username=uname,medicinename=mn4,medicinetiming=mt4,medicineprice=mp4)
                            re_4.save()
                            reH_4=receiptHistory(username=uname,medicinename=mn4,medicinetiming=mt4,medicineprice=mp4)
                            reH_4.save()
            else:
                return redirect('/clinik/rprint')
            url = "/clinik/bill/"
            return redirect(url)	
        return render(request,'app/prescription/medicine_inside.html')
    else:
        return HttpResponseRedirect('/login')

            
        

def history(request):
    if request.user.is_authenticated:
        r_history = receiptHistory.objects.all()
        med_out_history = medicineoutsideHistory.objects.all()

        return render(request,"app/prescription/history.html",{'reciepts':r_history,'out_meds':med_out_history})
    else:
        return HttpResponseRedirect('/login')

        
    
        
    
 
# ==================================critical patient==========================================
def criticalpatientadd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            val=criticalpatientregister(request.POST)
            if val.is_valid():
                cpfname=val.cleaned_data['patient_firstname']
                cpmname=val.cleaned_data['patient_middlename']
                cplname=val.cleaned_data['patient_lastname']
                cpadd=val.cleaned_data['patient_address']
                cpmn=val.cleaned_data['patient_mobileno']
                if len(str(cpmn))!=10:
                    messages.error(request,'Invalid Mobile Number')
                    return redirect("/clinik/cpatientadd")    
                cpd=val.cleaned_data['prescribedoctorname']
                cphi=val.cleaned_data['healthproblem']
                data=criticalpatient(patient_firstname=cpfname,patient_middlename=cpmname,patient_lastname=cplname,patient_address=cpadd,patient_mobileno=cpmn,prescribedoctorname=cpd,healthproblem=cphi)
                data.save()
                val=criticalpatientregister()#when execution done then black form pop up
        else:
            val=criticalpatientregister()
        return render(request,'app/criticalpatient/cpatientadd.html',{'fm':val})
    
    else:
        return HttpResponseRedirect('/login')


def criticalpatientdetails(request):
    if request.user.is_authenticated:
        pdata=criticalpatient.objects.all()
        return render(request,'app/criticalpatient/cpatientdetails.html',{'dt':pdata})
    else:
        return HttpResponseRedirect('/login')

def cpdelete(request,id):
    data=criticalpatient.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/clinik/cpatientdetails')


def cpupdate(request,id):
    if request.method == 'POST':
        data=criticalpatient.objects.get(pk=id)
        fm=criticalpatientregister(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
        return redirect("/clinik/cpatientdetails/")
    else:
        data=criticalpatient.objects.get(pk=id)       
    fm=criticalpatientregister(instance=data)
    return render(request,'app/criticalpatient/updatecp.html',{'form':fm})

