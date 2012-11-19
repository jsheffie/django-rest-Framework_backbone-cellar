from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wine_cellar.wines.models import Wine
from wine_cellar.wines.serializers import WineSerializer

@api_view( ['GET', 'POST'] )
def wine_list( request, format='json' ):
    """ list all of wines, or create a new wine """
    if request.method == 'GET':
        wines = Wine.objects.all()
        serializer = WineSerializer( wines )
        return Response( serializer.data )

    elif request.method == 'POST':
        serializer = WineSerializer( data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response ( serializer.data, status=status.HTTP_201_CREATED )
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

