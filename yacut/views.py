from flask import flash, redirect, render_template

from . import app
from .forms import UrlCutForm
from .messages import SHORT_ALREADY_EXIST, SHORT_ALREADY_EXIST_FORM
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlCutForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    # short = form.custom_id.data or URLMap.generate_unique_short_id()
    # # if not short:
    # #     short = URLMap.generate_unique_short_id()
    # # if not is_short_unique(short):
    # #     flash(SHORT_ALREADY_EXIST.format(short=short))
    # #     return render_template('index.html', form=form)
    # url_map = URLMap(
    #     original=form.original_link.data,
    #     short=short
    # )
    # db.session.add(url_map)
    # db.session.commit()
    try:
        url_map =  URLMap.create_in_db(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        return render_template(
            'index.html',
            **{'form': form, 'short': url_map.short}
        )
    except ValueError as error:
        flash(SHORT_ALREADY_EXIST_FORM.format(short=form.custom_id.data))



@app.route('/<short_id>')
def redirect_to_original(short_id):
    return redirect(
        URLMap.get_url_map_or_404(short=short_id).original
    )
