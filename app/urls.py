from django.urls import path
from . import views
from TMC2 import settings
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tmc'

urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('problemset/',views.problem_set,name="problem_set"),
    path('problemset/problem/<int:pk>/',views.problem,name="problem"),
    path('profile/',views.profile,name="profile"),
    path('profile/<str:username>/',views.other_profile,name="other_profile"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('topic_problems/<str:topic>/<int:num>/',views.topic_probelm_set,name="topic_problems"),
    path('problemset/problem/add_problem', views.add_problem, name="add_problem"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('user_registration/', views.user_registration, name="user_registration"),
    path('forgot_password/<str:email>/<str:otp>/',views.forgot_password, name="forgot_password"),
    path('admin_panel/', views.admin_panel_users, name='admin_panel_users'),
    path('admin_panel/problems/', views.admin_panel_problems,name="admin_panel_problems"),
    path('admin_panel/club_members/', views.admin_panel_club_members, name="admin_panel_club_members"),
    path('admin/problems/delete_problems/<int:pk>/', views.delete_problem, name="delete_problems"),
    path('admin/problems/edit_problems/<int:pk>/', views.edit_problem, name="edit_problem"),
    path('login_as_admin/',views.admin_login, name="admin_login"),
    path('admin_panel/club_members/<int:pk>/', views.admin_panel_club_member_details, name="admin_panel_club_member_details"),
    path('admin_panel/submissions/', views.admin_panel_submissions, name="admin_panel_submissions"),
    path('admin/user/<int:pk>/delete/', views.delete_user, name="delete_user"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



