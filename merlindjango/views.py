from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, ModelForm
from .models import GSMModels, Noticias, downloadableFiles
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseForbidden
from itertools import chain
import requests
import os
import shutil


def news(request):
    template_name = 'merlindjango/news.html'
    noticia = Noticias.objects.order_by('-created_at')
    return render(request, template_name, {'noticia': noticia})


def home(request):
    template_name = 'merlindjango/home.html'
    return render(request, template_name)


def aboutmerlin(request):
    template_name = 'merlindjango/about_merlin.html'
    return render(request, template_name)


def description(request):
    template_name = 'merlindjango/description.html'
    return render(request, template_name)


def downloads(request):
    template_name = 'merlindjango/downloads.html'
    download = downloadableFiles.objects.order_by('-created_at')
    return render(request, template_name, {'download': download})


def download_version(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        response = HttpResponse(content_type='force-download')
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    raise Http404


def team(request):
    template_name = 'merlindjango/team.html'
    return render(request, template_name)


def tutorial(request):
    template_name = 'https://merlin-sysbio.org/tutorial.html'
    return redirect(template_name)


def register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password, first_name=first_name, last_name=last_name)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'merlindjango/home.html')
    context = {"form": form}
    return render(request, 'merlindjango/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                userName = user.first_name
                userId = user.pk
                context = {"userId": userId, "userName": userName}
                return render(request, 'merlindjango/home.html', context)
            else:
                return render(request, 'merlindjango/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'merlindjango/login.html', {'error_message': 'Invalid login'})
    return render(request, 'merlindjango/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'merlindjango/home.html', context)


def submit_model(request):
    if request.user.is_authenticated:
        form = ModelForm(request.POST, request.FILES or None)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            return gsmmodels(request, True)
        return render(request, 'merlindjango/form_submit_model.html', {'form': form})
    else:
        return render(request, 'merlindjango/login.html')


def delete_model(request, id_modelo):
    if request.user.is_authenticated:
        m = GSMModels()
        modelInDatabase = m.getmodel(id_modelo)
        if modelInDatabase.user == request.user or request.user.is_superuser:
            m.delete_model(id_modelo)
            return gsmmodels(request)
    else:
        return render(request, 'merlindjango/login.html')


def download_model(request, path):
    if request.user.is_authenticated:
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            response = HttpResponse(content_type='force-download')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        raise Http404
    else:
        return render(request, 'merlindjango/login.html')


def edit_model(request, id_modelo):
    if request.user.is_authenticated:
        m = GSMModels()
        modelindb = m.getmodel(id_modelo)
        if modelindb.user == request.user or request.user.is_superuser:
            form = ModelForm(request.POST, request.FILES or None, instance=modelindb)
            if form.is_valid():
                model = form.save(commit=False)
                model.save()
                return gsmmodels(request)
            return render(request, 'merlindjango/form_edit_model.html', {'form': form})
        else:
            return HttpResponseForbidden("")
    else:
        return render(request, 'merlindjango/login.html')


def gsmmodels(request, submitted=False):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            template_name = 'merlindjango/gsm_models.html'
            model = GSMModels.objects.all()
            return render(request, template_name, {'model': model, "submittedHTML": submitted})
        else:
            template_name = 'merlindjango/gsm_models.html'
            i = GSMModels.objects.filter(user=request.user)
            j = GSMModels.objects.filter(is_public=True)
            model = list(set(chain(i, j)))
            return render(request, template_name, {'model': model, "submittedHTML": submitted})
    else:
        return render(request, 'merlindjango/login.html')


def submitMemote(request, id_modelo):

    if request.user.is_authenticated:

        model_path = os.path.join(settings.MEDIA_ROOT, GSMModels.objects.filter(pk=id_modelo)[0].file.name)
        new_model_path = os.path.join(settings.MEDIA_ROOT, 'temp_model')
        new_model_path_2 = os.path.join(new_model_path, 'model.xml')

        if os.path.exists(new_model_path):
            shutil.rmtree(new_model_path, ignore_errors=True)

        os.mkdir(new_model_path)
        shutil.copy(model_path, new_model_path_2)

        e_mail = request.user.email
        data_auth_path = os.path.join(settings.MEDIA_ROOT, 'data_authorization.txt')

        data_auth_file = open(new_model_path_2, 'rb')
        model_file = open(data_auth_path, 'rb')
        files = [('files', data_auth_file),
                 ('files', model_file)]
        try:
            r = requests.post('http://palsson.di.uminho.pt:6082/submitMerlinPlugin/Memote/' + e_mail, files=files)
            data_auth_file.close()
            model_file.close()
        except:

            data_auth_file.close()
            model_file.close()

            if os.path.exists(new_model_path):
                shutil.rmtree(new_model_path, ignore_errors=True)

            return render(request, 'merlindjango/memote_fail.html')

        if r.status_code == 201:
            submissionID = eval(r.text).get('submissionID')

            if os.path.exists(new_model_path):
                shutil.rmtree(new_model_path, ignore_errors=True)

            return display_results_wrapper(request, e_mail, int(submissionID))
        else:

            if os.path.exists(new_model_path):
                shutil.rmtree(new_model_path, ignore_errors=True)

            return render(request, 'merlindjango/memote_fail.html')

    else:
        return render(request, 'merlindjango/login.html')


def display_results_wrapper(request, e_mail, submissionID):

    if request.user.is_authenticated:

        try:
            r = requests.get('http://palsson.di.uminho.pt:6082/status/' + str(e_mail) + '/' + str(submissionID))
        except:
            return render(request, 'merlindjango/memote_fail.html')

        ok_status_code = [202, 201]

        if r.status_code == 200:
            context = {'content': 'http://palsson.di.uminho.pt:6082/download/' + str(e_mail) + '/' + str(submissionID)}
            return render(request, 'merlindjango/submission_download.html', context)

        elif r.status_code in ok_status_code:
            return render(request, 'merlindjango/status.html', {'email': e_mail, 'submissionID': submissionID})

        else:
            return render(request, 'merlindjango/memote_fail.html')

    else:
        return render(request, 'merlindjango/login.html')
