from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html')


def year_country_query(request):
	return render(request, 'year-country-query.html')


def year_sorted_output_query(request):
	return render(request, 'year-sorted-output-query.html')
