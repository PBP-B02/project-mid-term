import django_filters
from homepage.models import Search

class ListingFilter(django_filters.FilterSet):
    class Meta:
        
        model = Search
        fields = {
            'article_name' : ['exact'],
            
        }
