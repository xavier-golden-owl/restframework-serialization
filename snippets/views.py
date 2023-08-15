from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

from rest_framework import generics
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SnippetListView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer		

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer