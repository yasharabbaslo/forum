
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views
from boards.views import BoardListView, TopicListView, PostListView, new_topic, topic_reply, PostUpdateView
from accounts.views import signup, UserUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BoardListView.as_view(), name='index'),

    path('boards/<int:pk>/', TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', topic_reply, name='topic_reply'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', PostUpdateView.as_view(), 
    name='edit_post'),

    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('reset/', views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt'
    ), name='password_reset'),

    path('reset/done/', views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), 
    name='password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
    views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), 
    name='password_reset_confirm'),

    path('reset/complete/', views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
    name='password_reset_complete'),

    path('settings/password/', views.PasswordChangeView.as_view(template_name='accounts/change_password.html'), 
    name='change_password'),

    path('settings/password/done/', views.PasswordChangeDoneView.as_view(template_name='accounts/change_password_done.html'), 
    name='change_password_done'),

    path('settings/account/', UserUpdateView.as_view(), name='my_account'),
]
