import xml.etree.cElementTree  as ElementTree



class XMLBuilder:
    def __init__(self):
        self.root = ElementTree.Element("text")
        pass

    def add_child(self, key, value, attrib):
        child = ElementTree.SubElement(self.root, key, attrib)
        child.text = value

    def print_xml(self):
        content = ElementTree.tostring(self.root, encoding='utf-8')
        print content

    def save_to_file(self, file_path):
        tree = ElementTree.ElementTree(self.root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)