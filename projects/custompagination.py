from rest_framework.pagination import LimitOffsetPagination


class LimitedOffsetPaginationProjects(LimitOffsetPagination):
    max_limit = 9
