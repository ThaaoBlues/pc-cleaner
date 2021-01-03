import sys

DATA = {
    'aix': {
        'temp-dirs': ['/tmp', '/var/tmp', '/usr/tmp'],
        'search-paths': ['/'],
    },
    'linux': {
        'temp-dirs': ['/tmp', '/var/tmp', '/usr/tmp'],
        'search-paths': ['/'],
    },
    'win32': {
        'temp-dirs': ['C:\\Windows\\Temp', 'C:\\Users\\$(USERNAME)\\AppData\\Local\\Temp', '/usr/tmp'],
        'search-paths': ['C:\\'],
    },
    'cygwin': {
        'temp-dirs': ['/tmp', '/var/tmp', '/usr/tmp'],
        'search-paths': ['/'],
    },
    'darwin': {
        'temp-dirs': ['/tmp', '/var/tmp', '/usr/tmp'],
        'search-paths': ['/'],
    }
}

WEIGHT_NOTIFY_LIMIT = "1gb"

# transform DATA to fields depending of the platform
d = {}
if sys.version_info.major > 3 or sys.version_info.major == 3 and sys.version_info.minor >= 8:
    try:
        d = DATA[sys.platform]
    except IndexError:
        pass
else:
    for p in DATA:
        if sys.platform.startswith(p):
            d = DATA[p]
            break

for v in d:
    locals()[v.upper().replace('-', '_')] = d[v]

del DATA  # not necessary anymore, free memory
