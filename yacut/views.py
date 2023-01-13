from flask import (
    flash, redirect, render_template, send_from_directory, url_for
)

from . import app
from .forms import UrlCutForm
from .messages import COMMON_SERVER_ERROR, FORM_VALIDATION_ERROR
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlCutForm()
    if not form.validate_on_submit():
        flash(FORM_VALIDATION_ERROR)
        return render_template('index.html', form=form)
    try:
        url_map = URLMap.create_in_db(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        return render_template(
            'index.html',
            form=form,
            short=url_for(
                'redirect_to_original',
                short_id=url_map.short,
                _external=True
            )
        )
    except Exception as error:
        flash(COMMON_SERVER_ERROR.format(error=str(error)))
        return render_template('index.html', form=form)


@app.route('/api/docs')
def swagger_ui():
    return render_template('swagger_ui.html')


@app.route('/api/spec')
def get_spec():
    return send_from_directory(app.root_path, 'openapi.yml')


@app.route('/<short_id>')
def redirect_to_original(short_id):
    return redirect(
        URLMap.get_url_map_or_404(short=short_id).original
    )
