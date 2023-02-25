from django.shortcuts import render

# Create your views here.
def Mobiles(request):
    mydata={'p1':'samsung',
             'p2':'vivo',
             'p3':'infinix'}
    return render(request,'template/mobile.html',mydata)



def Telivisions(request):
    mydata={'p1':'Mi TV',
            'p2':'sony',
             'p3':'LG TV'}
    return render(request,'template/Tv.html',mydata)


def  Watches(request):
    x={'p1':'Titon watch',
        'p2':'fastarck watch',
        'p3':'apple watch'}
    return render(request,'template/Watches.html',x)

def Fridges(request):
    y={'p1':'Whirpool',
       'p2':'lg',
       'p3':'samsung'}
    return render(request,'template/Fridges.html',y)

def Index(request):
    return render(request,'template/Index.html')
