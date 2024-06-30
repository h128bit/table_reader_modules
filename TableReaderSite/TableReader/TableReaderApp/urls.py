from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('drawcells', DrawCellsContoursView.as_view()),
    path('recognize', RecognizeView.as_view()),
    path('downloadexcel', DownloadExcelView.as_view()),
]
