from restframework.models import *
from rest_framework import serializers

class BuySerializer(serializers.Serializer):
    test = serializers.CharField(help_text='test 쿼리파라미터', default='no')

    addr = serializers.SerializerMethodField()
    mem_name = serializers.SerializerMethodField()

    def get_addr(self, obj):
        print(obj.mem.addr)
        return obj.mem.addr

    def get_mem_name(self, obj):
        print(obj.mem.mem_name)
        return obj.mem.mem_name

    class Meta:
        model = Buy
        fields = ['mem', 'mem_name', 'addr', 'prod_name', 'group_name', 'price']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['mem_id', 'mem_number']