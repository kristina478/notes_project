from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Мои заметки</h1><p>Скоро здесь будет список.</p>")