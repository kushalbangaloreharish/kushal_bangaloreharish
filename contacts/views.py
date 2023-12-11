# contacts/views.py
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm  # We'll create this form in the next step

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'create.html', {'form': form})

def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'detail.html', {'contact': contact})

def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit.html', {'form': form})

def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete.html', {'contact': contact})

