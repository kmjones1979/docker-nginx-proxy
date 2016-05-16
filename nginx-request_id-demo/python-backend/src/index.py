import web
import logging

# log setup
logging.basicConfig(filename='/var/log/python/python.log',level=logging.DEBUG)

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        xreq = web.ctx.env['HTTP_X_REQUEST_ID']
        if xreq == "":
            return 'Please pass a header named X-Request-ID'
            logging.info(xreq)
        else:
            return 'X-Request-ID: ' + xreq + '\n'
            return web.ctx.env
            logging.info(xreq)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
