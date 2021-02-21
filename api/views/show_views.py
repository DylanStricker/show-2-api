from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.show import Show
from ..serializers import ShowSerializer, UserSerializer

# Create your views here.
class Shows(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ShowSerializer
    def get(self, request):
        """Index request"""
        # Get all the shows:
        shows = Show.objects.all()
        # Filter the shows by owner, so you can only see your owned shows
        # shows = Show.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ShowSerializer(shows, many=True).data
        print(data)
        return Response({ 'shows': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['owner'] = request.user.id
        # Serialize/create show
        show = ShowSerializer(data=request.data)
        # If the show data is valid according to our serializer...
        if show.is_valid():
            # Save the created show & send a response
            show.save()
            return Response(show.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(show.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the show to show
        show = get_object_or_404(Show, pk=pk)
        # Only want to show owned shows?
        # if not request.user.id == show.owner.id:
        #     raise PermissionDenied('Unauthorized, you do not own this show')

        # Run the data through the serializer so it's formatted
        data = ShowSerializer(show).data
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        # Locate show to delete
        show = get_object_or_404(Show, pk=pk)
        # Check the show's owner agains the user making this request
        if not request.user.id == show.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this show')
        # Only delete if the user owns the  show
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['show'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data.get('owner', False):
            del request.data['owner']

        # Locate Show
        # get_object_or_404 returns a object representation of our Show
        show = get_object_or_404(Show, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == show.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this show')

        # Add owner to data object now that we know this user owns the resource
        request.data['owner'] = request.user.id
        # Validate updates with serializer
        data = ShowSerializer(show, data=request.data)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
