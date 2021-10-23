#Listen
Module = ['Statistik', 'Psychologie', 'Testtheroie']
Zeitraum = ['1xWoche', ' 1xMonat', 'unregelmäßig']
Uni = ['Dortmund', 'Iserlohn', 'Hagen']
Gruppeng = ["2", "3", "4"]
Grund = ["kennen", "austausch", "lernen"]

#Importing
import django_filter.rest_framework
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer
from rest_framework import generics
from rest_framework import filters

REST_FRAMEWORK = {'DEFAULT_FILTER_BACKENDS' : ['django_filter.rest_framework.DjangoFilterBackend']}

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filter.rest.framework.DjangoFilterBackend]
    filterset_fields = ['Module', 'Uni', 'Zeitraum']


#Suche
class CustomSearchFilter(filter.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
            return super(CustomSearchFilter, self).get_search_fields(view, request)


#html - should return rendered HTML string
to_html(self, request, queryset, view)
