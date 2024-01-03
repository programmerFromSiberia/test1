from django.urls import path, re_path
import films.views as film  #from films.views import index, movie, categories

urlpatterns = [
    path('', film.index),  # http://127.0.0.1:8000
    path('search_movie/page<int:page_number>/', film.search_movies),# http://127.0.0.1:8000/search_movie/page0
    path('suggestion/', film.suggest_genre),  # http://127.0.0.1:8000/info_movie/id_movie/



    path('info_movie/<slug:id_movie>/', film.movie_pages), # http://127.0.0.1:8000/info_movie/id_movie/
    path('cats/', film.categories, name="media"), # http://127.0.0.1:8000/cats/

    # http://127.0.0.1:8000/test/
    path('test/', film.f), #для учебы

    # http://127.0.0.1:8000/archive/2000 - валидный
    re_path(r"^archive/(?P<year>(1|2)\d{3})/$", film.archive),
    #  1000 - 2999 - валидный
    # http://127.0.0.1:8000/archive/434324234 - невалидный

]