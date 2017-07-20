from cgi import parse_qs, escape

def wcgi_application(environ, start_response):
	d = parse_qs(environ["QUERY_STRING"])
	for k,v in d.items():
		print(k + "=" + v[0])
	status = "200 OK"
	headers = [("Content-Type", "text/plain")]
	body = b"Hello, World!"
	start_response(status, headers)
	return [body]
