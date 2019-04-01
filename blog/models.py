from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Member(models.Model):
    name = models.CharField('成员', max_length=30, unique=True)
    parent_member = models.ForeignKey('self', verbose_name='父分类', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Member"

    def __str__(self):
        return self.name

    def get_same_level_member(self):
        if self.parent_member:
            return self.parent_member.member_set.all().exclude(id=self.id)


class Tag(models.Model):
    name = models.CharField('标签', max_length=30, unique=True)
    parent_tag = models.ForeignKey('self', verbose_name='父分类', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Tag"

    def __str__(self):
        return self.name

    def get_same_level_tag(self):
        if self.parent_tag:
            return self.parent_tag.tag_set.all().exclude(id=self.id)


class Post(models.Model):
    name = models.CharField('标题', max_length=30, unique=True)
    parent_post = models.ForeignKey('self', verbose_name='父分类', blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    deadline = models.DateTimeField(blank=True) 
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True) # autotime 
    tags = models.ManyToManyField(Tag, blank=True)
    members = models.ManyToManyField(Member, blank=True)



    class Meta:
        ordering = ['name']
        verbose_name = "Post"

    def __str__(self):
        return self.name

    def get_same_level_post(self):
        if self.parent_post:
            return self.parent_post.post_set.all().exclude(id=self.id)



