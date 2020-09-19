from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'merlindjango'

urlpatterns = [
    # # /news/
    path('news/', views.news, name='news'),
    #
    # # /home
    path('', views.home, name='home'),
    #
    # # /about
    path('about/', views.aboutmerlin, name='about_merlin'),
    #
    # # /description
    path('description/', views.description, name='description'),
    #
    # # /downloads
    path('downloads/', views.downloads, name='downloads'),
    path('downloads/<path>', views.download_version, name='download_version'),
    #
    # # /team
    path('team/', views.team, name='team'),
    #
    # # /tutorial
    path('tutorial/', views.tutorial, name='tutorial'),
    #
    # # /user
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    #
    # # /models
    path('gsm_models/', views.gsmmodels, name='gsm_models'),
    path('form_submit_model/', views.submit_model, name='submit_model'),
    path('delete_model/<int:id_modelo>', views.delete_model, name='delete_model'),
    path('download/<path>', views.download_model, name='download_model'),
    path('form_edit_model/<int:id_modelo>', views.edit_model, name='edit_model'),
    #
    # # /memote
    path('memote/<int:id_modelo>', views.submitMemote, name='submitMemote'),
    path('memote_status/<e_mail>/<int:submissionID>', views.display_results_wrapper, name='memote_status'),
    path('memote_download/<content>', views.display_results_wrapper, name='memote_download')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
