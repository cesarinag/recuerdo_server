from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.haiku_views import Haikus, HaikuDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('haikus/', Haikus.as_view(), name='haikus'),
    path('haikus/<int:pk>/', HaikuDetail.as_view(), name='haiku_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
