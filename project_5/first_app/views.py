from django.shortcuts import render
from .forms import contactForm
from .forms import StudentForm,passwordValidationProject
def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name' : name, 'email': email , 'select' : select})
    else:
        return render(request, 'about.html')
    

def submit_form(request):
    return render(request,'form.html')

def DjangoForm(request):
    print(request.POST)
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # file_path = './first_app/upload/' + file.name
            # with open(file_path, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
        # return render(request,'djangoForm.html',{'form' : form})
    else:
        form = contactForm()
    
    return render(request,'djangoForm.html',{'form' : form})


def student_form_view(request):  # Updated function name
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'djangoForm.html', {'form': form})


def passwordValidation(request):  
    if request.method == 'POST':
        form = passwordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()
    return render(request, 'djangoForm.html', {'form': form})
    