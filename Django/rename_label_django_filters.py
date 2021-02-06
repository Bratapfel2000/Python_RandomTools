#changes only name of field. Not working with dropdown menu
import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
	field_1 = django_filters.CharFilter(label='New Name')
	class Meta:
		model = Product
		exclude = ['image']
		#fields = '__all__'
		fields =  ['field_1']




#this works with dropdown
class ProductFilter(django_filters.FilterSet):
	LETTERS = (('KP', 'KP'),
                   ('A', 'A'),)
	field_1 = django_filters.ChoiceFilter(label='test123', choices=LETTERS)        
	class Meta:
		model = Product
		exclude = ['image']
		fields = '__all__'


#take in Product from models for dropdown menu
class ProductFilter(django_filters.FilterSet):
	field_1 = django_filters.ChoiceFilter(label='test123',choices=Product.LETTERS)        
	class Meta:
		model = Product
		exclude = ['image']
		fields = '__all__'
		#fields =  ['field_1']
