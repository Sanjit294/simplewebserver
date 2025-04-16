## PROGRAM:
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