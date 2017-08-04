import chew_toy_web
import sys

if __name__ == '__main__':
    host = 'localhost'
    if len(sys.argv) > 1:
        chew_toy_web.instance_id = sys.argv[1]
    if len(sys.argv) > 2:
        host = sys.argv[2]
    chew_toy_web.app.run(host=host, port=int(chew_toy_web.instance_id))
    