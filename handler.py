#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import cgi
import datetime
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import RequestHandler, template


import utils

get_path = utils.path_getter(__file__)

class BaseHandler(RequestHandler):
    
    def render_template(self, template_name, template_dict=None):
        if template_dict is None:
            template_dict = {}
        template_path = get_path(
            os.path.join('templates', '%s.html' % template_name))
        self.response.out.write(
            template.render(template_path, template_dict))

class AboutUsPage(BaseHandler):
  def get(self):
    self.render_template('about_us')

class ContactLensPage(BaseHandler):
  def get(self):
    self.render_template('contact_lens')
    
class EyeTestPage(BaseHandler):
  def get(self):
    self.render_template('eye_test')
    
class GlassesPage(BaseHandler):
  def get(self):
    self.render_template('glasses')
    
class HomePage(BaseHandler):
  def get(self):
    self.render_template('home')
    
class LocationPage(BaseHandler):
  def get(self):
    self.render_template('location')

class PractisePage(BaseHandler):
  def get(self):
    self.render_template('practise')
    
class SpecialistEquiptmentPage(BaseHandler):
  def get(self):
    self.render_template('specialist_equiptment')
    
class WindowDisplaysPage(BaseHandler):
  def get(self):
    self.render_template('window_displays')
    

application = webapp.WSGIApplication([
  ('/', HomePage),
  ('/location',                 LocationPage),
  ('/practise',                 PractisePage),
  ('/eye_test',                 EyeTestPage),
  ('/contact_lens',             ContactLensPage),
  ('/specialist_equiptment',    SpecialistEquiptmentPage),
  ('/about_us',                 AboutUsPage),
  ('/glasses',                  GlassesPage),
  ('/window_displays',          WindowDisplaysPage),
], debug=True)


def main():
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
