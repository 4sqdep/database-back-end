# from django.utils.deprecation import MiddlewareMixin
# from db_main.models import APIRequestCount, APIRequestCountLog
#
#
# class APICountMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         if request.path.startswith('/api/login/'):
#             # IP manzilini olish
#             ip_address = request.META.get('REMOTE_ADDR')
#             # Foydalanuvchini olish
#             user = None
#             if request.user.is_authenticated:
#                 user = request.user
#             endpoint = request.path
#             api_request, created = APIRequestCount.objects.get_or_create(endpoint=endpoint,
#                                                                          user=user, ip_address=ip_address)
#             api_request.count = int(api_request.count)
#             api_request.count += 1
#             api_request.save()
#             APIRequestCountLog.objects.create(api_request=api_request)
#         elif request.path.startswith('/api/main/categories-create/'):
#             # IP manzilini olish
#             ip_address = request.META.get('REMOTE_ADDR')
#         # Foydalanuvchini olish
#             user = None
#             if request.user.is_authenticated:
#                 user = request.user
#             endpoint = request.path
#             api_request, created = APIRequestCount.objects.get_or_create(endpoint=endpoint, user=user,
#                                                                          ip_address=ip_address)
#             api_request.count = int(api_request.count)
#             api_request.count += 1
#             api_request.save()
#             APIRequestCountLog.objects.create(api_request=api_request)
#         elif request.path.startswith('/api/main/category-all/'):
#             # IP manzilini olish
#             ip_address = request.META.get('REMOTE_ADDR')
#             # Foydalanuvchini olish
#             user = None
#             if request.user.is_authenticated:
#                 user = request.user
#             endpoint = request.path
#             api_request, created = APIRequestCount.objects.get_or_create(endpoint=endpoint, user=user,
#                                                                          ip_address=ip_address)
#             api_request.count = int(api_request.count)
#             api_request.count += 1
#             api_request.save()
#             APIRequestCountLog.objects.create(api_request=api_request)
#         elif request.path.startswith('/api/main/user-category/'):
#             # IP manzilini olish
#             ip_address = request.META.get('REMOTE_ADDR')
#             # Foydalanuvchini olish
#             user = None
#             if request.user.is_authenticated:
#                 user = request.user
#             endpoint = request.path
#             api_request, created = APIRequestCount.objects.get_or_create(endpoint=endpoint, user=user,
#                                                                          ip_address=ip_address)
#             api_request.count = int(api_request.count)
#             api_request.count += 1
#             api_request.save()
#             APIRequestCountLog.objects.create(api_request=api_request)
#         elif request.path.startswith('/api/main/post-project/'):
#             # IP manzilini olish
#             ip_address = request.META.get('REMOTE_ADDR')
#             # Foydalanuvchini olish
#             user = None
#             if request.user.is_authenticated:
#                 user = request.user
#             endpoint = request.path
#             api_request, created = APIRequestCount.objects.get_or_create(endpoint=endpoint, user=user,
#                                                                          ip_address=ip_address)
#             api_request.count = int(api_request.count)
#             api_request.count += 1
#             api_request.save()
#             APIRequestCountLog.objects.create(api_request=api_request)
#         return None