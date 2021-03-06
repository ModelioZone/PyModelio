# -*- coding: utf-8 -*-
"""
Miscellaneous functions gathered here and waiting for some refactoring.

.. moduleauthor:: jeanmariefavre

"""




#----- String functions -----------------------------------------
  
def withCapital(s):
  if len(s)==0: return ""
  else: return s[0].capitalize()+s[1:]



#----- List functions -------------------------------------------

# noinspection PyUnresolvedReferences
from java.util import List as JavaList
# noinspection PyUnresolvedReferences
from java.util import Collection as JavaCollection

def isList(x):
  # is it enough?
  return isinstance(x,list) \
         or isinstance(x,JavaCollection)
  

# FIXME: should be replaced by alaocl
def flatten(colls):
  """ flatten a collection of collections
  """
  return [item for coll in colls for item in coll]  
  
def onlyOnce(coll):
  """ return a list where elements appear only once but in the
      same order as in the given list, that is in the order of
      the first occurence. The result is a list.
      onlyOnce[2,4,2,1,1] = {2,4,1]
  """
  result = []
  for e in coll:
    if not e in result:
      result=result+[e]
  return result
  
def _addItemToGroups(element,fun,groups):
  elementKey = apply(fun,[element])
  size = len(groups)
  if size==0:
    return [(elementKey,[element])]
  else:
    (firstGroupKey,groupElements)=groups[0]
    if elementKey == firstGroupKey:
      return [(elementKey,groupElements+[element])]+groups[1:]
    else:
      return [groups[0]]+_addItemToGroups(element,fun,groups[1:])
      
def _getGroups(fun,coll):
  # groupedBy(lambda x:x//10,[22,31,11,36,34]) = [(2, [22]), (3, [31, 36, 34]), (1, [11])]
  if len(coll)==0:
    return []
  else:
    r = _addItemToGroups(coll[-1],fun,groupedBy(fun,coll[:-1]),)
    return r
    
def groupedBy(fun,coll,style="nested"):
  groups = _getGroups(fun,coll)
  return groups if style is "nested" else flatten(map(lambda (a,b):b,groups))


#----- web  ---------------------------------------------------------

# noinspection PyUnresolvedReferences
from encodings import iso8859_1
import urllib2
  
def getWebPage(url):
  """ read the content of the given url and throws an exception in case of error
  """
  return urllib2.urlopen(url).read()

