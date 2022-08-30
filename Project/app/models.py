from email.policy import default
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User, AbstractUser

class QuestionManager(models.Manager):
    def with_tag(self, tag: str):
        tag_id = Tag.objects.filter(name=tag)[0].id
        if len(tag_id):
            return self.filter(tags = tag_id)
        else:
            return self.filter(tags = -1)

class QuestionLikesManager(models.Manager):
    def with_count_on_question_id(self, question_id: int):
        likes = LikeQuestion.objects.filter(question=question_id).count()
        return likes

class AnswerLikesManager(models.Manager):
    def with_count_on_answer_id(self, answer_id: int):
        likes = LikeAnswer.objects.filter(answer=answer_id).count()
        return likes


class AnswerManager(models.Manager):
    def with_question(self, question_id):
        return self.filter(question = question_id)
class CustomUser(User):
    avatar = models.ImageField(blank=True, null=True, default='avatar2.jpg', upload_to='avatar/%Y/%m/%d/')

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_q_set')
    tags = models.ManyToManyField(Tag, null=True, blank=True) 

    objects = QuestionManager()

    class Meta:
        abstract = False


class LikeQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_lq_set')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_lq_set')
    
    objects = QuestionLikesManager()

    class Meta:
        abstract = False
        unique_together=("user", "question")

class Answer(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_a_set')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_a_set')

    objects = AnswerManager()

    class Meta:
        abstract = False


class LikeAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_la_set')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_a_set')

    objects = AnswerLikesManager()
    
    class Meta:
        abstract = False
        unique_together=("user", "answer")




