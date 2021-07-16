*****************10, 11, 13강 추가 내용 정리*********************

<장고의 모델 필드 타입>

[Charfield 와 SlugField]
- SlugField는 Charfield를 상속받은 것으로 데이터베이스 입장에서는 둘 다 같은 타입이다. 
하지만 SlugField의 경우 장고가 '이것은 Slug 목적으로 사용할 필드다!'라고 따로 정의해 둔 것이다.

[DecimalField 와 FloatField]
- 둘 다 실수 범위를 의미하지만 DecimalField가 더 정확한 값을 산출해낼 수 있다

[이메일 필드와 URL필드]
- 둘 다 형식을 검사하는 필드이며 데이터베이스 입장에서는 Charfield이다.

[UUID필드]
-from uuid import uuid4를 해준 후 uuid4()를 실행하면 32글자의 랜덤 문자열이 추출된다.
UUID필드는 이러한 값을 저장해주는 필드이다.

[GenericIPAddressField]
-IP주소를 담을 수 있는 필드로, IPv4와 IPv6 모두 담을 수 있다.

[Relation Types]
- ForeignKey : 1대n 관계로 다른 모델과의 관계를 나타내는 필드
- ManyToManyField : n대n 관계를 나타내는 필드
- OneToOneField : 1대1 관계를 나타내는 필드 

ForeignKey에 대해서는 반드시 on_delete 옵션을 설정해주어야 함.
주로 models.CASCADE 로 설정하는데, 이는 관련된 테이블이 삭제되면 
이에 소속된 테이블도 싹 다 지원 버리겠다는 의미.
(예를 들어 게시글과 댓글의 관계에서 게시글이 삭제되면 이에 소속된 댓글들도 싹 지워버린다는 것)

+ 추가: pk = primary_key!!

[ModelCls.objects -> 데이터 질의 인터페이스]

1. ModelCls.objects.all() : 해당 모델 클래스의 내용을 모두 가져옴

2. ModelCls.objects.all().order_by('-id')[:10]
 : 해당 모델 클래스의 내용 중 처음 10개만 가져오고 역순 정렬

 3. ModelCls.objects.create(title="New Title")
  : title이 New Title인 새로운 객체를 해당 모델 데이터베이스에 삽입

  + queryset.get() -> 조건을 만족하는 1개의 객체 반환
  (즉 조건을 만족하는 객체가 없거나 2개 이상일 경우 오류 발생)
  반면 queryset.first()나 queryset.last()는 각각 첫 번째 객체와 마지막 객체를 반환하는 것으로, 
  객체가 없더라도 오류는 발생되지  않고 None이 반한됨

  + filter의 모든 조건은 AND로 묶임 
  OR 조건으로 묶고 싶다면 django.db.models에서 Q를 import 해와야 함.
  (Post.objects.filter(Q(title="New title") | Q(author_name="admin"))과 같이 사용)
