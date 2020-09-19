from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User

# classes
class Noticias(models.Model):
    titulo_noticia = models.CharField(max_length=500)
    imagem_noticia = models.FileField(null=True, blank=True)
    texto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def get_absolute_url(self):
        return reverse('merlindjango:news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = ("Notícias")
        ordering = ['-created_at', ]

    def submit_noticias_db(self, titulo_noticia, imagem_noticia, texto, created_at):
        self.titulo_noticia = titulo_noticia
        self.imagem_noticia = imagem_noticia
        self.texto = texto
        self.created_at = created_at
        self.save()


class downloadableFiles(models.Model):
    titulo_versao = models.CharField(max_length=500)
    update_ficheiro = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    class Meta:
        verbose_name_plural = ("Downloads")
        ordering = ['-created_at', ]


class GSMModels(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    organism = models.CharField(max_length=500)
    publication = models.TextField()
    year = models.IntegerField()
    file = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('merlindjango:gsm_models', kwargs={'pk': self.id_modelo})

    class Meta:
        verbose_name_plural = ("GSMModels")

    def getmodel(self, identifier):
        try:
            return GSMModels.objects.get(id_modelo=identifier)
        except Exception as E:
            print(E)
            return None

    def get_model_by_name(self, name):
        return self.objects.get(name=name)

    def get_model_by_year(self, year):
        return self.objects.get(year=year)

    def get_model_by_user(self, user):
        return self.objects.get(user=user)

    def get_model_by_boolean(self):
        return self.objects.get(is_public=True)

    def submit_model_db(self, name, organism, publication, year, file, is_public, user):
        self.name = name
        self.organism = organism
        self.publication = publication
        self.year = year
        self.file = file
        self.is_public = is_public
        self.user = user
        self.save()

    def edit_model_db_name(self, modelID, new_name):
        model = self.getmodel(modelID)
        model.name=new_name
        model.save()

    def edit_model_db_organism(self, modelID, new_organism):
        model = self.getmodel(modelID)
        model.organism=new_organism
        model.save()

    def edit_model_db_publication(self, modelID, new_publication):
        model = self.getmodel(modelID)
        model.publication=new_publication
        model.save()

    def edit_model_db_year(self, modelID, new_year):
        model = self.getmodel(modelID)
        model.year=new_year
        model.save()

    def edit_model_db_file(self, modelID, new_file):
        model = self.getmodel(modelID)
        model.file=new_file
        model.save()

    def edit_model_db_is_public(self, modelID, novo_is_public):
        model = self.getmodel(modelID)
        model.is_public=novo_is_public
        model.save()

    def delete_model(self, modelId):
        model = self.getmodel(modelId)
        model.delete()

    def selection(self,user, id_modelo):
        userID = self.objects.get(user_id=user)
        userID.getmodel(id_modelo)
