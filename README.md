# EX01 Developing a Simple Webserver
## Date: 16/04/25

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
<html>
    <body>
        <center>
        <table border="1" align="center" cellpadding="5" bgcolor="red" >
            <caption>
                Protocal list
            </caption>
            <tr>
                <th>s.no</th><th>layer</th><th>protocals</th>
            </tr>
            <tr>
                <td>1</td><td>applicationlayer</td><td>HTTP,FTP,SSH,TELNET,DNS</td>
            </tr>
            <tr>
                <td>2</td><td>transport layer</td><td>tcp,udp</td>
            </tr>
            <tr>
                <td>3</td><td>intrnet layer</td><td>IP,IMPC</td>
            </tr>
            <tr>
                <td>4</td><td>link layer</td><td>MAC,WI-FI</td>
            </tr>
        </table>
        </center>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:

![alt text](<Screenshot (11).png>)

![alt text](<Screenshot (12).png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
