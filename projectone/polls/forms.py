from django import forms


from polls.models import Category, Course


class CourseCreateForm(forms.Form):
    title = forms.CharField(min_length=3,max_length=50,
        label="Kurs başlığı",
        error_messages={
            "required":"Kurs başlığı girmelisiniz."
        },
        widget=forms.TextInput(attrs={"id":"title"}),
        )
    description = forms.CharField(widget=forms.Textarea,label="Kurs Açıklaması",error_messages={
            "required":"Kurs açıklaması girmelisiniz."
        })
    imageUrl = forms.CharField(max_length=50,label="Kurs Fotoğrafı",error_messages={
            "required":"Kurs fotoğrafı yüklemelisiniz"
    })
    slug = forms.SlugField(required=False,label="Kurs Slugı")
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}),
                               label="Kurs Tarihi",
                               required=False)#aradığın şey
    
    isActive=forms.BooleanField(required=False,label="Kurs Açık Mı?",error_messages={
        "required":"Kurs Hatasını girmelisiniz."
    })


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=('name','isActive') #'__all__' herşeyi ekler
        labels ={'name':'Kategori İsmi',
                 'isActive':'Aktif mi?',
                 }



class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','imageUrl','isActive','slug','categories')
        labels ={
            'title':'Başlık',
            'description':'Açıklama',
            'imageUrl':'Resim',
            'isActive':'Aktif mi?',
            'slug':'Slug',
            'categories':'Kategoriler', 
        }
        widgets = {
            "categories":forms.SelectMultiple()
        }