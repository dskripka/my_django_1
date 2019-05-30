from django.urls import path
from hw18.views import write_line, display_lines, clear_file

urlpatterns = [
    path('write_line/', write_line),
    path('display_lines/', display_lines),
    path('clear_file/', clear_file),
]
