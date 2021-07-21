from django.shortcuts import redirect, render, get_object_or_404
from .models import Idea
from .forms import IdeaForm

# Create your views here.

def idea_list(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/idea_list.html', context={'ideas': ideas})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/idea_detail.html', context={'idea':idea})

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('ideas:idea_detail', pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, template_name='ideas/idea_form.html', context={'form':form})
        
def idea_register(request):

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('ideas:idea_list')
    else:
        form = IdeaForm()
    return render(request, template_name='ideas/idea_form.html', context={'form':form})

def idea_delete(request, pk):
    idea = Idea.objects.get(pk=pk)
    idea.delete()
    return redirect('ideas:idea_list')