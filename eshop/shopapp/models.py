from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(unique=True)
    Image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def grt_url(self):
        return reverse('shopapp:productsbycategory',args=[self.slug])

    def __str__(self):
            return '{}'.format(self.name)

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='product', blank=True)
    stock=models.IntegerField(default=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shopapp:procatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural ='products'

        def __str__(self):
            return '{}'.format(self.name)



