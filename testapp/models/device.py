from testapp import db
from datetime import datetime

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255)) #デバイスの名前
    type = db.Column(db.String(255)) #デバイスの種類
    model = db.Column(db.String(255)) #モデル番号
    year = db.Column(db.Date) #販売開始年月日
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)    #登録日時
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now) #更新日時