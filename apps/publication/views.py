import json
from apps.common.features import *
from django.http import HttpResponse


def publish_to_wall(request):
    """
    Publish a publiation to a wall.
    :param request:
    :return:
    """
    author = request.user
    message = request.GET.get('message', None)
    publish_message(author, message)

    return HttpResponse(json.dumps({'ok':'ok'}))


def comment_status(request):
    """
    Comment a publication.
    :param request:
    :return:
    """
    comment(request)

    return HttpResponse(json.dumps({'ok':'ok'}))


def delete_comment(request):
    """
    Delete a comment.
    :param request:
    :return:
    """
    id_publication = request.GET.get('id_publication', None)
    Comment.objects.get(id=id_publication).delete()

    return HttpResponse(json.dumps({'ok': id_publication}))


def delete_status(request):
    """
    Delete a publication.
    :param request:
    :return:
    """
    id_publication = request.GET.get('id_publication', None)
    status = Status.objects.get(id=id_publication)
    for comment in status.comments.all():
        status.comments.remove(comment)

    for notification in Notification.objects.filter(status=status):
        notification.delete()

    Status.objects.get(id=id_publication).delete()

    return HttpResponse(json.dumps({'ok': id_publication}))
