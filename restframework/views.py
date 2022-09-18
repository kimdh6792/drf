from restframework.models import *
from restframework.serializers import BuySerializer, MemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils       import swagger_auto_schema
from drf_yasg             import openapi

class BuyListAPI(APIView):
    # query_serializer는 해당 serializer에서 설정한 내용을 swagger에서 인풋값으로 받을 수 있게 해줌.
    @swagger_auto_schema(tags=['데이터를 검색합니다.'], query_serializer=BuySerializer, responses={200: 'Success'})
    def get(self, request):
        params = request.GET

        test = params.get('test')
        print(test)
        qs = Buy.objects.filter(mem__in=Member.objects.filter(mem_number=6).values('mem_id'))
        serializer = BuySerializer(qs, many=True)
        return Response(serializer.data)

