from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, reverse
from uploadfile.forms import DocumentForm
from django.contrib import messages


def home(request):
    template = loader.get_template('uploadfile/home.html')
    return HttpResponse(template.render({}, request))


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File Uploaded Successfully')
            return HttpResponseRedirect(reverse(""))
        else:
            if form.errors:
                messages.error(request, "File Not Uploaded successfully")
            return HttpResponseRedirect(reverse(""))
    else:
        form = DocumentForm()
    print(messages)
    return render(request, 'uploadfile/upload.html', {
        'form': form, messages: messages
    })
