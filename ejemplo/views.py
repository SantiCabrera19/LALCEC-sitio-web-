from django.shortcuts import render

# Create your views here.
def noticia_list(request):

    return render(request, 'ejemplo/post_list.html', {})