from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.id,

		class Meta(object):
			verbose_name='Товар'
			verbose_name_plural='Товар'

class ProductImage(models.Model):
	image = models.ForeignKey(Product, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='products_images/')
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.product.name,

		class Meta(object):
			verbose_name='Фотография'
			verbose_name_plural='Фотографии'