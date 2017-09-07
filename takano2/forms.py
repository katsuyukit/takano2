"""Forms module."""

from __future__ import absolute_import, print_function

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class RecordForm(FlaskForm):
    """Custom record form."""

    title = StringField(
        'Title', [validators.DataRequired()]
    )
    description = TextAreaField(
        'Description', [validators.DataRequired()]
    )
