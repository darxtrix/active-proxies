#-------this is a script for suggesting working proxy servers(py 2.7.5)------------------------
#------------------written by---> black_perl(ankush sharma) @ 21-08-2013 01:45 a.m.-------------------------------
#-------------------------for queries message me @dustin on dc---------------------------------------------------------


import httplib
import base64
import sys
import time

class proxy_checker:
    def __init__(self,proxy,port):
        self.proxy_str=proxy
        self.proxy_port=port
        self.count=0

    def connection(self):
        try:
            self.conn=httplib.HTTPConnection(proxy,port,timeout=20)#A HTTP SERVER CONNECTION CLOSES AFTER A SINGLE REQUEST
            self.start=time.time()
            self.conn.request("GET","http://www.google.com")
        except:
             self.end=time.time()
             if self.end-self.start>=15:
                 print " -----------time out error--------Server not responding,please try again-------------------"
             else:
                print "--------INVALID PROXY SERVER ADDRESS---------"
             sys.exit()

    def response_checker(self):
        self.resp=self.conn.getresponse()
        if self.resp.status==407:#proxy authentication required
            print "\n ----------------------------the server is up but requires authentication---------------------------\n"
        if self.resp.status==200:#ok response
            print "the server is up and working"
        if self.resp.status==408:#The 408 Request Timeout error is an HTTP status code that means the request you sent to the website server (e.g. a request to load a web page) took longer than the website's server was prepared to wait
            print "the server is not responding in time,timeout..try again"
        if self.resp.status==401:#http basic authentication required not necessary proxy
            print "------SERVER WORKING-------request unauthorized"
        self.conn.close()
        return self.resp.status
    
        
    def credentials(self):
        self.username=raw_input("enter username for the proxy server:")
        self.password=raw_input("enter password for the proxy server:")
        self.auth=str(base64.b64encode(self.username+":"+self.password))

    def retry(self):
        self.conn1=httplib.HTTPConnection(proxy,port)
        self.conn1.request("GET","http://www.python.org/index.html",headers={"Proxy-Authorization":"Basic "+self.auth})
        self.response=self.conn1.getresponse()
        return self.response.status
        
        
proxy=raw_input("enter the address of the proxy server:")
port=input("enter the proxy port:")
p=proxy_checker(proxy,port)
p.connection()
status=p.response_checker()
if status==407:
    p.credentials()
    if p.retry()==200:
        print "\n---AUTHENTICATED----proxy ready for use-----------------"
    else:
        print "\n    authentication failed,try again"
else:
    pass
    

    
