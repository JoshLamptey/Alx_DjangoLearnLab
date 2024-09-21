from django.urls import path
from .views import NotificationView

notification_list = NotificationView.as_view({
    'get': 'list',
    'post': 'create'
})

notification_detail = NotificationView.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})


urlpatterns = [
    path('/notifications/', notification_list , name='notification_list'),
    path('<int:pk>/', notification_detail, name='notification_detail'),
    path('mark_as_read/', NotificationView.as_view({'post': 'mark_as_read'}), name='notification-mark-as-read'),
]
