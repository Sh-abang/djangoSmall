from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Entry
from .forms import EntryForm
from django.db.models import DateField
from django.contrib.auth.decorators import login_required

    
@login_required(login_url='login')
def index(request):
    entries_list = Entry.objects.filter(author=request.user).order_by('-created')
    context = {'user_specific_entries': entries_list}
    return render(request, "diary/index.html",context)


@login_required(login_url='login')
def entry(request, entry_id):
    try:
        entry = Entry.objects.get(pk = entry_id)
    except Entry.DoesNotExist:
        raise Http404("Entry does not exist :'(")
    return render(request, 'diary/entry.html', {'entry':entry})

    
@login_required(login_url='login')
def create_entry(request):
    createForm = EntryForm()

    if request.method == 'POST':
        createForm = EntryForm(request.POST)
        if createForm.is_valid():
            entryObject = createForm.save()
            # print(entryObject.title +"__++__"+str(request.user.email))
            entryObject.author = request.user
            entryObject.save()
            return redirect('/diary')
    context = {'form':createForm}
    return render(request,  "diary/create_entry.html",context)

@login_required(login_url='login')
def edit_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    form = EntryForm(instance=entry)
    if request.method == 'POST':
        createForm = EntryForm(request.POST, instance=entry)
        if createForm.is_valid():
            createForm.save()
            return redirect('/diary')
    context ={'form': form}
    return render(request, "diary/create_entry.html", context)

@login_required(login_url='login')
def delete(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    if request.method == "POST":
        entry.delete()
        return redirect('index')
    context = {'entry':entry}
    return render(request, 'diary/delete.html',context)

@login_required(login_url='login')
def profile(request):
    return render(request, "diary/profile.html", {})