from django.db import models
from django.urls import reverse
from django.conf import settings

ON_DISCOUNT = [
  ('Y', 'yes'),
  ('N', 'no')
]

LABEL_CHOICES = [
  ('P', 'primary'),
  ('S', 'secondary'),
  ('D', 'danger')
]


class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class SubCategory(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Product(models.Model):
  product_id = models.AutoField
  product_name = models.CharField(max_length = 50)
  label = models.CharField(choices=LABEL_CHOICES, max_length=1)
  on_discount = models.CharField(choices=ON_DISCOUNT, max_length=1)
  category = models.ForeignKey(Category, related_name='Category', blank=True, on_delete=models.CASCADE)
  sub_category = models.ForeignKey(SubCategory, related_name='SubCategory', blank=True, on_delete=models.CASCADE)
  discount_price = models.FloatField()
  price = models.FloatField(default=0)
  desc = models.CharField(max_length = 300, default="")
  pub_date = models.DateTimeField(auto_now_add=False)
  image = models.ImageField(upload_to="store/images", default="")

  def get_absolute_url(self):
    return reverse('product_detail', args=(self.id,))

  def __str__(self):
    return self.product_name

class Contact(models.Model):
  msg_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50, default="")
  phone = models.CharField(max_length=70, default="")
  desc = models.CharField(max_length=500, default="")

  def __str__(self):
    return self.name


class OrderLine(models.Model):
  item = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Order(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  item = models.ManyToManyField(OrderLine)
  start_date = models.DateTimeField(auto_now_add=True)
  ordered_date = models.DateTimeField()
  ordered = models.BooleanField(default=False)
  pass

  def __str__(self):
    return self.username