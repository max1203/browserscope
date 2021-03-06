#!/usr/bin/python2.5
#
# Copyright 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the 'License')
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Handlers for Rich Text Tests"""

__author__ = 'annie.sullivan@gmail.com (Annie Sullivan)'

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import django
from django import http
from django import shortcuts

from django.template import add_to_builtins
add_to_builtins('base.custom_filters')

# Shared stuff
from categories import all_test_sets
from base import decorators
from base import util


CATEGORY = 'richtext'


def About(request):
  """About page."""
  overview = """These tests cover browers' implementations of 
  <a href="http://blog.whatwg.org/the-road-to-html-5-contenteditable">contenteditable</a>
  for basic rich text formatting commands. Most browser implementations do very
  well at editing the HTML which is generated by their own execCommands. But a
  big problem happens when developers try to make cross-browser web
  applications using contenteditable - most browsers are not able to correctly
  change formatting generated by other browsers. On top of that, most browsers
  allow users to to paste arbitrary HTML from other webpages into a
  contenteditable region, which is even harder for browsers to properly
  format. These tests check how well the execCommand, queryCommandState,
  and queryCommandValue functions work with different types of HTML. Please
  note that these are WYSIWYG editing tests, not semantic editing tests. Any
  HTML which produces a given visual style should be changeable via the
  execCommand for that style."""
  return util.About(request, CATEGORY, category_title='Rich Text',
                    overview=overview, show_hidden=False)


def EditableIframe(request):

  params = {}
  return shortcuts.render_to_response('richtext/templates/editable.html', params)
