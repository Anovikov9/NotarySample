from django.urls import path
from .views import *
urlpatterns = [

    path('', index, name='home'),
    path('tarifs/', tarifs ,name='tarifs'),
    path('link/',HomeLink.as_view(), name = 'link'),
    path('feedback/',contactView, name = 'feedback'),
    path('contacts/',contacts, name = 'contacts'),
    path('category/', DocView.as_view(), name='category'),
    path('category/<int:category_id>/', DocByCategory.as_view(extra_context={'title' : 'Необходимые документы'}), name='category_id'),
    path('category/<int:category_id>/<int:pk>/', GetByDoc.as_view(), name='actions'),
path('yandex/', yandex, name='yandex'),


]
