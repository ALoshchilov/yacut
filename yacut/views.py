from random import choice
from string import ascii_letters, digits

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import UrlCutForm
from .models import URLMap
from .utils import generate_unique_short_id, is_short_unique

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlCutForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.custom_id.data
    if not short:
        short = generate_unique_short_id()
    if not is_short_unique(short):
        flash('Short is already used')
        return render_template('index.html', form=form)
    url_map = URLMap(
        original = form.url.data,
        short = short
    )
    db.session.add(url_map)
    db.session.commit()
    return render_template('index.html', form=form)

@app.route('/<short_id>')
def redirect_to_original(short_id):
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original
    )
