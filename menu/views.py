from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .serializers import MenuSerializer
from .models import Menu

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# ctrl + k + c == 주석처리
# ctrl + k + u == 주석해제
# def menus(request):
#   mymenus = Menu.objects.all().values()
#   template = loader.get_template('all_menus.html')
#   context = {
#     'mymenus': mymenus,
#   }
#   return HttpResponse(template.render(context, request))
  
# def details(request, id):
#   mymenu = Menu.objects.get(id=id)
#   template = loader.get_template('details.html')
#   context = {
#     'mymenu': mymenu,
#   }
#   return HttpResponse(template.render(context, request))
  
# def main(request):
#   template = loader.get_template('main.html')
#   return HttpResponse(template.render())