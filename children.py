import requests

def fetch_child_content(base_url, course_id, content_id, headers):
    """ Recursively fetch and print child content items directly beneath another content item. """
    endpoint = f"/learn/api/public/v1/courses/{course_id}/contents/{content_id}/children"
    content_response = requests.get(base_url + endpoint, headers=headers, verify=False)
    if content_response.status_code == 200:
        child_contents = content_response.json()
        print(f"Child Content for Content ID {content_id}:", child_contents)

        # Recurse into children if they have their own children
        for child_content in child_contents.get('results', []):
            if child_content.get('hasChildren', False):
                fetch_child_content(base_url, course_id, child_content['id'], headers)
    else:
        print(f"Failed to retrieve child content items for Content ID {content_id}:", content_response.status_code, content_response.text)

def fetch_contents_and_children(base_url, course_id, headers):
    """ Fetch contents of a course and their children recursively. """
    content_endpoint = f"/learn/api/public/v1/courses/{course_id}/contents"
    content_response = requests.get(base_url + content_endpoint, headers=headers, verify=False)
    if content_response.status_code == 200:
        contents = content_response.json()
        print(f"Contents for Course ID {course_id}:", contents)

        # Fetch children for each content that can have children
        for content in contents.get('results', []):
            if content.get('hasChildren', False):
                fetch_child_content(base_url, course_id, content['id'], headers)
    else:
        print(f"Failed to retrieve contents for Course ID {course_id}:", content_response.status_code, content_response.text)

# Configuration and execution
base_url = "https://ec2-54-160-110-4.compute-1.amazonaws.com"
courses_endpoint = "/learn/api/public/v1/courses"
headers = {
    'Authorization': 'Bearer WwORYUzhB00lkRHfHhW09DFBUvj5pfvh',
    'Content-Type': 'application/json'
}

# Fetch all courses
courses_response = requests.get(base_url + courses_endpoint, headers=headers, verify=False)
if courses_response.status_code == 200:
    courses = courses_response.json()
    print("Course Data:", courses)

    # Iterate through each course and fetch all contents and their children
    for course in courses.get('results', []):
        fetch_contents_and_children(base_url, course['id'], headers)
else:
    print("Failed to retrieve courses:", courses_response.status_code, courses_response.text)
