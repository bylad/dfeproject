from django.db import models


# Create your models here.
class BlogPage(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=210,
                             blank=True,
                             help_text='длина до 210 символов, заполнять необязательно',
                             verbose_name='SEO Title')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='длина до 450 символов',
                                   verbose_name='SEO Description')
    h1 = models.CharField(max_length=100,
                          blank=True,
                          help_text='Описание страницы под заголовком до 100 символов',
                          verbose_name='Описание страницы')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def __str__(self):
        return self.h1


class CategoryBlog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=210,
                             blank=True,
                             help_text='длина до 210 символов, заполнять необязательно',
                             verbose_name='SEO Title')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='длина до 450 символов',
                                   verbose_name='SEO Description')
    h1 = models.CharField(max_length=100,
                          help_text='Заголовок h1 до 100 символов',
                          verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL-адрес')
    mini_description = models.CharField(max_length=100,
                                        blank=True,
                                        help_text='Описание страницы под заголовком  до 100 символов',
                                        verbose_name='Описание страницы')
    category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории в блоге'

    def __str__(self):
        return self.title
