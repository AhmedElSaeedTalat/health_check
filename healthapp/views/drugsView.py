#!/user/bin/python3
""" view module for Medicines API """
from flask import Blueprint, render_template, session, redirect, url_for
from flask import abort, request, jsonify
from healthapp.views.forms import SearchForm
from flask_login import current_user
import requests


medicine_views = Blueprint('medicine_views', __name__, url_prefix='/medicines')


def request_fda(name):
    """ request data from fda """
    med_name = name
    url = 'https://api.fda.gov/drug/label.json?search=drug_interactions:{}&limit=1'.format(med_name)
    data = requests.get(url)
    status = data.status_code
    res = data.json()
    return status, res


@medicine_views.route('/med-info', methods=['POST'],
                      strict_slashes=False)
def display_med():
    """ process form request to rceive data from fda """
    form = SearchForm()
    if form.validate_on_submit():
        name = form.name.data
        status, data = request_fda(name)
        data = {'status': status, 'data': data, 'name': name}
        session['data'] = data
    #return jsonify(data)
        return redirect(url_for('medicine_views.show_data'))


@medicine_views.route('/display-med',  strict_slashes=False)
def show_data():
    """
        show received data from session from the
        redirected post form
    """
    data = session.get('data')
    return render_template('med-info.html', data=data)


@medicine_views.route('/save-drug', methods=['POST'],
                      strict_slashes=False)
def save_drug():
    """ save drug for current user """
    if current_user.is_authenticated:
        from healthapp.models.drugs import Drug
        from healthapp.models.users import User
        from healthapp import db
        data = request.get_json()
        if data:
            try:
                user = User.query.filter_by(id=current_user.id).first()
                drug = Drug(name=data, users=[user])
                db.session.add(drug)
                db.session.commit()
                return 'success'
            except Exception as e:
                print(e)


@medicine_views.route('/search', strict_slashes=False)
def searchbar():
    """ display searchbar template """
    return render_template('searchbar.html')
