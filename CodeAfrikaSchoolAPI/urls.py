from rest_framework.routers import DefaultRouter
from .Communities.views import  CommunityViewSet
from .Projects.views import ProjectViewSet
from .Users.views import UserViewSet
from .Posts.views import PostViewSet
from .Courses.views import CourseViewSet
#from .SchoolModules.views import SchoolModuleViewSet
from .Lessons.views import LessonViewSet
from .Topics.views import TopicViewSet



router = DefaultRouter()

router.register(r'projects' , ProjectViewSet)
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'Communities', CommunityViewSet)
router.register(r'posts',PostViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'lessons',LessonViewSet)
#router.register(r'module', SchoolModule)
