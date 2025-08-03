from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Collectingdb(models.Model):
    # learn django - the easyway [youtube]  
    
    STATUS_CHOICES = (
        ('신규','신규'),
        ('완료','완료'),
        ('진행중','진행중'),
        ('보류','보류'),
    )
    CATE001_CHOICES = (
        ('모델하우스','모델하우스'),
        ('홍보관','홍보관'),
        
    )
    CATE002_CHOICES = (
        ('남성','남성'),
        ('여성','여성'),        
    )
    CATE003_CHOICES = (
        ('20대','20대'),
        ('30대','30대'),
        ('40대','40대'),
        ('50대','50대'),
        ('60대','60대'),
        ('70대','70대'),
        ('80대','80대'),        
    )
    
    # [중요 title 없앨것입니다]
    # title = models.CharField(max_length=100, verbose_name='제목', default='') 

    cate001 = models.CharField(max_length=30, choices=CATE001_CHOICES, null=True, verbose_name='분류')
    cate002 = models.CharField(max_length=30, choices=CATE002_CHOICES, null=True, verbose_name='성별')

    # dhname = models.CharField(max_length=50 ,null=True, verbose_name='미용실명')
    name = models.CharField(max_length=50 ,null=True, verbose_name='성함')
    age = models.CharField(max_length=30, choices=CATE003_CHOICES, null=True, verbose_name='연령대')
    number = models.CharField(max_length=50 ,null=True, verbose_name='연락처')
    carnumbers = models.CharField(max_length=50 ,null=True, verbose_name='차량번호')
    reservation = models.CharField(max_length=50 ,null=True, verbose_name='예약날짜')
    

    # email = models.EmailField(max_length=50 ,null=True, verbose_name='이메일')

    # promoperson = models.CharField(max_length=24, default='없음', verbose_name="추천인")   
    # [중요 필드생성 필요함]
    # input == text : 전화번호
    # input = selectboxes : 세무기장, 법인세금 신고 기타 등등
    # subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='', verbose_name='문의종류')
    # subject02 = models.CharField(max_length=50, choices=SUBJECT02_CHOICES, null=True, verbose_name='과세유형')
    # learn django - the easyway [youtube]
    # author = models.ForeignKey(User, related_name='blog_posts')
    # body = models.TextField(null=True,verbose_name='내용')
    created = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='신규', verbose_name='status')
    # input = hidden : dbcode db01 - 문의하기db  db02 -  랜딩페이지 db  db03 - 추가 홍보페이지

    terms_confirmed = models.BooleanField(max_length=10, null=True, verbose_name="개인정보 수집 동의")

    # code = models.CharField(max_length=10, default='as01') # code 문의하기, as01로 코드두어서 나중에 디비 join시킬때 사용
    # dbcode = models.CharField(max_length=20, default='db01', verbose_name='디비코드')# input = hidden : dbcode db01 - 문의하기db  db02 -  랜딩페이지 db  db03 - 추가 홍보페이지
    # dbname = models.CharField(max_length=20, default='', verbose_name='dbname')
    # dbnamekr = models.CharField(max_length=20, default='', verbose_name='DB종류')
    # address001 = models.CharField(max_length=10, choices=ADDRESS001_CHOICES, null=True, verbose_name='지역')
    address001 = models.CharField(max_length=120 ,null=True, verbose_name='거주지')        
    # address002 = models.CharField(max_length=50 ,null=True, verbose_name='주소2')        
    # 추천인정보
    # promoperson = models.CharField(max_length=50 ,null=True, verbose_name='추천인')        
    # object~~ 대신에 제목, 작성자 title name 로 나오도록
    def __str__(self):
        return self.name + ' | ' + str(self.number)
    # 설명 : class AddPostView(CreateView) 로 만든 포스트 등록 폼 저장 후에 이동할 주소
    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk':self.id})
        return reverse('home')
    # admin에서 쉽게 사용하기 위해 meta를 사용 => 1.테이블명, 2.어드민에서 사용될 이름
    class Meta:
        # db_table = 'py_user'
        verbose_name = '상담신청DB'
        verbose_name_plural = '상담신청DB'
        ordering = ['-created']

