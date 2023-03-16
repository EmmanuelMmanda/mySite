from django.db import models


class Tag(models.Model):
    tag_title = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_title


class Post(models.Model):
    title = models.CharField(max_length=100,null=False)
    thumbnail = models.ImageField(upload_to='uploads')
    text = models.TextField()
    slug = models.SlugField(null=False)
    created_on = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comment')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text


class Gallery(models.Model):
    title = models.CharField(max_length=30, null=True)
    thumbnail = models.ImageField(upload_to='uploads/gallery')
    created_on = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag,related_name="gallery")

    def __str__(self):
        return self.title




