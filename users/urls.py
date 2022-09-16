from django.urls import path
from users.views import RegisterListView, Logout, LoginListView, ProfileFormView


app_name = 'users'

urlpatterns = [
   path('login/', LoginListView.as_view(), name='login'),
   path('register/', RegisterListView.as_view(), name='register'),
   path('profile/', ProfileFormView.as_view(), name='profile'),
   path('logout/', Logout.as_view(), name='logout')
]
