from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    renderer_classes = [JSONRenderer]
    if request.method == 'GET':
        return Response("hello")

    elif request.method == 'POST':
        return Response("hello", status=status.HTTP_400_BAD_REQUEST)