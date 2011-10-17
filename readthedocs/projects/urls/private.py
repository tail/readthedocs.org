from django.conf.urls.defaults import *

urlpatterns = patterns('projects.views.private',
    url(r'^$',
        'project_dashboard',
        name='projects_dashboard'
    ),
    url(r'^create/$',
        'project_create',
        name='projects_create'
    ),
    url(r'^import/$',
        'project_import',
        name='projects_import'
    ),
    url(r'^upload_html/(?P<project_slug>[-\w]+)/$',
        'upload_html',
        name='projects_upload_html'
    ),
    url(r'^export/(?P<project_slug>[-\w]+)/$',
        'export',
        name='projects_export'
    ),
    url(r'^(?P<project_slug>[-\w]+)/$',
        'project_manage',
        name='projects_manage'
    ),
    url(r'^(?P<project_slug>[-\w]+)/alias/(?P<id>\d+)/',
        'edit_alias',
        name='projects_alias_edit'
    ),
    url(r'^(?P<project_slug>[-\w]+)/alias/$',
        'edit_alias',
        name='projects_alias_create'
    ),
    url(r'^(?P<project_slug>[-\w]+)/alias/list/$',
        'list_alias',
        name='projects_alias_list'
    ),
    url(r'^(?P<project_slug>[-\w]+)/edit/$',
        'project_edit',
        name='projects_edit'
    ),
    url(r'^(?P<project_slug>[-\w]+)/versions/$',
        'project_versions',
        name='projects_versions'
    ),
    url(r'^(?P<project_slug>[-\w]+)/delete/$',
        'project_delete',
        name='projects_delete'
    ),
    url(r'^(?P<project_slug>[-\w]+)/subprojects/$',
        'project_subprojects',
        name='projects_subprojects'
    ),
    url(r'^(?P<project_slug>[-\w]+)/add/$',
        'file_add',
        name='projects_file_add'
    ),
    url(r'^(?P<project_slug>[-\w]+)/(?P<file_id>\d+)/edit/$',
        'file_edit',
        name='projects_file_edit'
    ),
    url(r'^(?P<project_slug>[-\w]+)/(?P<file_id>\d+)/history/$',
        'file_history',
        name='projects_file_history'
    ),
    url(r'^(?P<project_slug>[-\w]+)/(?P<file_id>\d+)/diff/(?P<from_id>\d+)/(?P<to_id>\d+)/$',
        'file_diff',
        name='projects_file_diff'
    ),
    url(r'^(?P<project_slug>[-\w]+)/(?P<file_id>\d+)/delete/$',
        'file_delete',
        name='projects_file_delete'
    ),
)
