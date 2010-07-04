class Release:
    """
        Release information:
            - name : (str) package name
            - version_info : (tuple<int,int,int,str,int>) The five components of the version number: major, minor, micro, releaselevel, and serial.
            - version : (str) package version in format x.y.z
            - version_description : (str) short description for the current version
            - version_number : (int) x*100 + y*10 + z
            - description : (str) package description
            - long_description : (str) longer package description
            - authors : (dict<str(last name), tuple<str(full name),str(email)>>) package authors
            - url : (str) package url
            - download_url : (str) package download url
            - platform : (seq<str>) list of available platforms
            - keywords : (seq<str>) list of keywords
            - licence : (str) the licence"""
    name = 'rsbac-python'
    version_info = (0, 0, 1, 'beta', 0)
    version = '.'.join(map(str, version_info[:3]))
    version_description = 'First version, mostly architecture design.'
    version_number = int(version.replace('.',''))
    description = 'A python binding for the rsbac system'
    long_description = 'This module implements the rsbac API mapping'
    license = 'GPL'
    authors = { 
                'TristanC'    : ('Tristan de Cacqueray',     'tcacqueray@gcm-sarl.eu'),
              }
    url = 'http://www.rsbac.org'
    download_url = 'http://www.rsbac.org'
    platform = ['Linux']
    keywords = ['rsbac', 'binding']

