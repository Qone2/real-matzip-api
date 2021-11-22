from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from django.db.models import Count, Min, Max, Avg
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


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
    posts = Post.objects.filter(keyword=keyword).values().order_by("-scraped_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_keyword_query_posted_date_order(request, keyword):
    posts = Post.objects.filter(keyword=keyword).values().order_by("-posted_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_keyword_score_query(request, keyword, food_score):
    posts = Post.objects.filter(keyword=keyword, food_score__gte=float(food_score), is_ad=False).values().order_by("-scraped_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_keyword_score_query_posted_date_order(request, keyword, food_score):
    posts = Post.objects.filter(keyword=keyword, food_score__gte=float(food_score), is_ad=False).values().order_by("-posted_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


class PostListKeywordScoreQuery(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        keyword = self.kwargs.get("keyword", None)
        food_score = self.kwargs.get("food_score", None)
        queryset = Post.objects.filter(keyword=keyword, food_score__gte=float(food_score), is_ad=False).values().order_by(
            "-scraped_date")
        return queryset


@api_view(['GET'])
def keyword_list(request):
    keywords = Post.objects.values("keyword").annotate(post_count=Count("post_id"), first_date=Min("scraped_date")).filter(post_count__gt=1).order_by("first_date")
    response = {"keyword_list": []}
    for keyword in keywords:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


@api_view(['GET', 'DELETE'])
def post_postid_keyword_query(request, keyword, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(post_id=post_id, keyword=keyword)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        try:
            post = Post.objects.get(post_id=post_id, keyword=keyword)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def not_scraped_yet(request):
    response = {"keyword_list": []}
    keyword_list = Post.objects.values("keyword").annotate(post_count=Count("post_id"), first_date=Min("scraped_date")).filter(post_count__lte=1).order_by("first_date")
    for keyword in keyword_list:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


@api_view(['POST'])
def insert_keyword(request, keyword):
    if "맛집" not in keyword:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = {
        "post_id": "dummy",
        "post_url": "dummy",
        "img_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c",
        "keyword": keyword,
        "post_text": "dummy",
        "insta_analysis": "dummy",
        "insta_analysis_food": False,
        "is_ad": False
    }
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def all_keyword_list(request):
    keywords = Post.objects.values("keyword").annotate(first_date=Min("scraped_date")).order_by("first_date")
    response = {"keyword_list": []}
    for keyword in keywords:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


@api_view(['GET'])
def all_keyword_list_alphabetical_order(request):
    keywords = Post.objects.values("keyword").distinct()
    response = {"keyword_list": []}
    for keyword in keywords:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


class AllPostList(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-scraped_date")
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
