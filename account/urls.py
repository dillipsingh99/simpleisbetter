from django.urls import path
from . views import home, about, account, AccountUpdateView
urlpatterns = [
    path('', home,name='home'),
    path('about/', about, name='about'),
    path('account/<int:id>/', account, name='account'),
    # path('account_update/', account_update, name='update'),
    path('<int:pk>/update/', AccountUpdateView.as_view(), name='update'),
]