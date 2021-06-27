from rest_framework.pagination import PageNumberPagination


class StandardResultSetPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 100
