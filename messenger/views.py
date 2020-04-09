from django.shortcuts import render, redirect
from login.models import User
from .models import Message, Comment
from django.http import JsonResponse

def render_messages_home(request, id):
	if request.session['logged_on']:
		context = {
			'posts': Message.objects.filter(recieving_user=User.objects.get(id=id)).order_by('-created_at'),
			'user': User.objects.get(id=id)
		}
		return render(request, 'messages_home.html', context)
	else:
		return redirect('/')

def post_message(request):
	if request.method == 'POST':
		Message.objects.create(message=request.POST['new_message'], recieving_user=User.objects.get(id=request.POST['recieving_user']), sending_user=User.objects.get(id=request.session['user_id']))
	return redirect(request.META.get('HTTP_REFERER'))

def post_comment(request):
	if request.method == 'POST':
		Comment.objects.create(comment=request.POST['new_comment'], sending_user=User.objects.get(id=request.session['user_id']), message_id=request.POST['message_id'])
	return redirect(request.META.get('HTTP_REFERER'))

def delete_post(request):
	data = {}
	if request.GET.get('post_id', None) != None:
		post_id = request.GET.get('post_id', None)
		Message.objects.get(id=post_id).delete()
		data['deleted'] = True
	elif request.GET.get('comment_id', None) != None:
		comment_id = request.GET.get('comment_id', None)
		Comment.objects.get(id=comment_id).delete()
		data['deleted'] = True
	return JsonResponse(data)