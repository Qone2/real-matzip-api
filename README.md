# Real Matzip API
진짜맛집 프로젝트의 메인 api서버

## 1. Install
### pip
```shell
pip install -r requirements.txt
```
### Migration
```shell
python manage.py makemigrations

python manage.py migrate
```

### Run
```shell
python manage.py runserver 0.0.0.0:8443

python waitress-server.py
```
## 2. Usage
### (1) 클라이언트 사이드 통신용
#### GET baseurl/posts/<키워드>
키워드로 스크랩 된 모든 포스트들을 반환합니다. <br>
posted_date 최신순으로 보여집니다. <br>
ex) GET http://localhost:8443/posts/명동맛집
```json
[
    {
        "id": 28904,
        "post_id": "CW----UvPGp",
        "post_url": "https://www.instagram.com/p/CW----UvPGp/",
        "img_url": "https://www.instagram.com/p/CW----UvPGp/media/?size=l",
        "keyword": "명동맛집",
        "food_score": 77.08,
        "scraped_date": "2021-11-26T15:31:48.386112+09:00",
        "posted_date": "2021-11-26T15:28:18+09:00",
        "post_text": "--이랑 데이트 ------ ❤🧡💛💚💙💜\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#명짐맛집\r\n#명대사\r\n#명랑골프\r\n#명동맛집\r\n#명동\r\n#명품가방추천\r\n#명언\r\n#명상\r\n#명언스타그램\r\n#명품백\r\n#명절\r\n#명품의류\r\n#명품지갑\r\n#명품운동화\r\n#명품패딩\r\n#명화\r\n#명절선물\r\n#명곡\r\n#명품도매\r\n#명지대\r\n#명품샵\r\n#명품신상\r\n#명동교자\r\n#명품신발\r\n#명화그리기\r\n#명불허전\r\n#명품벨트\r\n#멸치볶음\r\n#멸망\r\n#멸치탈출",
        "insta_analysis": "",
        "insta_analysis_food": false,
        "is_ad": false
    },
    {
        "id": 28900,
        "post_id": "CWu----voE8",
        "post_url": "https://www.instagram.com/p/CWu----voE8/",
        "img_url": "https://www.instagram.com/p/CWu----voE8/media/?size=l",
        "keyword": "명동맛집",
        "food_score": 95.6,
        "scraped_date": "2021-11-26T15:31:42.961757+09:00",
        "posted_date": "2021-11-26T15:26:14+09:00",
        "post_text": "추천 메뉴 삼겹살,곱창 마무리 김치말이국수 크으~\n#초반식당\n.\n.\n#충무로맛집 #을지로맛집 #을지로3가맛집 #을지로데이트 #명동맛집 #명동데이트 #남산맛집 #청계천맛집 #종로맛집 #종로3가맛집 #충무로맛집초반식당",
        "insta_analysis": "",
        "insta_analysis_food": false,
        "is_ad": false
    },
.... 중략 ....
]
```

<br>

#### GET baseurl/posts/<키워드>/<점수>
키워드로 스크랩 된 모든 포스트들 중에서 음식점수가 원하는 값보다 높은 포스트들만 보여집니다. <br>
posted_date 최신순으로 보여집니다. <br>
ex) GET http://127.0.0.1:8443/posts/합정맛집/50
```json
[
    {
        "id": 29260,
        "post_id": "CWur----K9N",
        "post_url": "https://www.instagram.com/p/CWur----K9N/",
        "img_url": "https://www.instagram.com/p/CWur----K9N/media/?size=l",
        "keyword": "합정맛집",
        "food_score": 94.64,
        "scraped_date": "2021-11-26T15:42:41.475726+09:00",
        "posted_date": "2021-11-26T15:39:08+09:00",
        "post_text": "추워지는 요즘 자꾸자꾸 생각나는 보이 밀크티 \n기존에 밀크티누 잊어라 한번 맛 보면 빠져드는 맛 \n커피 맛집 미유당  왕 크로플  하나만 먹어도 배가 든든  달달한 보이밀크티에 고소한 플레인크로플 쌉쌀구수한 아메리카노에는 달달리 블루베리 크로플 한번도 안 먹은 사람은 있어도 한번만 먹은 사람은 없는 미유당 보이카노 보이밀크티 \n이제는 선택에 폭을 넓혀 커피도 함께 할수 있는 \n동서양의 만남 \n#미유당#보이카노#아메리카노#보이밀크티#왕크로플#합정#합정맛집#건강#힐링#보이차와커피를미유당에서",
        "insta_analysis": "",
        "insta_analysis_food": false,
        "is_ad": false
    },
    {
        "id": 29256,
        "post_id": "CWuq----zsu",
        "post_url": "https://www.instagram.com/p/CWuq----zsu/",
        "img_url": "https://www.instagram.com/p/CWuq----zsu/media/?size=l",
        "keyword": "합정맛집",
        "food_score": 96.96,
        "scraped_date": "2021-11-26T15:42:37.484558+09:00",
        "posted_date": "2021-11-26T15:31:41+09:00",
        "post_text": "#미도인\n광주에 이런곳 생겼음면 좋겠다!!\n.\n.\n.\n#홍대라멘#합정맛집#홍대데이트코스#홍대맛집#미도인홍대#홍대맛집미도인#합정데이트#홍대스테이크#라멘맛집#홍대스테이크맛집",
        "insta_analysis": "",
        "insta_analysis_food": false,
        "is_ad": false
    },
...중략...
]
```

