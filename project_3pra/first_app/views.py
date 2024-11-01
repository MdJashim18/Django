from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    d = {'Name' : 'Jashim','Age' : 24, 'lst' : ['Python','is','the','best'],'courses' :[
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
        {
            'id' : 4,
            'name' : 'c++',
            'fee' : 8000
        },
        {
            'id' : 5,
            'name' : 'java',
            'fee' :9000
        },
    ]}
    d['date'] = datetime.datetime.now()
    d['NameList'] = [
                {'name': 'Josh', 'age': 19},
                {'name': 'Dave', 'age': 22},
                {'name': 'Joe', 'age': 31},
            ]
    d['fruits'] = ['Apple', 'Mango', 'Orange']
    d['animal'] = [
        {'cat'},
        {'dog'},
        {'horse'},
    ]
    return render(request,'index.html',d)