from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import reverse_lazy

urlpatterns = [
    path('accounts', include(('django.contrib.auth.urls', 'auth'),
                             namespace='accounts')),
    path('reset/', views.PasswordResetView.as_view(success_url=reverse_lazy(
        'accounts:password_reset_done')), name='password_reset'),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy('accounts:password_reset_complete')
         ), name='password_reset_confirm'
         ),
    path('password_change', views.PasswordChangeView.as_view(
        success_url=reverse_lazy(
            'accounts:password_change_done')
    ), name='password_change'),
    path('admin/', admin.site.urls),
    path('', include('reviews.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
