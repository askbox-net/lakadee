# -*- coding:utf-8 -*-


from . baseapp import app
from . baseapp import init_master

init_master()

# 分割先のコードをインポート
from .views.user import user
from .views.product import product
from .views.real_estate import real_estate
from .views.image import image

# 分割先のコントローラー（Blueprint）を登録
app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(real_estate)
app.register_blueprint(image)

