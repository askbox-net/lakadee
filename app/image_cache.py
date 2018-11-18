# -*- coding:utf-8 -*-

import sqlite3
import base64
import re
import tempfile
import hashlib
import json



def base64img(base64str):
    if base64str is None or len(base64str) == 0:
        return None

    try:
        base64_md5 = hashlib.md5(base64str.encode('utf-8')).hexdigest()
        print('base64_md5:', base64_md5)
        mime_re = re.search('^data:(image/.+);base64,', base64str)
        print('mime = ', mime_re.group(0))
        print('mime = ', mime_re.group(1))
        mime = mime_re.group(1)
        base64str = re.sub('^data:image/.+;base64,', '', base64str)
        imgdata = base64.b64decode(base64str)
        """
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(imgdata)
            temp_filename = tf.name

        #mime = filetype.guess(temp_filename).mime
        #print('mime : ', mime)
        print('temp_filename:', temp_filename)

        with open(temp_filename, 'rb') as fp:
            binary = fp.read()
        """

    except Exception as e:
        print('error1:', e)
        return None

    return { 'mime': mime, 'checksum': base64_md5, 'binary': imgdata }


class ImageObject(object):
    def __init__(self, dbpath):
        # データベース接続とカーソル生成
        self.connection = sqlite3.connect(dbpath)
        # 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
        # connection.isolation_level = None
        self.connection.row_factory = sqlite3.Row

    def Insert(self, user_id, obj):
        if obj is None:
            return

        cursor = self.connection.cursor()
        print('mime:', obj['mime'], ' checksum:', obj['checksum'])
        sql = "select count(id) as cnt from images where checksum='%s'" % obj['checksum']
        cursor.execute(sql)
        if cursor.fetchone()['cnt'] == 0:
            checksum = obj['checksum']
            mime = obj['mime']
            binary = obj['binary']
            sql_img = "insert into images(user_id,checksum,mime,binary) values(?,?,?,?)"
            self.connection.execute(sql_img, [user_id, checksum, mime, binary])
            self.connection.commit()
    
    def GetId(self, obj):
        if obj is None:
            return None

        cursor = self.connection.cursor()
        sql = "select id from images where checksum='%s'" % obj['checksum']
        cursor.execute(sql)
        #print(obj['checksum'], 'id = ', cursor.fetchone()['id'])
        return cursor.fetchone()['id']

    def UpdateImgIds(self, id, img_ids):
        print('json:', id, json.dumps(img_ids))

        sql = "update real_estates set img_ids=? where id=?"
        self.connection.execute(sql, [json.dumps(img_ids), id])
        self.connection.commit()


    def Exec(self):
        sql = "select * from real_estates"
        cursor = self.connection.cursor()
        cursor.execute(sql) # select文をexecute()に渡す

        for row in cursor:  # レコードを出力する
            img_ids = []
            id = row['id']
            user_id = row['user_id']
            img1 = row['img1']
            img2 = row['img2']
            img3 = row['img3']
            img4 = row['img4']
            img5 = row['img5']
            img6 = row['img6']

            img_obj = base64img(img1)
            self.Insert(user_id, img_obj)
            img_id = self.GetId(img_obj)
            if img_id:
                img_ids.append(img_id)

            img_obj = base64img(img2)
            self.Insert(user_id, img_obj)
            img_id = self.GetId(img_obj)
            if img_id:
                img_ids.append(img_id)

            img_obj = base64img(img3)
            self.Insert(user_id, img_obj)
            img_id = self.GetId(img_obj)
            if img_id:
                img_ids.append(img_id)

            img_obj = base64img(img4)
            self.Insert(user_id, img_obj)
            img_id = self.GetId(img_obj)
            if img_id:
                img_ids.append(img_id)

            img_obj = base64img(img5)
            self.Insert(user_id, img_obj)
            img_id = self.GetId(img_obj)
            if img_id:
                img_ids.append(img_id)

            img_obj = base64img(img6)
            self.Insert(user_id, img_obj)
            img_id = self.GetId(img_obj)
            if img_id:
                img_ids.append(img_id)
            

            self.UpdateImgIds(id, img_ids)




if __name__ == '__main__':
    # データベースファイルのパス
    dbpath = 'lakadee.sqlite'
    obj = ImageObject(dbpath)
    obj.Exec()

