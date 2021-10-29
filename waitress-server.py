from waitress import serve
from real_matzip_api.wsgi import application
from paste.translogger import TransLogger

if __name__ == "__main__":
    serve(TransLogger(application, setup_console_handler=False), host="0.0.0.0", port=8443)
