#!/user/bin/python3
""" view module for Medicines API """
from flask import Blueprint, render_template, session, redirect, url_for
from flask import abort, request, jsonify
from healthapp.views.forms import SearchForm
from flask_login import current_user
import requests
import hmac
import hashlib
import base64
import json

medicine_views = Blueprint('medicine_views', __name__, url_prefix='/medicines')


class MakeRequests:
    """ class that makes api requests """
    def request_fda(self, name):
        """ request data from fda """
        med_name = name
        url = 'https://api.fda.gov/drug/label.json?search=drug_interactions:{}&limit=1'.format(med_name)
        data = requests.get(url)
        status = data.status_code
        res = data.json()
        return status, res

    def request_token(self):
        """ function to request symptoms """

        url = 'https://sandbox-authservice.priaid.ch/login'
        api_key = 'ahmedelsaeed105@gmail.com'
        secret_key = 'q9FMo4y7YPk35Axb8'
        hashed_data = hmac.new(secret_key.encode(), url.encode(),
                               hashlib.md5).digest()
        token = base64.b64encode(hashed_data).decode('utf-8')
        headers = {'Authorization': 'Bearer ' + api_key + ':' + token}
        request = requests.post(url, headers=headers)
        received_token = request.json()['Token']
        return received_token

    def request_listSymptoms(self):
        """ function to list symptoms """
        token = self.request_token()
        url = 'https://sandbox-healthservice.priaid.ch/symptoms'
        headers = {'autherization': token, 'content-type': 'application/json'}
        params = {'token': token, 'language': 'en-gb'}
        return requests.get(url, params=params, headers=headers)

    def request_diagnosisAPI(self, data):
        """ with args passed diangnosis request is made """
        token = self.request_token()
        url = 'https://sandbox-healthservice.priaid.ch/diagnosis'
        symptoms = json.dumps(data['symptoms'])
        print('heeeeeeeeeeey', symptoms)
        headers = {'autherization': token, 'content-type': 'application/json'}
        params = {'token': token, 'symptoms': symptoms,
                  'gender': data['gender'], 'year_of_birth': int(data['year']),
                  'language': 'en-gb'}
        response = requests.get(url, params=params, headers=headers)
        return response


@medicine_views.route('/med-info', methods=['POST'],
                      strict_slashes=False)
def display_med():
    """ process form request to rceive data from fda """
    form = SearchForm()
    if form.validate_on_submit():
        name = form.name.data
        fda_request = MakeRequests()
        status, data = fda_request.request_fda(name)
        data = {'status': status, 'data': data, 'name': name}
        session['data'] = data
    #return jsonify(data)
        return redirect(url_for('medicine_views.show_data'))


@medicine_views.route('/drug-deatails', methods=['POST'],
                      strict_slashes=False)
def get_details():
    """ post request from js """
    name = request.get_json()
    fda_request = MakeRequests()
    status, data = fda_request.request_fda(name['name'])
    data = {'status': status, 'data': data, 'name': name}
    session['data'] = data
    if status == 200:
        return 'success'


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


@medicine_views.route('/health-checker', strict_slashes=False)
def health_check():
    """
    form to list symptoms and choose from to check
    for symptoms
    """
    req = MakeRequests()
    if session.get('symptoms'):
        symptoms = session.get('symptoms')
        return render_template('symptoms.html', symptoms=symptoms)
    else:
        symptoms = req.request_listSymptoms()
        symptoms = symptoms.json()
        session['symptoms'] = symptoms
        return render_template('symptoms.html', symptoms=symptoms)


@medicine_views.route('/diagnosis', methods=['POST'],
                      strict_slashes=False)
def request_diagnosis():
    """ 
    function to make api request
    to request diagnosis for symptoms
    """
    data = request.get_json()
    make_request = MakeRequests()
    response = make_request.request_diagnosisAPI(data)
    response = response.json()
    return jsonify(response)

