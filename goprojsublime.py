# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import os

def find_project_file(dir, filenames=None):
  """
  Find project file config, recursion up to tree
  @param current dir path
  @filenames string or array name variants
  @return (projectdir, absfilepath)
  """

  if not dir:
    return None, None

  if not filenames:
    filenames = ['config.goproj', '.goproj']
  elif isinstance(filenames, basestring):
    filenames = [filenames]

  for fname in filenames:
    pathname = '%s/%s' % (dir, fname)
    if os.path.isfile(pathname) or os.path.islink(pathname):
      return dir, os.path.realpath(pathname)

  if len(dir)<1 or dir=='/':
    return None, None

  return find_project_file(dir=os.path.dirname(dir), filenames=filenames)

############################
##### SUBLIME COMMANDS #####
############################

class GoprojEditCommand(sublime_plugin.TextCommand):
  def run(self, text):
    d, goprojFile = find_project_file(os.getcwd())
    if d is None:
      sublime.status_message('Can`t find .goproj file')
    else:
      sublime.status_message('Open file: %s' % goprojFile)
      sublime.active_window().open_file(goprojFile)
