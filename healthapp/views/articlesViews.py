#!/user/bin/python3
""" view module for Medicines API """
from flask import Blueprint, render_template, session, redirect, url_for
from flask import abort, request, jsonify
from flask_login import current_user


article_views = Blueprint('article_views', __name__, url_prefix='/articles')
