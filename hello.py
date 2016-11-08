def hello(environ, start_response):


        #print environ
        
        qs = environ['QUERY_STRING']
        qs = qs.strip('?/').split('&')
        data = ''
        for d in qs:
            data += d + '\n'
            
        
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
