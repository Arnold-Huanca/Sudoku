import os.path
from xml.dom.minidom import parse
class Config_file(object):
	"""docstring for Config_file"""
	def __init__(self, path, solver_output_type, default_algorith, difficulty_levels):

		#super(Config_file, self).__init__()			
		self.solver_output_type = solver_output_type
		self.default_algorith = default_algorith
		self.difficulty_levels = difficulty_levels

	def read_xml_config_file(self,path):
		#doc1_xml=parse("C:\Users\jonas aramayo\Desktop\prueba.xml")
		doc_xml=parse(path)
		#print doc_xml
		#toxml: este metodo nos devuelve el codigo XML.
		#firstChild: esta propiedad es el enlace al primer nodo hijo
		#getAttribute: obtiene el valor de una propiedad determinada del tag
		#attributes: es un diccionario de propiedades del tag
		for n in doc_xml.getElementsByTagName("solver_output_type"):
			#print("::::::::::::::::::::::::::::")
			#print n.toxml()
			return n.firstChild.data
			#print n.firstChild.data
			#print n.getAttribute("type")
			#print n.attributes.keys()
			#print n.attributes["tipo"].value
		for n in doc_xml.getElementsByTagName("default_algorith"):
			return n.firstChild.data
		for n in doc_xml.getElementsByTagName("difficulty_levels"):
			return n.firstChild.data
	
class Path:
	"""docstring for Path"""
	def __init__(self, path):
		#super(Path, self).__init__()
		self.path = path
		
	def checkpath(self,path):
		if os.path.isdir("xml_config_file.xml"):
			print "El directorio existe"
		else:
			print "El directorio no existe"
		
