from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100
    limit_query_param = "limit"
