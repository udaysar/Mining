from django.shortcuts import render,get_object_or_404,redirect
from .models import Stocks
from .forms import StockForm

def stocks_list(request):
    stocks=Stocks.objects.all()
    return  render(request,'pepapp1/stock_list.html',{'stocks':stocks})

def stocks_detail(request,pk):
    stock=get_object_or_404(Stocks,pk=pk)
    return render(request,'pepapp1/stock_detail.html',{'stock':stock})

def stocks_create(request):
    if request.method=='POST':
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')

    else:
        form=StockForm()
    return render(request,'pepapp1/stock_form.html',{'form':form})
    

def stocks_update(request,pk):
    stock=get_object_or_404(Stocks,pk=pk) 
    if request.method=="POST":
        form=StockForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form=StockForm(instance=stock)
    return render(request,'pepapp1/stock_form.html',{'form':form})

def stocks_delete(request,pk):
    stock=get_object_or_404(Stocks,pk=pk)
    if request.method=="POST":
        stock.delete() 
        return redirect('stock_list')
    return render(request,'pepapp1/stock_confirm_delete.html',{'stock':stock})
  

