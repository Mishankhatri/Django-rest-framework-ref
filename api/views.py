import io
from urllib import request
from api.customauthentication import MyCustomAuthentication
from api.custompaginator import MyCustomPaginator
from api.custompermissions import MyCustomPermission
from api.models import Song, Student,Singer
from api.serializers import SongSerializer, StudentSerializer,SingerSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from api.throttling import AdminThrottleRate
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

# basic jsonresponse apis
# def student_detail(request,pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data,content_type='application/json')
#     return JsonResponse(serializer.data)

# def studentAll(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu,many=True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data,content_type='application/json')
#     return JsonResponse(serializer.data,safe=False)

# @csrf_exempt
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pydata)
#         if serializer.is_valid():
#             serializer.save()
#             res= {'msg':'data created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')

#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pydata)
#         if serializer.is_valid():
#             serializer.save()
#             res= {'msg':'data created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu,data = pydata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res= {'msg':'data updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res= {'msg':f'data deleted for {id}'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')



# @method_decorator(csrf_exempt,name='dispatch')
# class StudentApi(View):
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type= 'application/json')

#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pydata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'data sucessfull created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type= 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type= 'application/json')

#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu,data=pydata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':f'Data edited for id no. {id}'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.error)
#         return HttpResponse(json_data,content_type='application/json')

#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res= {'msg':f'data deleted of id. {id}'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')



# # DRF apiview decorators and APIView class
# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg':'This is get request'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This is post request','data':request.data})


# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def fxnapi(request,pk=None):
#     if request.method == 'GET':
#         id = pk
#         # id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data is created'}
#             return Response(res,status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':f'Data edited for id no. {id} complete(PUT)'}
#             return Response(res)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PATCH':
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':f'Data edited for id no. {id} partial(PATCH)'}
#             return Response(res)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res= {'msg':f'data deleted of id. {id}'}
#         return Response(res)



# class ClassApi(APIView):
#     def get(self, request, format= None,*args, **kwargs):
#         id = kwargs.get('pk')
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)

#     def post(self,request,format= None):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'},status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     def put(self,request,format=None):
#         id = request.data.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':f'Data edited for id no. {id} complete(PUT)'}
#             return Response(res)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     def patch(self,request,format=None,*args, **kwargs):
#         id = kwargs.get('pk')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':f'Data edited for id no. {id} partial(PATCH)'}
#             return Response(res)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,format= None,*args, **kwargs):
#         id = kwargs.get('pk')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res= {'msg':f'data deleted of id. {id}'}
#         return Response(res)

# #DRF GenereicAPIView and mixins
# class LCmixins(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)

# class RUDmixins(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)

#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)

#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)


# #DRF ConcreteViews
# class StudentListCreateAPIView(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# #normal viewset
# class StudentViewSet(viewsets.ViewSet):
#     def list(self,request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
    
#     def create(self,request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'},status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
#     def update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':f'Data edited for id no. {id} complete(PUT)'}
#             return Response(res)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     def partial_update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':f'Data edited for id no. {id} complete(Patch)'}
#             return Response(res)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     def destroy(self,request,pk):
#         id=pk
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res= {'msg':f'data deleted of id. {id}'}
#         return Response(res)
        

#ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    # queryset = Student.objects.all()
    # queryset = Student.objects.filter(city='Butwal')
    serializer_class = StudentSerializer
    # permission_classes = [MyCustomPermission]
    permission_classes= [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    # throttle_classes = [AnonRateThrottle,AdminThrottleRate]
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [MyCustomAuthentication]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['id','name','city']
    
    search_fields=['name','city']
    # search_fields=['^name','=city']
    
    ordering_fields = ['name', 'city']
    ordering=['name'] #default ordering
    
    pagination_class =  MyCustomPaginator
    
    def get_queryset(self):
        user = self.request.user
        # return Student.objects.filter(user=user)
        return Student.objects.all()
        
    
    

#ReadOnlyModelViewSet
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

# # for generating tokens for all existing users
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

class SongModelViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    
class SingerModelViewSet(viewsets.ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()

    



