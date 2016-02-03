from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queryserver.models import Session, Query, Object, Box
from queryserver.serializers import SessionSerializer, QuerySerializer, ObjectSerializer, BoxSerializer


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

@api_view(['POST'])
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

@api_view(['POST'])
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

@api_view(['POST'])
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
def query_with_sessionid(request, sessionid):
    """
    Retrieve queries with seesion id.
    """
    try:
        query = Query.objects.filter(sessionid=sessionid)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuerySerializer(query, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def update_boxinfo_with_boxid(request, boxid):
    """
    Update boxinfo in a box with box id
    """
    try:
        box = Box.objects.get(id=boxid)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    box.boxinfo = request.data.get("boxinfo")
    box.save()
    serializer = BoxSerializer(box)
    return Response(serializer.data)

