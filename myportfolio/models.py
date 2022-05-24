from django.db import models
from ckeditor.fields import RichTextField


class Personal(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField()
    what_i_do = models.CharField(max_length=500)
    content = RichTextField()
    github = models.CharField(max_length=500)
    hackerrank = models.CharField(max_length=500)
    leetcode = models.CharField(max_length=500)


class Skills(models.Model):
    name = models.CharField(max_length=500)


class SoftSkills(models.Model):
    name = models.CharField(max_length=500)


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = RichTextField()
    brief = models.CharField(max_length=150)
    github_link = models.CharField(max_length=200, blank=True, null=True)
    website_link = models.CharField(max_length=200, blank=True, null=True)
    content = RichTextField()


class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    positon = models.CharField(max_length=100)
    content = RichTextField()


class Contact(models.Model):
    name = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    msg = models.TextField()