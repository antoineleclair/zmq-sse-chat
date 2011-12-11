import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('ipc:///tmp/zmq.test')
socket.setsockopt(zmq.SUBSCRIBE, 'test')

while True:
    msg = socket.recv()
    print msg.replace('test ', '')