<br>

#### POST baseurl/<키워드>
키워드로 스크랩 된 포스트가 하나도 없을 때 사용합니다. 미리 지정된 형식의 더미포스트가 저장됩니다.
저희 서버에서는 특정키워드에 포스트가 하나밖에 없으면 스크랩대상이지만 아직 스크랩되지 않은 걸로 간주합니다.
따라서 해당 주소로 요청을 보내면 곧 해당 키워드로 스크랩하게 됩니다. <br>
ex) POST http://127.0.0.1:8443/post/서귀포맛집 <br>
return status code 201
```json
{
    "id": 31672,
    "post_id": "dummy",
    "post_url": "dummy",
    "img_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c?w=640",
    "keyword": "서귀포맛집",
    "food_score": 0.0,
    "scraped_date": "2021-12-06T18:27:53.097114+09:00",
    "posted_date": "2020-12-06T18:09:35.623587+09:00",
    "post_text": "dummy",
    "insta_analysis": "dummy",
    "insta_analysis_food": false,
    "is_ad": false
}
```

<br><br>

### (2) 서버 사이드 통신용
#### GET baseurl/not-scraped-yet
아직 스크랩되지 않은 키워드 목록을 보여줍니다. <br>
정확히는 키워드별로 포스트개수가 1개인 키워드 목록을 반환합니다. <br>
해당 서버는 키워드별로 포스트 개수가 1개 이상인 키워드를 스크랩 대사으로 간주합니다.
또한 키워드별로 포스트 개수가 1개인 키워드는 아직 스크랩되지 않은 키워드로 판단합니다. <br>
각각의 키워드에 대하여, 등록된 날짜가 가장 오래된(처음등록된) 포스트의 날짜가 최신순으로 정렬되어 보여집니다. <br>
ex) GET http://localhost:8443/not-scraped-yet
```json
{
    "keyword_list": [
        "서귀포맛집"
    ]
}
```

<br>

#### GET baseurl/keywords
한번이상 스크랩된 키워드 목록을 보여줍니다. <br>
포스트 개수가 2개 이상인 키워드 목록을 보여줍니다. <br>
각각의 키워드에 대하여, 등록된 날짜가 가장 오래된(처음등록된) 포스트의 날짜가 최신순으로 정렬되어 보여집니다. <br>
ex) GET http://localhost:8443/keywords
```json
{
    "keyword_list": [
        "성수맛집",
        "홍대맛집",
        "합정맛집",
...중략...
        "송파맛집",
        "천호맛집",
        "산본맛집",
        "목포맛집",
        "군만두맛집",
        "의정부맛집"
    ]
}
```

<br>

#### GET baseurl/all-keywords
포스트개수와 상관없이 모든 키워드목록을 반환합니다.
스크랩할 계정을 인덱싱할 때 사용합니다. <br>
각각의 키워드에 대하여, 등록된 날짜가 가장 오래된(처음등록된) 포스트의 날짜가 최신순으로 정렬되어 보여집니다. <br>
ex) GET http://localhost:8443/all-keywords
```json
{
    "keyword_list": [
        "성수맛집",
        "홍대맛집",
...중략...
        "의정부맛집",
        "서귀포맛집"
    ]
}
```

<br>

#### POST baseurl/posts
포스트를 저장할 때 사용합니다. json형식을 담아 요청합니다. <br>
또한 스크랩 했을때 스크랩 결과물이 0개 일때도 사용합니다.
이때는 not-scraped-yet 목록에 나오지 않게 하는 목적입니다. <br>
ex) POST http://localhost:8443/posts
```json
{
    "post_id": "dummy1",
    "post_url": "dummy1",
    "img_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c",
    "keyword": "명동맛집",
    "post_text": "dummy1",
    "posted_date": "2021-09-23T12:00:50+0000",
    "insta_analysis": "dummy1",
    "insta_analysis_food": false,
    "is_ad": false
}
```

return)
```json
{
    "id": 31673,
    "post_id": "dummy1",
    "post_url": "dummy1",
    "img_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c",
    "keyword": "명동맛집",
    "food_score": 0.0,
    "scraped_date": "2021-12-06T18:55:06.505473+09:00",
    "posted_date": "2021-09-23T21:00:50+09:00",
    "post_text": "dummy1",
    "insta_analysis": "dummy1",
    "insta_analysis_food": false,
    "is_ad": false
}
```

<br><br>

### (3) 단순 확인용
#### GET baseurl/posts
모든 포스트 목록을 보여줍니다. <br>
ex) GET http://127.0.0.1:8443/posts

<br>

#### GET PUT DELETE baseurl/post/<(id)>
id에 해당하는 포스트를 반환하거나, 수정하거나, 삭제합니다. <br>
ex) GET PUT DELETE http://localhost:8443/post/70

<br>

#### GET DELETE baseurl/post/<키워드>/<post_id>
키워드와 post_id에 해당하는 포스트를 반환하거나, 삭제합니다. <br>
ex) GET DELETE http://192.168.0.5:8443/post/홍대맛집/CWKs----83r

<br>

#### GET baseurl/all-keywords-alphabet
모든 키워드를 알파벳순서로 보여줍니다. <br>
ex) GET http://localhost:8443/all-keywords-alphabet

<br>

#### GET baseurl/all-posts
모든 포스트목록을 불러옵니다. <br>
페이징이 적용되어 반환됩니다. <br>
ex) GET http://localhost:8443/all-posts
