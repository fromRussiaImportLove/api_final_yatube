from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

API_VERSION = 'v1'

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('group', GroupViewSet)
router.register('follow', FollowViewSet)
router.register(r'posts/(?P<post_id>\d)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path(f'{API_VERSION}/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path(f'{API_VERSION}/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path(f'{API_VERSION}/', include(router.urls)),
]
