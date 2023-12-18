from rest_framework import routers

from .views import BookListView, AuthorListView

router = routers.DefaultRouter()
router.register("books", BookListView, "books")
router.register("authors", AuthorListView, "authors")

urlpatterns = router.urls
