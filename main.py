from taipy.gui import Gui
import pandas as pd
import os

section_1 = """
## Power Consumption Dashboard
<|{dataset}|chart|x=YearMonth|y[1]=Usage|color=blue|>
"""

dataset = pd.read_csv("data.csv")

gui = Gui(page=section_1)

if __name__ == '__main__':
    gui.run(title='Dashboard',
    		dark_mode=False)
else:
    app = gui.run(title='Dashboard',
                  dark_mode=False)