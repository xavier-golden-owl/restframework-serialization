from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework import generics

class SnippetListView(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer		


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer