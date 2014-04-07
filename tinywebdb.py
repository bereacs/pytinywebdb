#!/usr/bin/env python
# -*- coding: ascii -*-

"""
tinywebdb
~~~~~~~~~~~

TinyWebDB is an ad-hoc API defined by the App Inventor programming environment 
(http://appinventor.org/). 

# Python Interface

The Python interface is an object-oriented interface; the TinyWebDB class creates
an object that manages the communications to and from a server implementing the 
TinyWebDB API. This approach makes it easy for the programmer to have multiple connections
to different servers (or, open multiple database connections).

# Under the Covers

The TinyWebDB interface is an HTTP POST API that has two endpoints:

/getvalue

The getvalue endpoint has a single parameter, 'tag'. The response is a JSON encoded
array: ["VALUE", tag, value]. 

/storeavalue

The storeavalue endpoint has two parameters, 'tag' and 'value'. The response is a JSON
encoded array: ["VALUE", tag, value] (echoing back what was sent). 



"""

__author__ = 'Matt Jadud (matt@jadud.com)'
__copyright__ = 'Copyright (c) 2014 Matt Jadud'
__license__ = 'GPL v2'
__vcs_id__ = '$Id$'
__version__ = '0.0.0' #Versioning: http://www.python.org/dev/peps/pep-0386/


from urlparse import urljoin
import re, httplib, urllib, json

class TinyWebDB:
  ## FIELDS
  # url    => string
  # dbname => string
    
  ## METHODS
  
  # PROCEDURE
  # __init__ -> self, string, [string]
  # PURPOSE
  # Constructor. Consumes self, a URL for the API server, and
  # an optional database name. The database name is not generally
  # implemented; this is a special feature of the server implemented
  # by Matt Jadud for use at Berea College.
  def __init__(self, host, path, dbname=False):
    self.host = host
    self.path = self.addTrailingSlash(path)
    self.fullPath = self.path
    if dbname:
      self.dbname = self.addTrailingSlash(dbname)
      self.fullPath = self.fullPath  + self.dbname
  
    
  # FIXME: Handle URLs nicely. Find a library, or do it yourself.
  def getURL(self):
    return "http://" + self.addTrailingSlash(self.host) + self.fullPath

  def addTrailingSlash (self, url):
    if not re.search('/$', url):
      url += '/'
    return url
  
  # FIXME: I need to handle errors in the opening.
  # FIXME: Use urllib2, which looks to be Python 3-safer...
  def getvalue (self, tag):
    params = urllib.urlencode({'tag': tag})
    API = self.getURL() + "getvalue"
    result  = urllib.urlopen(API, params)
    read    = result.read()
    decoded = json.loads(read)
    return decoded[2]

  def setvalue (self, tag, value):
    params = urllib.urlencode({'tag': tag, 'value' : json.dumps(value)})
    API = self.getURL() + "storeavalue"
    result  = urllib.urlopen(API, params)
    read    = result.read()
    decoded = json.loads(read)
    return {'tag': decoded[1], 'value': decoded[2]}
    