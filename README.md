This code provides a reusable CRUD (Create, Retrieve, Update, Delete) functionality for your API views. It includes mixins for handling list, create, retrieve, update, and delete operations. The BaseCrud class combines these mixins to provide a complete CRUD functionality. It also includes methods for handling GET, POST, PUT, and DELETE requests, as well as filtering out deleted objects and returning appropriate responses


# Django CRUD API Mixins

This repository contains Django API mixins that provide a convenient way to implement CRUD (Create, Retrieve, Update, Delete) functionality for your API views. The mixins are designed to be reusable and can be easily integrated into your Django projects.

## Mixin Classes

### ListCreateMixin

This mixin provides functionality for listing and creating objects.

- `GET /` - Retrieve a list of objects.
- `GET /?pk={id}` - Retrieve a single object by its primary key.
- `POST /` - Create a new object.

### RetrieveUpdateDestroyMixin

This mixin provides functionality for retrieving, updating, and deleting objects.

- `GET /{id}` - Retrieve a single object by its primary key.
- `PUT /{id}` - Update an existing object.
- `DELETE /{id}` - Delete an object.

### BaseCrud

This class combines the ListCreateMixin and RetrieveUpdateDestroyMixin to provide a complete CRUD functionality.

- It filters out deleted objects automatically.
- It uses the provided serializer class for serialization and deserialization of objects.
- It can be easily customized to fit your specific requirements.

## Usage

1. Copy the desired mixin classes (`ListCreateMixin`, `RetrieveUpdateDestroyMixin`, `BaseCrud`) into your Django project.
2. Customize the mixin classes if needed, such as specifying the `queryset` and `serializer_class` attributes.
3. In your views, inherit from the appropriate mixin class (`ListCreateMixin`, `RetrieveUpdateDestroyMixin`, or `BaseCrud`) and set the necessary attributes.
4. Implement your API endpoints by defining the appropriate HTTP methods (e.g., `get`, `post`, `put`, `delete`) in your views.
5. Customize the behavior and responses of the mixin methods as per your requirements.

## Dependencies

The code provided in this repository relies on the following dependencies:

- Django
- Django REST framework

Make sure you have these dependencies installed in your Django project before using the mixins.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this code in your Django projects.

