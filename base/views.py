from django.shortcuts import render, redirect
from .forms import CollectingdbForm
from django.views.generic.edit import FormView

class HomeView(FormView):
    # model = Post     
    # template_name = 'home.html'
    


    template_name = 'home.html'
    form_class = CollectingdbForm

    success_url = 'successori2'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        # context ['blog'] = Blog.objects.all()
        
        return context

class CollectdbView(FormView):
    # model = Post     
    template_name = 'collectingdb.html'
    form_class = CollectingdbForm

    success_url = 'successori2'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        # context ['blog'] = Blog.objects.all()
        
        return context
    



def successori2(request): 
    # send_mail(
    #     '[SOTOPLUS] 검사 신청 접수가 들어왔습니다.',
    #     '검사 신청 접수가 들어왔습니다. 관리자페이지를 확인해주세요! https://sotoplus.co.kr/admin/',
    #     'bluewate02@naver.com',
    #     ['bluewate02@naver.com'],
    # )
    return redirect("successree2")

def successree2(request): 
    return render(request, 'successree2.html', {}) 


def error_500(request):
    return render(request, '500.html')
def error_404(request, exception):
    return render(request, '404.html') 
