





import codecs
import mimetypes

from uuid import uuid4
from io import BytesIO

from .packages import six
from .packages.six import b

writer = codecs.lookup('utf-8')[3]


def choose_boundary():
    
    return uuid4().hex


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


def iter_fields(fields):
    
    if isinstance(fields, dict):
        return ((k, v) for k, v in six.iteritems(fields))

    return ((k, v) for k, v in fields)


def encode_multipart_formdata(fields, boundary=None):
    
    body = BytesIO()
    if boundary is None:
        boundary = choose_boundary()

    for fieldname, value in iter_fields(fields):
        body.write(b('--%s\r\n' % (boundary)))

        if isinstance(value, tuple):
            if len(value) == 3:
                filename, data, content_type = value
            else:
                filename, data = value
                content_type = get_content_type(filename)
            writer(body).write('Content-Disposition: form-data; name="%s"; '
                               'filename="%s"\r\n' % (fieldname, filename))
            body.write(b('Content-Type: %s\r\n\r\n' %
                       (content_type,)))
        else:
            data = value
            writer(body).write('Content-Disposition: form-data; name="%s"\r\n'
                               % (fieldname))
            body.write(b'\r\n')

        if isinstance(data, int):
            data = str(data)  

        if isinstance(data, six.text_type):
            writer(body).write(data)
        else:
            body.write(data)

        body.write(b'\r\n')

    body.write(b('--%s--\r\n' % (boundary)))

    content_type = b('multipart/form-data; boundary=%s' % boundary)

    return body.getvalue(), content_type
