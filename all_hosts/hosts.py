from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'', 'all_hosts.app.urls', name='main'),
    host(r'help', 'all_hosts.help.urls', name='help'),
)
