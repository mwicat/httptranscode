import SimpleHTTPServer
import movieutil


class StreamingHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def send_head(self):
        path = self.translate_path(self.path)
        if movieutil.is_movie(path):
            self.send_response(200)
            self.send_header("Content-type", 'video/x-matroska')
            self.end_headers()
            f = movieutil.transcode(path)
        else:
            f = SimpleHTTPServer.SimpleHTTPRequestHandler.send_head(self)
        return f


if __name__ == '__main__':
    SimpleHTTPServer.test(StreamingHTTPRequestHandler)
