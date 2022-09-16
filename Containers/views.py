from django.http import JsonResponse

def imagens(request):
    if request.method == 'GET':
        imagem = {}
        return JsonResponse(imagem)