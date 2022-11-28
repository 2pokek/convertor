from django.shortcuts import render

def exchange(request):
    name= 'mr'

    context = {
        'name' : name
    }

    return render(request=request,template_name='exchange/index.html',context=context)