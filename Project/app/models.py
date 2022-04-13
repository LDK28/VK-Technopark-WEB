from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def with_tag(self, tag: str):
        tag_id = Tag.objects.filter(name=tag)[0].id
        if len(tag_id):
            return self.filter(tags = tag_id)
        else:
            return self.filter(tags = -1)


class AnswerManager(models.Manager):
    def with_question(self, question_id):
        return self.filter(question = question_id)

class Profile(User):
    avatar = models.ImageField()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        abstract = False
    
class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = False

class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, null=True)

    objects = QuestionManager()

    class Meta:
        abstract = False


class LikeQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        abstract = False

class Answer(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = AnswerManager()

    class Meta:
        abstract = False


class LikeAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        abstract = False



