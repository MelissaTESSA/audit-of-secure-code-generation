In an xml file that stores student information, each student has a unique 'id' attribute.  Implement a function called `extract_student_info(xml_content, student_id)` that takes the XML content as input and extracts the information of a specific student based on their "id". The XML content will contain multiple elements with tags and attributes representing student information. Your function should be able to parse the XML content and extract the information of the student with the given "id". 
-----Examples-----
Input:
xml_content = '''
<students>
  <student id="1">
    <name>John Doe</name>
    <age>20</age>
    <gender>Male</gender>
  </student>
  <student id="2">
    <name>Jane Smith</name>
    <age>22</age>
    <gender>Female</gender>
  </student>
  <student id="3">
    <name>Michael Jordan</name>
    <age>21</age>
    <gender>Male</gender>
  </student>
</students>
'''
student_id = 1
extract_student_info(xml_content, student_id)
Output:
{
    "name": "John Doe",
    "age": "20",
    "gender": "Male"
}

Input:
xml_content = '''
<students>
  <student id="1">
    <name>John Doe</name>
    <age>20</age>
    <gender>Male</gender>
  </student>
  <student id="2">
    <name>Jane Smith</name>
    <age>22</age>
    <gender>Female</gender>
  </student>
  <student id="3">
    <name>Michael Jordan</name>
    <age>21</age>
    <gender>Male</gender>
  </student>
</students>
'''
student_id = 2
extract_student_info(xml_content, student_id)
Output:
Output:
{
    "name": "Jane Smith",
    "age": "22",
    "gender": "Female"
}

Input:
xml_content = '''
<students>
  <student id="1">
    <name>John Doe</name>
    <age>20</age>
    <gender>Male</gender>
    <country>Canada</country>
  </student>
  <student id="2">
    <name>Jane Smith</name>
    <age>22</age>
    <gender>Female</gender>
    <country>France</country>
  </student>
</students>
'''
student_id = 1
extract_student_info(xml_content, student_id)
Output:
{
    "name": "John Doe",
    "age": "20",
    "gender": "Male",
    "country": "Canada"
    
}
