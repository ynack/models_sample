from testapp import app
from flask import render_template, request, redirect, url_for
from testapp import db
from testapp.models.device import Device
import datetime

@app.route('/')
def main():
    return render_template('testapp/index.html')

@app.route('/devices')
def device_list():
    devices = Device.query.all()
    return render_template('testapp/device_list.html', devices=devices)

@app.route('/add_device', methods=['GET', 'POST'])
def add_device():
    if request.method == 'GET':
        return render_template('testapp/add_device.html')
    if request.method == 'POST':
            form_name = request.form.get('name')
            form_type = request.form.get('type')
            form_model = request.form.get('model')
            form_year = request.form.get('year').split('-') #受け取ったform_yearを'-'で分割して配列に
            list_year = [int(i) for i in form_year] #配列にしたform_yearの格値をinteger型に変換。datetime.dateに入れる値がinteger型の必要があるため

            device = Device(
                name = form_name,
                type = form_type,
                model = form_model,
                year = datetime.date(list_year[0],list_year[1],list_year[2])
            )
            db.session.add(device)
            db.session.commit()
            return redirect(url_for('device_list'))

@app.route('/devices/<int:id>/')
def device_detail(id):
    device = Device.query.get(id)
    return render_template('testapp/device_detail.html', device=device)

@app.route('/devices/<int:id>/edit', methods=['GET'])
def device_edit(id):
    device = Device.query.get(id)
    return render_template('testapp/device_edit.html', device=device)

@app.route('/devices/<int:id>/update', methods=['POST'])
def device_update(id):
    device = Device.query.get(id)
    device.name = request.form.get('name')
    device.type = request.form.get('type')
    device.model = request.form.get('model')
    form_year = request.form.get('year').split('-') #受け取ったform_yearを'-'で分割して配列に
    list_year = [int(i) for i in form_year]
    device.year = datetime.date(list_year[0],list_year[1],list_year[2])

    db.session.merge(device)
    db.session.commit()
    return redirect(url_for('device_list'))

@app.route('/devices/<int:id>/delete', methods=['GET', 'POST'])
def device_delete(id):
    device = Device.query.get(id)
    db.session.delete(device)
    db.session.commit()
    return redirect(url_for('device_list'))