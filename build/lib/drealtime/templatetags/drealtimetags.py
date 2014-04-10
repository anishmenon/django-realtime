from django.conf import settings
from django.template import Library
register = Library()

def _determine_base_path():
    client = getattr(settings, 'ISHOUT_CLIENT_ADDR', 'localhost:5500')
    secure = getattr(settings, 'ISHOUT_HTTPS', False)
    proto = 'http'
    if secure:
        proto = 'https'

    return '%s://%s' % (proto, client)    

@register.simple_tag
def ishout_socketio_path():
    return '%s/%s' %(_determine_base_path(), 'socket.io/socket.io.js')

@register.simple_tag
def ishout_js_path():
    return '%s/%s' %(_determine_base_path(), 'client/ishout.client.js')


@register.simple_tag
def ishout_js():
    """
    returns the needed HTML tags for including ishout.js and its dependency
    (socket.io) in the client's browser. make sure that `ISHOUT_CLIENT_ADDR`
    is in the settings.py file and is reachable from the internet, as
    it will be used as the domain name. if you are using ishout.js over
    SSL, be sure to set `ISHOUT_HTTPS` to True.
    """
    path = _determine_base_path()
    return """
    <script type="text/javascript" src="%s/socket.io/socket.io.js"></script>
    <script type="text/javascript" src="%s/client/ishout.client.js"></script>
    """ % (path, path)