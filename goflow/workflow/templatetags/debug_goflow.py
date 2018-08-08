from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag('switch_user.html')
def switch_users():
    """
    Returns a menu content to switch users quickly.

    Settings required::

        settings.TEST_USERS = (('user1', 'pass1'), ...)
        settings.DEBUG = True

    FOR TESTING PURPOSE ONLY
    """
    if not settings.DEBUG: return ''
    try:
        if settings.TEST_USERS:
            pass
    except Exception:
        return ''
    
    title = 'switch user:'
    content={}
    for item in settings.TEST_USERS:
        u, p = item

        # content[u]= {' [<a href=switch/%s/%s/>%s</a>]' % (u,p,u)
        content[u] = p
    return {'title': title, 'content': content}
