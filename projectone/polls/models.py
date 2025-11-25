from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(default='',blank=True,editable=False,unique=True,db_index=True) 
    isActive = models.BooleanField()
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50,blank=True)
    date = models.DateTimeField(auto_now=True,)
    isActive = models.BooleanField()
    slug = models.SlugField(default='',editable=True,blank=True,unique=True,db_index=True) 
    #category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    
    def save(self,*args,**kwargs):
         # Eğer slug boşsa title'dan oluştur
        if not self.slug:
            base_slug = slugify(self.title)
        else:
            base_slug = slugify(self.slug)

        slug = base_slug
        counter = 1

        # Aynı slug varsa, sonuna -2, -3, ... ekle
        while Course.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug
        super().save(args,kwargs)
        
    def __str__(self):
        return f"{self.title}"
