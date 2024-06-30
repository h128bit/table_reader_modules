from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .handlers.files_handler import to_excel_tabel
from .connectors.Direct_connection import *
from .connectors.connector import Connector


connector: Connector = DirectConnector()


class DrawCellsContoursView(APIView):

    def post(self, request):
        file = request.data.getlist('data')
        extension = str(file[0]).split('.')[-1]
        response = connector.get_table_struct(file[0].read(), extension)
        return Response({'image': response})


class RecognizeView(APIView):
    def post(self, request):
        files = request.data.getlist('data')
        files = list(map(lambda x: x.read(), files))
        response = connector.recognize(files)
        table = {'table': response}
        return Response(table)


class DownloadExcelView(APIView):
    def post(self, request):
        tables = request.data['data']
        excel = to_excel_tabel(tables)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=table.xlsx'
        response.write(excel.getvalue())
        return response
