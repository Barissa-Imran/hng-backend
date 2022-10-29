from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.serializers import ProfileSerializer
from server.models import Profile

@api_view(['GET'])
def profile_detail(request):
    """
    Get profile from the database
    """
    if request.method == 'GET':
        pk = 1
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
