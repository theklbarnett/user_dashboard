from django.db import models
from login.models import User

class Message(models.Model):
	message = models.TextField()
	sending_user = models.ForeignKey(User, related_name="s_messages", on_delete = models.CASCADE)
	recieving_user = models.ForeignKey(User, related_name="r_messages", on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	comment = models.TextField()
	sending_user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
	message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)