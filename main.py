from taipy.gui import Gui
import taipy as tp
import pandas as pd
from gevent.pywsgi import WSGIServer
section_1 = """
## Power Consumption Dashboard
<|{dataset}|chart|x=YearMonth|y[1]=Usage|color=blue|>
"""

dataset = pd.read_csv("data.csv")

gui = Gui(page=section_1)

if __name__ == '__main__':
    app = gui.run(title='Dashboard',
    		dark_mode=False)
    
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()