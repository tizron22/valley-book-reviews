"""
------------------------------
Valley Book Reviews run.py
------------------------------
This module start the whole code running from the __init__.py file,
in the valleybookreviews folder. 

"""


import os
from valleybookreviews import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
