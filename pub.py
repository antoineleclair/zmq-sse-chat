import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('ipc:///tmp/zmq.test')

while True:
    msg = raw_input(':')
    socket.send(msg)
