from random import choice
from string import ascii_letters, digits

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import UrlCutForm
from .models import URLMap


def create_random_short(base_url='http://yacut.ru', lenght=6):
    return (
        f'{base_url}/{"".join([choice(ascii_letters + digits) for _ in range(lenght)])}'
    )

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlCutForm()
    if form.validate_on_submit():
        short = form.short.data
        if short and URLMap.query.filter_by(short=short).first():
            flash('Short is already used')
            return render_template('index.html', form=form)
    url = URLMap(
        
    )
    return render_template('index.html', form=form)
        