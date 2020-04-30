from django.db import models
from django.utils import timezone
from django.urls import reverse

class Product(models.Model):
  product_id = models.AutoField
  product_name = models.CharField(max_length = 50)
  category = models.CharField(max_length = 50, default="")
  sub_category = models.CharField(max_length = 50, default="")
  price = models.IntegerField(default=0)
  desc = models.CharField(max_length = 300, default="")
  pub_date = models.DateField(default=timezone.now)
  image = models.ImageField(upload_to="store/images", default="")

  def get_absolute_url(self):
    return reverse('product_detail', args=(self.id,))

  def __str__(self):
    return self.product_name
