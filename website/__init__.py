import os
from flask import Flask

# state available calculation_types for web
available_cal_types =  ['Bitwise and ( & )','Bitwise NAND (x)','Bitwise NOR (x)','Bitwise NOT ( ~ )','Bitwise or ( | )','Bitwise XOR ( ^ )']
# get all the images associated in gate folder
images = os.listdir(os.path.join(os.getcwd(),'website\static\images\gates'))
gate_images_lst = [ "/static/images/gates/"+ i for i in images]

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "asdfghjklqzxwecvrtbnyum"

    from .views import views
    page_not_found = ""
    app.register_blueprint(views,url_prefix = "/")
    # app.register_error_handler(404,page_not_found)

    return app