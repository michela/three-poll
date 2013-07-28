import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import re
import logging
import json

class Poll:

    def __init__(self):
	self.options = ['optionA','optionB','optionC','optionD','optionE']
	self.votes = {} 
	for i in self.options:
		self.votes[i] = 0	

    def count_vote(self,option,value = 1):
	self.votes[str(option)] = self.votes[option] + 1
	print("%s %d" % (option,self.votes[option]))

    def results(self):
	latest = []
	for i in self.options:
		latest.append(self.votes[i])		
	return(latest)

class WSHandler(tornado.websocket.WebSocketHandler):
    """Websocket server for receiving votes from modprods poll client"""
    waiters = set()
    poll = Poll()

    def open(self):
#        print 'new connection'
	WSHandler.waiters.add(self)
        self.write_message("%s: hello " % ('poll.modprods.com'))

    def broadcast_results(self):
        for waiter in self.waiters:
		try:
			results = self.poll.results()
			msg = {'status':'ok' ,'latest':[results]}
			waiter.write_message('Content-type:application/json\n') 
			waiter.write_message(json.dumps(msg))
		except:
			logging.error("Error sending message", exc_info=True)
      
    def on_message(self, message):
        print 'message received %s' % message
	vote = re.match(r"/vote/(.*)",message)	
	msg = re.match(r"/message/(.*)",message)
	if vote:
		if vote.group(1):
			print("Vote: " + vote.group(1))
			self.poll.count_vote(vote.group(1))
	if msg:
                if msg.group(1):
                        print("Message: " + msg.group(1))
			msg = {"status":"ok"}
			self.write_message(tornado.escape.json_encode(msg))
	self.broadcast_results();

    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True

    def on_close(self):
      print 'connection closed'
      WSHandler.waiters.remove(self)

application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

