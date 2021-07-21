from django.shortcuts import redirect, render, get_object_or_404
from .models import DevTool
from .forms import DevToolForm
from ideas.models import Idea
# Create your views here.

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'devtools/devtool_list.html', context={'devtools': devtools})

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    ideas = Idea.objects.all()
    return render(request, 'devtools/devtool_detail.html', context={'devtool':devtool, 'ideas':ideas})

def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)

    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtools:devtool_detail', pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, template_name='devtools/devtool_form.html', context={'form':form})

def devtool_register(request):

    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtools:devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm()
    return render(request, template_name='devtools/devtool_form.html', context={'form':form})

def devtool_delete(request, pk):
    devtool = DevTool.objects.get(pk=pk)
    devtool.delete()
    return redirect('devtools:devtool_list')