from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' : 15 ,'lst' : ['python','is','best'] , 'course' : [
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 6000
        },
        {
            'id' : 3,
            'name' : 'c',
            'fee' : 7000
        },
    ]}
    return render(request,'home.html',d)