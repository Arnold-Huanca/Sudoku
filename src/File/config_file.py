import os
from xml.dom import minidom

class Config_file:
	"""docstring for Config_file"""
	def __init__(self, name,path):
		self.name = name
		self.path = path
		
		
class Xml_file(Config_file):
	"""docstring for xml_file"""
	def __init__(self, name,path):
		Config_file.__init__(self, name, path)

	"""Creating a xml file if it doesn't exist the xml file is created"""	
	def create_xml_file(self,solver_output_type,default_algorith,difficulty_levels):
		# Create object DOM.
		implementacion_DOM = minidom.getDOMImplementation()

		# Create the object Document.
		xml_document = implementacion_DOM.createDocument(None, "Sudoko_game", None)
		raiz_documento = xml_document.documentElement


		nodo_main = xml_document.createElement("Settings_SUDOKO")

		#for solver output type
		element1 = xml_document.createElement("solver_output_type")
		element1.setAttribute("id_type","1")
		element1.appendChild(xml_document.createTextNode(solver_output_type))

		#for solver output type
		element2 = xml_document.createElement("default_algorith")
		element2.setAttribute("id_type","B")
		element2.appendChild(xml_document.createTextNode(default_algorith))

		#for solver output type
		element3 = xml_document.createElement("difficulty_levels")
		element3.setAttribute("id_type","1")
		element3.appendChild(xml_document.createTextNode(difficulty_levels))

		# Adding the elements to node.
		nodo_main.appendChild(element1)
		nodo_main.appendChild(element2)
		nodo_main.appendChild(element3)

		# adding the node.
		raiz_documento.appendChild(nodo_main)

		
		if not os.path.exists(self.path):
			os.makedirs(self.path)

			
		file_path=self.path+"\\"+self.name+".xml"
		
		# oppening the file where the XML file is save.
		xml_file = open(file_path, "w")

		#  writing across of the writexml method on head of code
		xml_document.writexml(xml_file, encoding='utf-8')
		xml_file.close()
		return file_path

	"""Read the solver output type, default algorith and difficulty levels from a xml file"""
	def read_xml_config_file(self):
		from xml.dom.minidom import parse
		doc_xml=parse(self.path+"\\"+self.name+".xml")
		for n in doc_xml.getElementsByTagName("solver_output_type"):
			outputype= n.firstChild.data
		for n in doc_xml.getElementsByTagName("default_algorith"):
			algorith= n.firstChild.data
		for n in doc_xml.getElementsByTagName("difficulty_levels"):
			level= n.firstChild.data
		return outputype,algorith,level
