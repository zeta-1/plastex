#!/usr/bin/env python

import sys, os, re
from plasTeX.Renderer import Renderer
from plasTeX.TALUtils import htmltemplate, xmltemplate

# Regular expressions for multi-zpt files
templatere = re.compile(r'(<zpt:page-template\s+[^>]+>.*?</zpt:page-template>)', re.S)
attrsre = re.compile(r'<zpt:page-template\s+([^>]+)?\s*>')
parseattrsre = re.compile(r'\s*(\w+)\s*=\s*["\']([^"\']+)?["\']')
contentre = re.compile(r'<zpt:page-template\s+[^>]+>(.*?)</zpt:page-template>', re.S)

class XHTML(Renderer):
    
    def __init__(self):
        Renderer.__init__(self)
        self.filecount = 0
        self.importDirectory(os.path.dirname(__file__))

    def importDirectory(self, templatedir):
        """ Compile all ZPT files in the given directory """
        if templatedir and os.path.isdir(templatedir):
            files = os.listdir(templatedir)

            # Compile multi-zpt files first
            for file in files:
                file = os.path.join(templatedir, file)
                ext = os.path.splitext(file)[-1]

                # Multi-zpt files
                if ext.lower() == '.zpts':
                    content = open(file,'r').read().strip()
                    templates = templatere.split(content)
                    templates.pop()
                    while templates:
                        templates.pop(0)
                        template = templates.pop(0)
 
                        # Get macro attributes
                        attrs = attrsre.search(template).group(1) 
                        attrs = dict(parseattrsre.findall(attrs))

                        # Get content of macro
                        content = contentre.search(template).group(1) 

                        # Compile the template
                        if attrs.get('type','').lower() == 'xml':
                            template = xmltemplate(content) 
                        else:
                            template = htmltemplate(content) 

                        # Get all names in the 'name' attribute
                        names = [x.strip() for x in attrs['name'].split() 
                                           if x.strip()]
                        for name in names:
                            self[name] = template

            # Now compile macros in individual files.  These have
            # a higher precedence than macros found in multi-zpt files.
            for file in files:
                file = os.path.join(templatedir, file)
                ext = os.path.splitext(file)[-1]

                # Single zpt files
                if ext.lower() in ['.zpt','.html','.htm']:
                    content = open(file,'r').read().strip()
                    key = os.path.splitext(os.path.basename(file))[0]
                    self[key] = htmltemplate(content) 

                # XML formatted zpt files
                elif ext.lower() == '.xml':
                    content = open(file,'r').read().strip()
                    key = os.path.splitext(os.path.basename(file))[0]
                    self[key] = xmltemplate(content) 

xhtml = XHTML()

templates = os.environ.get('XHTMLTEMPLATES','')
for path in [x.strip() for x in templates.split(':') if x.strip()]:
    xhtml.importDirectory(path)

if __name__ == '__main__':
    print XHTML()
