from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Saved,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from datetime import datetime
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        comments = Comment.objects.all()
        now = datetime.now()
        q=request.GET.get('q', '')
        if q:
            products = products.filter(name__icontains=q)
        return render(request, "home.html", {'products':products,'datetime':now, 'commments': comments})
    

def product_detail(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    context = {
        'product':product
    }
    return render(request,'product_detail.html',context)

class SavedView(LoginRequiredMixin, View):
    def get(self, request):
        saveds = Saved.objects.filter(user=request.user)
        q=request.GET.get('q', '')
        if q:
            products = Product.objects.filter(name__icontains=q)
            saveds = saveds.filter(product__in=products)
        return render(request, 'saveds.html', {"saveds":saveds})
    
class AddRemoveSavedView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        saved_product = Saved.objects.filter(user=request.user, product=product)
        if saved_product:
            saved_product.delete()
            messages.info(request, 'Removed.')  
        else:
            Saved.objects.create(user=request.user, product=product)    
            messages.info(request, 'Saved.')  
        return redirect(request.META.get("HTTP_REFERER")) 
    
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.info(request, 'Successfully Deleted!')
        return redirect('home')
    return redirect('home')
    
def delete_product(request,pk):
    saved = Saved.objects.filter(id=pk).first()
    if saved is not None:
        saved.delete()
    return redirect('saveds')

def new_comment(request): 
    if request.method == 'POST':
        Comment.objects.create(
            author = request.user,
            body = request.POST['body']
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('home')
    return HttpResponse("add comment")
    
