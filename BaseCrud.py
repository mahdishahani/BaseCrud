class ListCreateMixin(generics.ListCreateAPIView):
    # This mixin provides the functionality for listing and creating objects.

    filter_backends = [filters.SearchFilter]

    def get(self, request, *args, **kwargs):
        # Handles GET requests for listing objects.

        pk = request.query_params.get("pk")
        if pk is not None:
            return self.get_one(request, pk)
        return self.list(request, *args, **kwargs)

    def get_one(self, request, pk):
        # Retrieves a single object by its primary key.

        query_set = self.queryset.filter(pk=pk, deleted_date=None)
        if not query_set.exists():
            return JsonResponse({'message': _("This object doesn't exist")}, status=status.HTTP_404_NOT_FOUND)
        data = self.serializer_class(query_set.first()).data
        return Response(data, status=status.HTTP_200_OK)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        # Handles POST requests for creating objects.

        return super().post(request, *args, **kwargs)


class RetrieveUpdateDestroyMixin(generics.RetrieveUpdateDestroyAPIView):
    # This mixin provides the functionality for retrieving, updating, and deleting objects.

    def put(self, request, *args, **kwargs):
        # Handles PUT requests for updating objects.

        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Handles DELETE requests for deleting objects.

        try:
            obj = self.get_object()
        except self.model.DoesNotExist:
            return Response({'message': _("This object doesn't exist")}, status=status.HTTP_404_NOT_FOUND)

        obj.deleted_date = datetime.datetime.now()
        obj.save()
        content = {'message': _('Successfully deleted')}
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class BaseCrud(ListCreateMixin, RetrieveUpdateDestroyMixin):
    # This class combines the ListCreateMixin and RetrieveUpdateDestroyMixin to provide a complete CRUD functionality.

    queryset = None
    serializer_class = None
    model = None
    lookup_field = 'pk'

    def get_queryset(self):
        # Filters the queryset to exclude deleted objects.

        queryset = self.queryset.filter(deleted_date=None)
        return queryset

    def get_serializer_class(self):
        # Returns the serializer class to be used.

        return self.serializer_class

    def get_object(self):
        # Retrieves a single object based on the lookup field and excludes deleted objects.

        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.request.query_params[self.lookup_field], 'deleted_date': None}
        obj = generics.get_object_or_404(queryset, **filter_kwargs)
        return obj

