import django_filters

from .models import *

class ProductFilter(django_filters.FilterSet):
	field_1 = django_filters.CharFilter(label='New Name')
	class Meta:
		model = Product
		exclude = ['image']
		#fields = '__all__'
		fields =  ['field_1']