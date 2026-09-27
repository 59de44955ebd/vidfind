import json
import os
import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt6.QtWebEngineWidgets import QWebEngineView

APP_NAME = 'vidfind'
APP_DIR = os.path.dirname(__file__)

IS_FROZEN = getattr(sys, 'frozen', False)

try:
    with open(os.path.join(APP_DIR, 'settings.json'), 'r') as f:
        APP_SETTINGS = json.loads(f.read())
except:
    APP_SETTINGS = {}

# Settings that can be overwritten by a JSON file called 'settings.json'
VIDSRC_HOST = APP_SETTINGS.get('VIDSRC_HOST', 'vidsrc.sh')
USER_AGENT = APP_SETTINGS.get('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36')

# Make QtWebEngine shut up
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --log-level=3"
QLoggingCategory.setFilterRules("*=false")

ERROR_WRONG_INPUT = 1
ERROR_SERVER_NOT_REACHED = 2
ERROR_MOVIE_NOT_FOUND = 3
ERROR_VIDEO_NOT_FOUND = 4
ERROR_UNKNOWN_ERROR = 5


########################################
#
########################################
class Main(QWebEngineView):

    ########################################
    #
    ########################################
    def __init__(self):

        self.imdb_id = None
        self.is_query = False
        self.is_query_and_load = False
        self.query_str = None

        if sys.argv[1] == '--query':
            self.is_query = True
            self.query_str = sys.argv[2]

        elif sys.argv[1].startswith('tt'):
            self.imdb_id = sys.argv[1]

        else:
            self.is_query_and_load = True
            self.query_str = sys.argv[1]

        super().__init__()

        self.page = self.page()

        self.profile = self.page.profile()
        self.profile.setHttpUserAgent(USER_AGENT)

        if self.is_query or self.is_query_and_load:
            self.page.loadFinished.connect(self.on_imdb_json_loaded)
            q = self.query_str.lower().replace(' ', '_')
            url = 'https://v2.sg.media-imdb.com/suggestion/' + ('x' if q[0] == '%' else q[0]) + '/' + q + '.json'
            self.load(QUrl(url))

        else:
            self.page.loadFinished.connect(self.on_vidsrc_json_loaded)
            url = f'https://data.{VIDSRC_HOST}/api.php?type=movie&imdb={self.imdb_id}'
            self.load(QUrl(url))

#        self.resize(1023, 744)
#        self.show()

    ########################################
    #
    ########################################
    def on_imdb_json_loaded(self):

        ########################################
        #
        ########################################
        def _on_json(data):
            self.page.loadFinished.disconnect(self.on_imdb_json_loaded)

            data = json.loads(data)

            if type(data) != dict:
                print('Error: Server not reached.', file=sys.stderr)
                QApplication.exit(ERROR_SERVER_NOT_REACHED)

            elif self.is_query:
                if 'd' in data:
                    for row in data['d']:
                        try:
                            if row['q'] == 'feature':
                                print(f"{row['id']}\t\"{row['l']}\"\t{row['y']}")
                        except:
                            pass
                    exit_code = 0
                    QApplication.exit(9)
                else:
                    print(f'Error: Unknown error.', file=sys.stderr)
                    QApplication.exit(ERROR_UNKNOWN_ERROR)

            elif self.is_query_and_load:
                if 'd' in data:
                    for row in data['d']:
                        try:
                            if row['q'] == 'feature':
                                self.imdb_id = row['id']
                                self.page.loadFinished.connect(self.on_vidsrc_json_loaded)
                                self.load(QUrl(f'https://data.{VIDSRC_HOST}/api.php?type=movie&imdb={self.imdb_id}'))
                                return
                        except:
                            pass

                    print('Error: Movie not found.', file=sys.stderr)
                    self.close()
                    sys.exit(ERROR_MOVIE_NOT_FOUND)
                else:
                    print('Error: Unknown error.', file=sys.stderr)
                    self.close()
                    sys.exit(ERROR_UNKNOWN_ERROR)

        self.page.toPlainText(_on_json)

    ########################################
    #
    ########################################
    def on_vidsrc_json_loaded(self):

        ########################################
        #
        ########################################
        def _on_json(data):
            self.page.loadFinished.disconnect(self.on_vidsrc_json_loaded)

            data = json.loads(data)

            if type(data) != dict:
                print('Error: Server not reached.', file=sys.stderr)
                QApplication.exit(ERROR_SERVER_NOT_REACHED)

            elif int(data['status_code']) != 200:
                print('Error: Video not found.', file=sys.stderr)
                QApplication.exit(ERROR_VIDEO_NOT_FOUND)

            else:
                self.load_video()

        self.page.toPlainText(_on_json)

    ########################################
    #
    ########################################
    def load_video(self):

        ########################################
        # Implementing the QWebEngineUrlRequestInterceptor interface and installing the interceptor
        # on the profile enables intercepting, blocking, and modifying URL requests before they
        # reach the networking stack of Chromium.
        ########################################
        class UrlRequestInterceptor(QWebEngineUrlRequestInterceptor):

            ########################################
            #
            ########################################
            def interceptRequest(me, info):
                url = info.requestUrl().toString()
                if '/master.m3u8' in url:
                    print(url)
                    QApplication.exit(0)

        self.ri = UrlRequestInterceptor()
        self.profile.setUrlRequestInterceptor(self.ri)

        ########################################
        #
        ########################################
        def _on_vidsrc_loaded(ok):
            frame = self.page.mainFrame()
            for c in frame.children():
                c.runJavaScript("if (document.querySelector('#bigPlay')) document.querySelector('#bigPlay').click()")

        self.page.loadFinished.connect(_on_vidsrc_loaded)

        url = f'https://{VIDSRC_HOST}/embed/{self.imdb_id}'
        self.load(QUrl(url))


########################################
#
########################################
if __name__ == '__main__':
    if len(sys.argv) < 2 or (sys.argv[1] == '--query' and len(sys.argv) < 3):
        print(
            (
                '\nUsage:\n\n'
                f'{APP_NAME} imdb-id\n'
                f'{APP_NAME} "some movie title"\n'
                f'{APP_NAME} --query "some movie title"'
            ),
            file=sys.stderr
        )
        sys.exit(ERROR_WRONG_INPUT)
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())
