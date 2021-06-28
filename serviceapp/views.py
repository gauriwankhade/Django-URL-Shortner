from django.shortcuts import render
from .serializers import *
from django.views import View
from rest_framework import generics, permissions
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.


# class LinkListView(APIView):
#     """
#     List all links, or create a new link.
#     """

#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         long_url = kwargs.get('slug')
#         short_url = get_shorturl()
#         data = {'long_url':long_url, 'short_url':short_url}
#         serializer = CreateLinkSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LinkDetailView(APIView):

#     def get(self, request, *args, **kwargs):
#         instance = Link.objects.get(kwargs.get('slug'))
#         serializer = RetrieveLinkSerializer(instance)
#         return JsonResponse(serializer.data)

class HomeView(View):

    def get(self, request, *args, **kwargs):
        form = UrlForm()
        context={
            "title":"Submit URL",
            "form": form
        }
        return render(request,'index.html',context)

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if form.is_valid():
            current_url=form.cleaned_data.get('url')
            obj = Link.objects.create(long_url=current_url)

            context={
                'object':obj,
            }
    
            return render(request, 'success.html',context)    

        return render(request, 'index.html',context)


def redirectView(request, url=None ,*args ,**kwargs ):
    try:
        obj = Link.objects.get(short_url=url)
        return HttpResponseRedirect(obj.long_url)
    except:
        return HttpResponse("URL DOES NOT EXIST")
        

class URLRetrieveView(generics.RetrieveAPIView):

    lookup_field = 'short_url'
    serializer_class = LinkSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Link.objects.all()


class URLCreateView(generics.CreateAPIView):

    lookup_field = 'short_url'
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = (permissions.AllowAny,)




