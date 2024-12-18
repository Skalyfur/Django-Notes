from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note


# Create your views here.
def note_list(request):
    return HttpResponse("Esta es la lista de notas.")

def note_create(request):
    return HttpResponse("Aquí puedes crear una nota.")

def note_delete(request, note_id):
    return HttpResponse(f"Nota con ID {note_id} eliminada.")

def note_list(request):
    notes = Note.objects.all()  # Obtener todas las notas
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)  # Crear una nueva nota
        return redirect('note_list')  # Redirigir a la lista de notas
    return render(request, 'notes/notes_create.html')

def note_delete(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
        note.delete()  # Eliminar la nota
        return redirect('note_list')
    except Note.DoesNotExist:
        return HttpResponse("Nota no encontrada", status=404)