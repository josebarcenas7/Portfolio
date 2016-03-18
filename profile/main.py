import webapp2
import os
import logging
import jinja2
import nav

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

newfile=nav.get_names()

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        try:
            page = self.request.path
            print 'attempting to access______'
            page=page[page.find("/")+1:page.find(".")]
            page = page.capitalize()
            if page =='Index':
                page = 'Home'

            template_values={
              'title': page,
              'names':newfile,
            }

            template = JINJA_ENVIRONMENT.get_template('template%s'% self.request.path)
            self.response.write(template.render(template_values))
        except:
            print 'access failed!'
            template_values={
              'title': 'Home',
              'page': 'HOME',
              'names':newfile
            }
            template = JINJA_ENVIRONMENT.get_template('template/index.html')
            self.response.write(template.render(template_values))

            #outstr = template.render(temp, { })
            #self.response.out.write(outstr)


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/projects.html', IndexHandler),
    ('/contact.html', IndexHandler),
    ('/resume.html', IndexHandler)
], debug=True)
