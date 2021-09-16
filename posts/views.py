from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    """
    모든 포스트목록을 불러옵니다.
    """
    if request.method == 'GET':
        posts = Post.objects.all().order_by("-scraped_date")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    """
    Retrieve, update or delete.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def post_list_keyword_query(request, keyword):
    if "맛집" not in keyword:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    posts = Post.objects.filter(keyword=keyword).values().order_by("-scraped_date")
    if posts.count() == 0:
        data = {
            "post_id": "dummy",
            "post_url": "dummy",
            "img_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c",
            "keyword": keyword
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_keyword_score_query(request, keyword, food_score):
    if "맛집" not in keyword:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    posts = Post.objects.filter(keyword=keyword, food_score__gte=float(food_score)).values().order_by("-scraped_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def keyword_list(request):
    keywords = Post.objects.filter().values("keyword").distinct()
    return Response(keywords)


@api_view(['GET'])
def post_postid_keyword_query(request, keyword, post_id):
    try:
        post = Post.objects.get(post_id=post_id, keyword=keyword)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(post)
    return Response(serializer.data)
