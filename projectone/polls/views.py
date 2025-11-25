from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse,Http404
from django.urls import reverse
from polls.forms import CategoryCreateForm, CourseCreateForm, CourseEditForm
from .models import Course , Category
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    sayfa_basi_sayisi=3

  
    kurslar = Course.objects.filter(isActive=1)   #list comphension  
    kategoriler = Category.objects.filter(isActive=1)
    paginator = Paginator(kurslar,sayfa_basi_sayisi)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)
    # for kurs in db["courses"]:
    #     if kurs["isActive"] == True:
    #         kurslar.append(kurs)
    # list comphension yapabilirsin
    print("buraya girdi indexe yani")
    
    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar,
        'page_obj':page_obj,
    })


def create_course(request):
    if request.method == "POST":
        title = request.POST["title"]
        description =request.POST["description"]
        imageUrl =request.POST["imageUrl"]
        date =request.POST["date"]
        slug = request.POST["slug"]
        isActive = request.POST.get("isActive",False)
        
        error =False
        messages=[]
    
        if isActive == "on":
            isActive=True

        
        if title == "":
            error =True
            messages.append("Lütfen title alanını boş bırakmayınız!")
            
        if description == "":
            error =True
            messages.append("Lütfen description alanını boş bırakmayınız!")

        if imageUrl == "":
            error =True
            messages.append("Lütfen imageUrl alanını boş bırakmayınız!")

        if len(title)<5 or len(title)>50:
            error =True
            messages.append("Title alanı en az 5,en fazla 50 karakter olmalıdır!")
            
        if len(imageUrl)>50:
            error =True
            messages.append("imageUrl alanı en fazla 50 karakter olmalıdır!")
        
        

        if error:

            return render(request,"courses/create-course.html",{"error":True, "messages":messages})

    


        kurs =Course(title=title,description=description,imageUrl=imageUrl,date=date,slug=slug,isActive=isActive)
        kurs.save()
        return redirect("/")
    return render(request,"courses/create-course.html")



def create_course_2(request):
    
    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        error = []
        
        if form.is_valid():
            kurs = Course(title=form.cleaned_data["title"],
                          description = form.cleaned_data["description"],
                          isActive = form.cleaned_data["isActive"],
                          imageUrl = form.cleaned_data["imageUrl"],
                          slug = form.cleaned_data["slug"],
                          date = form.cleaned_data["date"]    
                          )   
                    
            kurs.save()
            if kurs.isActive:
                url = reverse("details", kwargs={"slug_name": kurs.slug})           
            else:
                url = '/'
            return redirect(url)

    else:        
        form = CourseCreateForm()
    return render(request,"courses/create-course-new-method.html",{"form":form})

def create_category(request):
    if request.method == "POST":
        form = CategoryCreateForm (request.POST)
        error = []
        
        if form.is_valid():
            form.save()
            
            return redirect('/')

    else:        
        form = CategoryCreateForm()
    return render(request,"courses/create-category.html",{"form":form})
    
def course_list(request):
    kurslar = Course.objects.all()
    
    return render(request,'courses/course-list.html',{
        'courses':kurslar, 
    })

def course_edit(request, id):
    course = get_object_or_404(Course,pk=id)
    if request.method == "POST":
        form = CourseEditForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            print("kayıt yapıldı")
            return redirect("course_list")
        print(form.errors.as_json())
    else:
        form = CourseEditForm(instance=course)
    return render(request,"courses/edit-course.html",{"form":form,})

def course_delete(request,id):
    course = get_object_or_404(Course,pk=id)
    if request.method=="POST":
        pass 


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q =request.GET["q"]
        kurslar = Course.objects.filter(isActive=True,title__contains=q).order_by("-date")
        kategoriler = Category.objects.all()

        sayfa_basi_sayisi=3
        paginator = Paginator(kurslar,sayfa_basi_sayisi)
        page = request.GET.get('page',1)
        page_obj = paginator.page(page)
        
        
        return render(request,"courses/list.html",{    
            'page_obj':page_obj,
            'categories':kategoriler,
            'q':q,
        })
    else:
        return redirect("/")
    

    


def details(request,slug_name):
    try:
        course = Course.objects.get(slug=slug_name)
        context ={
            'course':course
        }
        return render(request,"courses/details.html",context)
    except:
        raise Http404()
        
    

def iletisim(request):
    return HttpResponse('<h1>iletisim sayfası</h1>')

def getPollsByCategory(request,slug):
    sayfa_basi_sayisi=3
    kurslar = Course.objects.filter(categories__slug=slug,isActive=True).order_by("-date")
    kategoriler = Category.objects.all()
    paginator = Paginator(kurslar,sayfa_basi_sayisi)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)
    
    print("buraya girdi getpollsa yani yani")
    
    return render(request,"courses/index.html",{    
        'page_obj':page_obj,
        'categories':kategoriler,
        'selectedCategory':slug,


        })

# def getPollsByCategory(request,pollsType_name):

    # try:
    #     text=f"{pollsType_name}".replace("-"," ") + " kategorisindeki tüm sonuçlar"

    #     return render(request,"courses/courses.html",{
    #         'category':pollsType_name,
    #         'text':text,
    #         'data':data
    #     })
    
    # except:
    #     return HttpResponseNotFound("Yanlış kategori seçimi")
 




  