from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from download.models import FileHandler
from download.forms import FileHandlerForm

# Create your views here. Class hase view(CV)

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_files = FileHandler.objects.all

        context = {'form': FileHandlerForm, 'get_files': get_files}
        return context


    def post(self, request, **kwargs):
        context = {}
        if request.method == 'POST':
            form = FileHandlerForm(request.POST, request.FILES)

            if form.is_valid():
                FileHandler.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))

                return redirect('download:index')
            else:
                context['form'] = form
        else:
            context['form'] = form

        return redirect('download:index')