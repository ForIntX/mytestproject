from polls import views
from django.urls import path


urlpatterns = [
    path('', views.index,name="index"),
    path('search/', views.search,name="search"),
    path('create-course/', views.create_course,name="create_course"),
    path('create-course-new-method/',views.create_course_2,name="create_course_2"),
    path('create-category/',views.create_category,name="create_category"),
    path('course-list/',views.course_list,name="course_list"),
    path("course-edit/<int:id>/", views.course_edit, name="course_edit"),
    path("course-delete/<int:id>/", views.course_delete, name="course_delete"),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('details/<slug:slug_name>/', views.details, name="details"),
    path('category/<slug:slug>/',views.getPollsByCategory,name='pollsTypeName'),
]   