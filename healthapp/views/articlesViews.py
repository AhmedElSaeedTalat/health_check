#!/user/bin/python3
""" view module for Medicines API """
from flask import Blueprint, render_template, session, redirect, url_for
from flask import abort, request, jsonify
from flask_login import current_user
from healthapp.views.forms import ArticleForm
import os
import secrets


article_views = Blueprint('article_views', __name__, url_prefix='/articles')


def save_image(image_file):
    """
    function to save image in path, and renaming file name using
    secrets
    """
    from healthapp import app
    random_name = secrets.token_hex(8)
    _, extention = os.path.splitext(image_file.filename)
    image_name = random_name + extention
    path = os.path.join(app.root_path, 'static/img', image_name)
    image_file.save(path)
    return image_name


@article_views.route('/add-article', methods=['GET', 'POST'],
                     strict_slashes=False)
def display_articleForm():
    """ display a form to add articles """
    from healthapp.models.users import User
    from healthapp.models.articles import Article
    from healthapp import db
    article_form = ArticleForm()
    if request.method == 'POST':
        if article_form.validate_on_submit():
            title = article_form.title.data
            content = article_form.content.data
            user_id = current_user.id
            image = save_image(article_form.image.data)
            article = Article(title=title, content=content,
                              image=image, user_id=user_id)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('home'))
    if current_user.is_authenticated:
        user_id = current_user.id
        user = User.query.filter_by(id=user_id).first()
        if user.role == 'client':
            return redirect(url_for('home'))
        elif user.role == 'author':
            return render_template('articleform.html',
                                   article_form=article_form)
    else:
        return redirect(url_for('home'))
