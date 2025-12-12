import xml.etree.ElementTree as ET

def extract_student_info(xml_content, student_id):
    try:
        root = ET.fromstring(xml_content)
        for student in root.findall('student'):
            if student.find('id').text == student_id:
                return {
                    'id': student.find('id').text,
                    'name': student.find('name').text,
                    'age': student.find('age').text,
                    'grade': student.find('grade').text
                }
        return None
    except:
        return None