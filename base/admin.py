from django.contrib import admin
from .models import Collectingdb




class CollectingdbAdmin(admin.ModelAdmin):
    # list_filter = ('price', 'name', ) 추후에 상태 컬럼이 필요한 모델에는 
    # 'status' ex. 완료 진행중 둘중 하나로 어드민에서 '필터' 가능하도록 할 것
    #
    list_filter = ('cate001', 'name', 'age', 'number', 'reservation', 'cate002', 'address001', 'carnumbers' , 'created', )
    list_display = ('cate001', 'name', 'age', 'number', 'reservation', 'cate002', 'address001', 'carnumbers' , 'created', )
    # 



    def changelist_view(self, request, extra_context = None):
        extra_context = { 'title': '상담신청DB' }
        return super().changelist_view(request, extra_context)

admin.site.register(Collectingdb, CollectingdbAdmin)
admin.site.site_header = '관리자 페이지'

admin.site.index_title = '관리자 페이지'
admin.site.site_title = '관리자 페이지'