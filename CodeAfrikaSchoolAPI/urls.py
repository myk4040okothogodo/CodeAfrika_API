from rest_framework.routers import DefaultRouter
from .Community.views import  CommunityViewSet
from .Projects.views import ProjectViewSet
from .user.views import UserViewSet
from .Posts.views import PostViewSet
from .Courses.views import CourseViewSet

router = DefaultRouter()

router.register(r'projects' , ProjectViewSet)
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'Communities', CommunityViewSet)
router.register(r'posts',PostViewSet)
