from django.db import models
from django.contrib.auth.models import User

# 게시글
class FreeBoards(models.Model):
	user = models.ForeignKey(User)
	category = models.CharField(max_length=30, blank=True)
	title = models.CharField(max_length=50, blank=True)
	contents = models.TextField(blank = True)
	pub_date = models.DateField(null=True, blank=True)
	hits = models.IntegerField(null=True, blank=True)
	file_path = models.CharField(max_length=50, null=True, blank=True)
	like = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.title


# 게시글 좋아요
class LikeArticles(models.Model):
	user = models.ForeignKey(User)
	article = models.ForeignKey(FreeBoards)
	like = models.BooleanField(default=False)
 
	def is_like(self):
		return self.like


# 게시글 댓글
class ArticleComments(models.Model):
	user = models.ForeignKey(User)
	article = models.ForeignKey(FreeBoards)
	comments = models.TextField(blank=True)
	target = models.IntegerField(null=True, blank=True) # 게시물의 댓글인 경우 0, 대댓글인 경우 해당 댓글의 id.
	pub_date = models.DateField(null=True, blank=True)
	like = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.comments


# 댓글 좋아요
class LikeComments(models.Model):
	user = models.ForeignKey(User)
	#comments = models.ForeignKey(ArticleComments)
	like = models.BooleanField(default=False)