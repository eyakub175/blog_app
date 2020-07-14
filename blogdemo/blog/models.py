from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.author_name


class Category(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='article_img')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    #auth_bio = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
