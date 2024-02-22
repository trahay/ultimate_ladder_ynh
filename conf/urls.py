"""
    urls.py
    ~~~~~~~
"""
from django.conf import settings
from django.urls import include, path
from django.views.static import serve

import ultimate_ladder


if settings.PATH_URL:
    # settings.PATH_URL is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path(f'{settings.PATH_URL}/', include('ultimate_ladder.urls')),
        #
        # TODO: Serve from nginx server ;)
#        path(f'{settings.PATH_URL}/<path:path>', serve, {'document_root': ultimate_ladder.WEB_PATH})
                path(f'{settings.PATH_URL}/<path:path>', serve, {'document_root': '/'})
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from ultimate_ladder.urls import urlpatterns  # noqa

    # TODO: Serve from nginx server ;)
#    urlpatterns.append(path('<path:path>', serve, {'document_root': ultimate_ladder.WEB_PATH}))
    urlpatterns.append(path('<path:path>', serve, {'document_root': '/'}))
