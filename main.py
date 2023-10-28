from taipy.gui import Gui
import taipy as tp
import pandas as pd
import os


section_1 = """
## Power Consumption Dashboard
<|{dataset}|chart|x=YearMonth|y[1]=Usage|color=blue|>
"""

dataset = pd.read_csv("data.csv")

rest = tp.Rest()
gui = Gui(page=section_1)

tp.run(
    title="Taipy Dashboard",
    host='0.0.0.0',
    port=os.environ.get('PORT', '5000'),
    debug=False,
)
    
