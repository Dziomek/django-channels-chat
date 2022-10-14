from .models import Room, Message


def count_messages(room):
    message_objects = Message.objects.filter(room=room)

    return {'room_name': room.name, 'messages': len(message_objects)}
