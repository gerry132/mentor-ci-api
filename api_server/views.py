from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .utils import get_json_data


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    renderer_classes = [JSONRenderer]
    if request.method == 'GET':
        data = get_json_data()
        return Response(data)

    elif request.method == 'POST':
        if (request.GET.get('name')):
            welcome = "Good morning {}! Welcome to APIs!".format(request.GET.get('name'))
            return Response(welcome)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)