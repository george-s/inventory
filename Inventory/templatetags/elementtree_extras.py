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

register.filter(tostring)