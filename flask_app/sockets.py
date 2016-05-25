from flask.ext.socketio import send, emit, join_room, leave_room, SocketIO
from flask import request, jsonify
from flask.ext.login import current_user

import redis

socketio = SocketIO()

r = redis.StrictRedis(host='web_games_redis')

@socketio.on('connect')
def hello():
  join_room('pub room')
  r.sadd('pub room', current_user.username)
  r.sadd(current_user.username, 'pub room')
  emit("room change", 'pub room')
  emit("room update", [x.decode('UTF-8') for x in r.smembers(current_user.username)])
  emit('user joined', [x.decode('UTF-8') for x in r.smembers('pub room')], room='pub room', broadcast=True)

@socketio.on('disconnect')
def goodbye():
  for room in r.smembers(current_user.username):
      r.srem(room, current_user.username)
      emit('user left', current_user.username, broadcast=True)

@socketio.on('chat message')
def handle_chat(message, room):
  if message[0] == '/':
    command = message[1:].split(' ')
    parse_command(command[0], *command[1:])
  else:
    emit('chat message', (current_user.username, message, room), room=room, broadcast=True)

@socketio.on('join')
def join(room):
    #TODO: Consider permission check
    r.sadd(room, current_user.username)
    r.sadd(current_user.username, room)
    join_room(room)
    emit('user joined', [x.decode('UTF-8') for x in r.smembers(room)], room=room, broadcast=True)

@socketio.on('leave')
def leave(room):
    r.srem(room, current_user.username)
    r.srem(current_user.username, room)
    leave_room(room)
    emit('user left', current_user.username, room=room, broadcast=True)

def parse_command(command, *args):
  if command == 'help':
    emit("command response", "No help yet exists")
  if command == 'room':
    if len(args) > 0:
      room = ' '.join(args)
      r.sadd(room, current_user.username)
      r.sadd(current_user.username, room)
      join_room(room)
      emit("room change", room)
      emit("user joined", [x.decode('UTF-8') for x in r.smembers(room)], room=room, broadcast=True)
      emit("command response", "Joined room %s" %(room))
    else:
      rooms = [x.decode('UTF-8') for x in r.smembers(current_user.username)]
      emit("command response", "Currently in %s room%s: %s" %(
                                                              'this' if len(rooms) == 1 else 'these',
                                                              's' if len(rooms) > 0 else '',
                                                              ', '.join(rooms)
      ))
  if command == 'leave':
    if len(args) > 0:
      room = ' '.join(args)
      if room != 'pub room':
        r.srem(room, current_user.username)
        r.srem(current_user.username, room)
        leave_room(room)
        emit("room change", "pub room")
        emit('room left', room)
        emit('user left', (current_user.username, room), room=room, broadcast=True)
        emit('command response', 'Left room %s' %(room))
      else:
        emit('command response', 'Cannot leave pub room')
    else:
      emit('command response', "No room name given.")
