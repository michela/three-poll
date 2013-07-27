import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import re

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message("%s: hello " % ('poll.modprods.com'))
      
    def on_message(self, message):
#        print 'message received %s' % message
	vote = re.match(r"/vote/(.*)",message)	
	msg = re.match(r"/message/(.*)",message)
	try:
		if vote.group(1):
			print("Vote: " + vote.group(1))
			self.write_message("ok")
	except Exception as e:
		#print(e)
		pass
        try:
                if msg.group(1):
                        print("Message: " + msg.group(1))
			self.write_message("ok")
        except Exception as e:
                #print(e)
		pass

    def on_close(self):
      print 'connection closed'

application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

