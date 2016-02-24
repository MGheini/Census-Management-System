from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'querysystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'queryservices.views.home'),
    url(r'^services/year-country-query', 'queryservices.views.year_country_query'),
    url(r'^services/year-sorted-output-query', 'queryservices.views.year_sorted_output_query'),
    url(r'^admin/', include(admin.site.urls)),
]
