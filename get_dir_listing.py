#!/usr/bin/python

"""
For content audit of a directory (e.g. for a website content audit).
However, this script looks at files via network path, and not via
http connections.

Inspiration from: https://github.com/terryjbates/content-audit.
"""

import os, os.path
import xlwt
from optparse import OptionParser
from bs4 import BeautifulSoup as Soup


class ContentAuditor:
  
  def __init__(self, startpath, xls_file):
    self.startpath = startpath
    self.xls_file = xls_file


  def enumeratepaths(self, path):
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
      for file in filenames:
        fullpath = os.path.join(dirpath, file)
        path_collection.append(fullpath)
    return path_collection
  

  def write_to_xls(self):
    workbook = xlwt.Workbook()
    page_name = "Files"
    current_sheet = workbook.add_sheet(page_name)
  
    current_sheet.write(0, 0, "File path => Root = " + self.startpath)
    current_sheet.write(0, 1, "File Number")
    current_sheet.write(0, 2, "HTML Title")
  
    count = 1
  
    for f in self.enumeratepaths(self.startpath):
      current_sheet.write(count, 0, f[len(self.startpath):])
      current_sheet.write(count, 1, count)  

      # if it is HTML file, then extract metadata and place in column 3 of xls
      if f.lower().endswith((".html", ".htm")):
        with open(f, 'r') as htmlFile:
          htmlSource = htmlFile.read()
          htmlSoup = Soup(htmlSource)
          if htmlSoup.title:
            current_sheet.write(count, 2, htmlSoup.title.string)
          else:
            current_sheet.write(count, 2, "")
      else:
        current_sheet.write(count, 2, "")

      count += 1
  
    workbook.save(self.xls_file)

# end class ContentAuditor


if __name__ == "__main__":

  parser = OptionParser()
  parser.add_option("-p", "--startpath", dest="startpath")
  parser.add_option("-x", "--xls-filename", dest="xls_file")

  (options, args) = parser.parse_args()

  content_bot = ContentAuditor(options.startpath, options.xls_file)
  content_bot.write_to_xls()

  print "Finished writing " + options.xls_file


