from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination,CursorPagination

# class MyCustomPaginator(PageNumberPagination):
#     page_size=3
#     page_query_param = 'p'
#     page_size_query_param='page_size'
#     max_page_size = 12
    
# class MyCustomPaginator(LimitOffsetPagination):
#     default_limit =5
#     max_limit=12
    
class MyCustomPaginator(CursorPagination):
    page_size=12
    
    