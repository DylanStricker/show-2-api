from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.show_views import Shows, ShowDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('shows/', Shows.as_view(), name='shows'),
    path('shows/<int:pk>/', ShowDetail.as_view(), name='show_detail'),
]
