import json
from apps.common.features import *
from django.http import HttpResponse


def publish_to_wall(request):
    author = request.user
    message = request.GET.get('message', None)
    publish_message(author, message)

    return HttpResponse(json.dumps({'ok':'ok'}))


def comment_status(request):
    comment(request)

    return HttpResponse(json.dumps({'ok':'ok'}))


def delete_comment(request):
    id_publication = request.GET.get('id_publication', None)
    Comment.objects.get(id=id_publication).delete()

    return HttpResponse(json.dumps({'ok': id_publication}))


def delete_status(request):
    id_publication = request.GET.get('id_publication', None)
    status = Status.objects.get(id=id_publication)
    for comment in status.comments.all():
        status.comments.remove(comment)

    for notification in Notification.objects.filter(status=status):
        notification.delete()

    Status.objects.get(id=id_publication).delete()

    return HttpResponse(json.dumps({'ok': id_publication}))
