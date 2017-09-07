"""Utils module."""

from __future__ import absolute_import, print_function

import uuid

from flask import current_app

from invenio_db import db
from invenio_indexer.api import RecordIndexer
from invenio_pidstore import current_pidstore
from invenio_records.api import Record


def create_record(data):
    """Create a record.

    :param dict data: The record data.
    """
    indexer = RecordIndexer()
    with db.session.begin_nested():
        # create uuid
        rec_uuid = uuid.uuid4()
        # add the schema
        host = current_app.config.get('JSONSCHEMAS_HOST')
        data["$schema"] = \
            current_app.extensions['invenio-jsonschemas'].path_to_url(
            'custom_record/custom-record-v1.0.0.json')
        # create PID
        current_pidstore.minters['custid'](
          rec_uuid, data, pid_value='custom_pid_{}'.format(rec_uuid)
        )
        # create record
        created_record = Record.create(data, id_=rec_uuid)
        # index the record
        indexer.index(created_record)
    db.session.commit()
