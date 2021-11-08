from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',include('app.urls'))
=======
    path('',include('app.urls')),
>>>>>>> 188199b0c779bce844f35f319a00cb288a8c15eb
]
