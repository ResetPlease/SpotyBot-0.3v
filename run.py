from __init__ import app
from waitress import serve
#app.run(debug = True)
serve(app,host="0.0.0.0", port=5000)
