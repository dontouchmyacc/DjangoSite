from django.shortcuts import render

def index(requests):
    data ={
        'title':'Главная страница',
        'values':['Some','Hello','Python'],
        'obj':{
            'car':'Audi',
            'age': 21,
            'hobby':'Programmer'
        }
    }
    return render(requests, 'main/index.html', data)

def about(requests):
    return render(requests, 'main/about.html')

def contacts(requests):
    return render(requests, 'main/contacts.html')