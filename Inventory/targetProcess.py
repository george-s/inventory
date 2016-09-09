print "HELLO"

import base64 
import urllib2 
import urllib 
import xml.etree.ElementTree as ET

class Target_Process(): 
    def __init__(self, tp_name, access_token): 
        self.tp_uri = tp_name
        self.access_token = access_token
    def get_object_as_xml_string(self, type, id): 
		request = (self.tp_uri + type + '/' + id + '/?access_token=' + self.access_token) 
		response = urllib2.urlopen(request)
		txt = response.read() 
		return txt
    def get_objects_as_xml_string(self, type): 
		request = (self.tp_uri + type + '/' + '/?access_token=' + self.access_token) 
		response = urllib2.urlopen(request)
		txt = response.read()
		return txt
    def get_objects_as_et(self, type): 
		request = (self.tp_uri + type + '/' + '/?access_token=' + self.access_token) 
		response = urllib2.urlopen(request)
		txt = response.read()
		root = ET.fromstring(txt)
		return root