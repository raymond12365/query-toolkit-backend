from rest_framework import serializers
from queryserver.models import Session, Soc, Video, Query, Object, Box

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
	model = Session
	fields = ('id', 'socid')

class SocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soc
        fields = ('id', 'url')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'socid', 'name', 'url')

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
        fields = ('id', 'objectid', 'videoid','time', 'x','y','xlen','ylen')
