from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Содержание')

    @property
    def get_count_of_likes(self):
        likes = Mark.objects.filter(post_id=self.id).filter(mark='LIKE').count()
        return likes

    @property
    def get_count_of_dislikes(self):
        dislikes = Mark.objects.filter(post_id=self.id).filter(mark='DISLIKE').count()
        return dislikes

    def __str__(self):
        return self.title
    # Like
    # dislike
    #
    # кол-во лайков, кол-во дизлайков


class Mark(models.Model):
    MARKS = [('LIKE', 'LIKE'), ('DISLIKE', "DISLIKE")]
    mark = models.CharField(choices=MARKS, max_length=8,blank=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id','post_id')

    def __str__(self):
        return f'реакция для поста: {self.post_id.title}'