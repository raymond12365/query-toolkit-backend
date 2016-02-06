from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queryserver.models import Session, Soc, Video, Query, Object, Box
from queryserver.serializers import SessionSerializer, SocSerializer, VideoSerializer, QuerySerializer, ObjectSerializer, BoxSerializer


@api_view(['GET', 'POST'])
def session_list(request):
    """
    List all sessions, or create a new session.
    """
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def soc_list(request):
    """
    List all socs, or create a new soc.
    """
    if request.method == 'GET':
        socs = Soc.objects.all()
        serializer = SocSerializer(socs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def video_list(request):
    """
    List all videos, or create a new video.
    """
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def query_list(request):
    """
    List all queries, or create a new query.
    """
    if request.method == 'GET':
        queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def object_list(request):
    """
    List all objects, or create a new object.
    """
    if request.method == 'GET':
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def box_list(request):
    """
    List all boxs, or create a new box.
    """
    if request.method == 'GET':
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def session_detail(request, pk):
    """
    Retrieve or delete a session instance with sessionid.
    """
    try:
        session = Session.objects.get(id=pk)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def query_detail(request, pk):
    """
    Retrieve or delete a query instance with queryid.
    """
    try:
        query = Query.objects.get(id=pk)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuerySerializer(query)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def soc_detail(request, pk):
    """
    Retrieve or delete a soc instance with socid.
    """
    try:
        soc = Soc.objects.get(id=pk)
    except Soc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocSerializer(soc)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        soc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def video_detail(request, pk):
    """
    Retrieve or delete a video instance with videoid.
    """
    try:
        video = Video.objects.get(id=pk)
    except Video.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def object_detail(request, pk):
    """
    Retrieve or delete an object instance with objectid.
    """
    try:
        object = Object.objects.get(id=pk)
    except Object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ObjectSerializer(object)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def box_detail(request, pk):
    """
    Retrieve or delete an object instance with boxid.
    """
    try:
        box = Box.objects.get(id=pk)
    except Object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoxSerializer(box)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        box.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_predicates_with_queryid(request, queryid):
    """
    Update predicates in a query with query id
    """
    try:
	query = Query.objects.get(id=queryid)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    query.predicates = request.data.get("predicates")
    query.save()
    serializer = QuerySerializer(query)
    return Response(serializer.data)

@api_view(['PUT'])
def update_answer_with_queryid(request, queryid):
    """
    Update the answer of a query with query id
    """
    try:
        query = Query.objects.get(id=queryid)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    query.answer = request.data.get("answer")
    query.save()
    serializer = QuerySerializer(query)
    return Response(serializer.data)

@api_view(['PUT'])
def update_comment_with_queryid(request, queryid):
    """
    Update comment in a query with query id
    """
    try:
        query = Query.objects.get(id=queryid)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    query.comment = request.data.get("comment")
    query.save()
    serializer = QuerySerializer(query)
    return Response(serializer.data)

@api_view(['GET'])
def queries_with_sessionid(request, sessionid):
    """
    Retrieve queries with seesion id.
    """
    try:
        queries = Query.objects.filter(sessionid=sessionid)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def videos_with_socid(request, socid):
    """
    Retrieve videos with soc id.
    """
    try:
        videos = Video.objects.filter(socid=socid)
    except Video.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def objects_with_sessionid(request, sessionid):
    """
    Retrieve objects with seesion id.
    """
    try:
        objects = Object.objects.filter(sessionid=sessionid)
    except Object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def boxes_with_sessionid(request, sessionid):
    """
    Retrieve boxes with seesion id.
    """
    try:
        boxes = Box.objects.filter(objectid__sessionid__exact=sessionid)
    except Box.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)
