from lxml import etree

def parse_medications():
    # Load and parse the XML file
    try:
        tree = etree.parse('lab_1/data/lab_sample.xml')
        # Find all medications in the XML structure
        medications = tree.xpath('//medication')

        # Extract and print medication details
        for medication in medications:
            name = medication.find('name').text
            dose = medication.find('dose').text
            frequency = medication.find('frequency').text
            print(f"name: {name}\ndose: {dose}\nfrequency: {frequency}\n")
    except FileNotFoundError:
        print("The XML file was not found. Please ensure it is located in 'lab_1/data/lab_sample.xml'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parse_medications()

