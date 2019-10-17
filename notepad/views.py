from django.shortcuts import render,redirect,get_object_or_404
from .forms import NoteForm
from .models import Note

#create
def create_view(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, "notepad/create.html", context)
  
def list_view(request):
    notes = Note.objects.all()
    context = {'notes':notes}
    return render(request,'notepad/list.html',context)

def delete_view(request,abc):
    note2bedeleted = Note.objects.filter(pk = abc)
    if note2bedeleted.exists():
        if request.user == note2bedeleted[0].user:
            note2bedeleted[0].delete()
    return redirect('list')

def update_view(request,abc):
    note2beupdated = get_object_or_404(Note,id = abc)
    form = NoteForm(request.POST or None, instance= note2beupdated)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('list')
    context = {'form':form}
    return render(request, "notepad/create.html", context)

