from rest_framework import serializers
from queryserver.models import Session, Query, Object, Box

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
	model = Session
	fields = ('id', 'socid')

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('id', 'sessionid', 'answer', 'comment', 'predicates')

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('id', 'sessionid', 'label')

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('id', 'objectid', 'boxinfo')
