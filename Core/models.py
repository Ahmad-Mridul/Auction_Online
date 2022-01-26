from django.db import models


class Categories(models.Model):
    slug = models.CharField(max_length=50,default=None)
    cat_Name = models.CharField(max_length=200, default="")
    cat_img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.cat_Name


# Create your models here.
class Product(models.Model):
    p_img = models.ImageField(upload_to='media')
    p_name = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_description = models.CharField(max_length=200, default='')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name


# class Vehicles(models.Model):
#     v_img = models.ImageField(upload_to='media')
#     v_name = models.CharField(max_length=50)
#     v_price = models.IntegerField()
#     v_description = models.CharField(max_length=200, default='')
#
#     def __str__(self):
#         return self.v_name
#
#
# class Jewelry(models.Model):
#     j_img = models.ImageField(upload_to='media')
#     j_name = models.CharField(max_length=50)
#     j_price = models.IntegerField()
#     j_description = models.CharField(max_length=200, default='')
#
#     def __str__(self):
#         return self.j_name
#
#
# class Watches(models.Model):
#     w_img = models.ImageField(upload_to='media')
#     w_name = models.CharField(max_length=50)
#     w_price = models.IntegerField()
#     w_description = models.CharField(max_length=200, default='')
#
#     def __str__(self):
#         return self.w_name
#
#
# class Coins(models.Model):
#     c_img = models.ImageField(upload_to='media')
#     c_name = models.CharField(max_length=50)
#     c_price = models.IntegerField()
#     c_description = models.CharField(max_length=200, default='')
#
#     def __str__(self):
#         return self.c_name
#
#
# class Realestate(models.Model):
#     r_img = models.ImageField(upload_to='media')
#     r_name = models.CharField(max_length=50)
#     r_price = models.IntegerField()
#     r_description = models.CharField(max_length=200, default='')
#
#     def __str__(self):
#         return self.r_name
#
#
# class Electronics(models.Model):
#     e_img = models.ImageField(upload_to='media')
#     e_name = models.CharField(max_length=50)
#     e_price = models.IntegerField()
#     e_description = models.CharField(max_length=200, default='')
#
#     def __str__(self):
#         return self.e_name
