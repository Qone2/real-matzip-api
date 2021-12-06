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
    GET
    모든 포스트목록을 불러옵니다.

    POST
    포스트를 저장할 때 사용합니다. json형식을 담아 요청합니다.
    또한 스크랩 했을때 스크랩 결과물이 0개 일때도 사용합니다.
    이때는 not-scraped-yet 목록에 나오지 않게 하는 목적입니다.
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
    id에 해당하는 포스트를 반환하거나, 수정하거나, 삭제합니다.
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
    """
    키워드로 스크랩 된 모든 포스트들을 반환합니다.
    scraped_date 최신순으로 보여집니다.
    """
    posts = Post.objects.filter(keyword=keyword).values().order_by("-scraped_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_keyword_query_posted_date_order(request, keyword):
    """
    키워드로 스크랩 된 모든 포스트들을 반환합니다.
    posted_date 최신순으로 보여집니다.
    """
    posts = Post.objects.filter(keyword=keyword).values().order_by("-posted_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_keyword_score_query(request, keyword, food_score):
    """
    키워드로 스크랩 된 모든 포스트들 중에서 음식점수가 원하는 값보다 높은 포스트들만 보여집니다.
    scraped_date 최신순으로 보여집니다.
    """
    posts = Post.objects.filter(keyword=keyword, food_score__gte=float(food_score), is_ad=False).values().order_by("-scraped_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_keyword_score_query_posted_date_order(request, keyword, food_score):
    """
    키워드로 스크랩 된 모든 포스트들 중에서 음식점수가 원하는 값보다 높은 포스트들만 보여집니다.
    posted_date 최신순으로 보여집니다.
    """
    posts = Post.objects.filter(keyword=keyword, food_score__gte=float(food_score), is_ad=False).values().order_by("-posted_date")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


class PostListKeywordScoreQuery(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """
        키워드로 스크랩 된 모든 포스트들 중에서 음식점수가 원하는 값보다 높은 포스트들만 보여집니다.
        페이징이 적용되어 보여집니다.
        scraped_date 최신순으로 보여집니다.
        """
        keyword = self.kwargs.get("keyword", None)
        food_score = self.kwargs.get("food_score", None)
        queryset = Post.objects.filter(keyword=keyword, food_score__gte=float(food_score), is_ad=False).values().order_by(
            "-scraped_date")
        return queryset


@api_view(['GET'])
def keyword_list(request):
    """
    한번이상 스크랩된 키워드 목록을 보여줍니다.
    포스트 개수가 2개 이상인 키워드 목록을 보여줍니다.
    각각의 키워드에 대하여, 등록된 날짜가 가장 오래된(처음등록된) 포스트의 날짜가 최신순으로 정렬되어 보여집니다.
    """
    keywords = Post.objects.values("keyword").annotate(post_count=Count("post_id"), first_date=Min("scraped_date")).filter(post_count__gt=1).order_by("first_date")
    response = {"keyword_list": []}
    for keyword in keywords:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


@api_view(['GET', 'DELETE'])
def post_postid_keyword_query(request, keyword, post_id):
    """
    키워드와 post_id에 해당하는 포스트를 반환하거나, 삭제합니다.
    """
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
    """
    아직 스크랩되지 않은 키워드 목록을 보여줍니다.
    정확히는 키워드별로 포스트개수가 1개인 키워드 목록을 반환합니다.
    해당 서버는 키워드별로 포스트 개수가 1개 이상인 키워드를 스크랩 대사으로 간주합니다.
    또한 키워드별로 포스트 개수가 1개인 키워드는 아직 스크랩되지 않은 키워드로 판단합니다.
    각각의 키워드에 대하여, 등록된 날짜가 가장 오래된(처음등록된) 포스트의 날짜가 최신순으로 정렬되어 보여집니다.
    """
    response = {"keyword_list": []}
    keyword_list = Post.objects.values("keyword").annotate(post_count=Count("post_id"), first_date=Min("scraped_date")).filter(post_count__lte=1).order_by("first_date")
    for keyword in keyword_list:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


@api_view(['POST'])
def insert_keyword(request, keyword):
    """
    키워드로 스크랩 된 포스트가 하나도 없을 때 사용합니다. 미리 지정된 형식의 더미포스트가 저장됩니다.
    저희 서버에서는 특정키워드에 포스트가 하나밖에 없으면 스크랩대상이지만 아직 스크랩되지 않은 걸로 간주합니다.
    따라서 해당 주소로 요청을 보내면 곧 해당 키워드로 스크랩하게 됩니다.
    """
    if "맛집" not in keyword:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = {
        "post_id": "dummy",
        "post_url": "dummy",
        "img_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c?w=640",
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
    """
    포스트개수와 상관없이 모든 키워드목록을 반환합니다.
    스크랩할 계정을 인덱싱할 때 사용합니다.
    각각의 키워드에 대하여, 등록된 날짜가 가장 오래된(처음등록된) 포스트의 날짜가 최신순으로 정렬되어 보여집니다.
    """
    keywords = Post.objects.values("keyword").annotate(first_date=Min("scraped_date")).order_by("first_date")
    response = {"keyword_list": []}
    for keyword in keywords:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


@api_view(['GET'])
def all_keyword_list_alphabetical_order(request):
    """
    모든 키워드를 알파벳순서로 보여줍니다.
    """
    keywords = Post.objects.values("keyword").distinct()
    response = {"keyword_list": []}
    for keyword in keywords:
        response["keyword_list"].append(keyword["keyword"])
    return Response(response)


class AllPostList(generics.ListAPIView):
    """
    모든 포스트목록을 불러옵니다.
    페이징이 적용되어 반환됩니다.
    """
    queryset = Post.objects.all().order_by("-scraped_date")
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
