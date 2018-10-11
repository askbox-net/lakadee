# -*- coding:utf-8 -*-


from . baseapp import app

# 分割先のコードをインポート
from .views.user import user
from .views.product import product

# 分割先のコントローラー（Blueprint）を登録
app.register_blueprint(user)
app.register_blueprint(product)

