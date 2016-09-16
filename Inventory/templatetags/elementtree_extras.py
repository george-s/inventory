import xml.etree.cElementTree as ET
from django import template

register = template.Library()

##
# Serializes an element structure to XHTML (or just plain XML).

def tostring(elem):
    "Serialize element structure to XHTML."
    if not ET.iselement(elem):
        return elem
    return ET.tostring(elem)

def tostringgetname(elem):
    "Serialize element structure to XHTML."
    if not ET.iselement(elem):
        return elem
    return elem.attrib['Name']

# result = tp.get_objects_as_et('UserStories')
# print result
# for child in result:
# 		#print(child.tag, child.attrib)
# 		print child.attrib['Name']


register.filter(tostring)
register.filter(tostringgetname)
