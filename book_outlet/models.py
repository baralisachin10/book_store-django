from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)

    def __str__(self):
        return self.city;
    
    class Meta:
        verbose_name_plural = ("Address Entries")



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete= models.CASCADE, null = True)

    def __str__(self):
        return self.first_name;



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Author, on_delete= models.CASCADE, null= True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)
    published_country = models.ManyToManyField(Country)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
