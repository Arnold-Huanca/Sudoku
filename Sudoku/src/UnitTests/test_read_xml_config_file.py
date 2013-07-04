import unittest
from File.config_file import Path

class Test_read_the_default_settings_from_an_XML_config_file(unittest.TestCase):

    def setUp(self):
        incorrect_path_for_xml_file="xml_config_file.xml"
        correct_path_for_xml_file="xml_config_file.xml"
        self.incorrect_path=Path(incorrect_path_for_xml_file)
        self.correct_path=Path(correct_path_for_xml_file)
      
    def test_if_a_path_is_incorrect_hould_display_the_path_not_exist(self):
        result=self.incorrect_path.checkpath(self.incorrect_path)
        self.assertFalse(result)	
if __name__=='__main__':
    unittest.main()