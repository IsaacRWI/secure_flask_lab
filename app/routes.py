from flask import Blueprint, render_template
from app.forms import NameForm

main = Blueprint('main', __name__) # This is a blueprint registered with the app in __init__.py

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    name = None

    if form.is_submitted():
        name = form.name.data
        form.name.data = '' # Clear the input field after submission

    return render_template('index.html', form=form, name=name)
