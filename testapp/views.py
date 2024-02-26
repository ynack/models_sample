from testapp import app
from flask import render_template, request, redirect, url_for
from testapp import db
from testapp.models.device import Device
import datetime

@app.route('/')
def main():
    return render_template('testapp/index.html')

@app.route('/add_device', methods=['GET', 'POST'])
def add_route():
    if request.method == 'GET':
        return render_template('testapp/add_device.html')
    if request.method == 'POST':
        device = Device(
            name = 'iMac',
            type = 'Mac',
            model = 'MQRxxJ/A',
            year = datetime.date(2023,10,30)
        )
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('main'))