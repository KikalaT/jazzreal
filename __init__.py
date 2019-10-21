import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
SECRET_KEY='dev',
)
<<<<<<< HEAD
# ensure the instance folder exists
=======
>>>>>>> 119765ce96705c5203d8148c1fd3b091f4ac5c5f
try:
	os.makedirs(app.instance_path)
except OSError:
	pass
