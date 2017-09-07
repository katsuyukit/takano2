# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio module that adds more fun to the platform."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from __future__ import absolute_import, print_function

from flask import Blueprint, redirect, render_template, request, url_for
from flask_babelex import gettext as _

from .forms import RecordForm
from .utils import create_record

blueprint = Blueprint(
    'takano2',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route("/")
def index():
    """Basic view."""
    return render_template(
        "takano2/index.html",
        module_name=_('takano2'))

@blueprint.route('/create', methods=['GET', 'POST'])
def create():
    """The create view."""
    form = RecordForm()
    # if the form is valid
    if form.validate_on_submit():
        # create the record
        create_record(
          dict(
            title=form.title.data,
            description=form.description.data
          )
        )
        # redirect to the success page
        return redirect(url_for('takano2.success'))
    return render_template('takano2/create.html', form=form)


@blueprint.route("/success")
def success():
    """The success view."""
    return render_template('takano2/success.html')
