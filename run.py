# -*- coding:utf-8 -*-


from app.app import app


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])

