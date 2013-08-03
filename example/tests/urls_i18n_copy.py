"""
Exists to be able to test solid_i18n_patterns with modified settings.USE_I18N
"""

from django.conf.urls import patterns, url, include
from solid_i18n.urls import solid_i18n_patterns
from django.views.generic import TemplateView

urlpatterns = solid_i18n_patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"),
        name='about'),
)

# without i18n
urlpatterns += patterns('',
    url(r'^onelang/', TemplateView.as_view(template_name="onelang.html"),
        name='onelang'),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
