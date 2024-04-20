import requests

def fetch_assignments_for_course(base_url, course_id, headers):
    """ Fetch and print all assignments for a given course. """
    endpoint = f"/learn/api/public/v1/courses/{course_id}/contents"
    response = requests.get(base_url + endpoint, headers=headers, verify=False)
    
    if response.status_code == 200:
        contents = response.json()
        assignments = [content for content in contents.get('results', []) if 'assignment' in content.get('contentHandler', {}).get('id', '')]
        
        if assignments:
            print(f"Assignments for Course ID {course_id}:")
            for assignment in assignments:
                print(f"Assignment ID: {assignment['id']}, Title: {assignment['title']}")
        else:
            print(f"No assignments found for Course ID {course_id}")
    else:
        print(f"Failed to retrieve contents for Course ID {course_id}:", response.status_code, response.text)

# Configuration
base_url = "https://ec2-54-160-110-4.compute-1.amazonaws.com"
course_id = "_3_1"  # Example course ID, replace with actual ID you need
headers = {
    'Authorization': 'Bearer WwORYUzhB00lkRHfHhW09DFBUvj5pfvh',
    'Content-Type': 'application/json'
}

# Execution
fetch_assignments_for_course(base_url, course_id, headers)
