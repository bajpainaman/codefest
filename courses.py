import requests

def get_all_courses(base_url, headers):
    """ Fetches all courses from the system. """
    courses_endpoint = "/learn/api/public/v1/courses"
    response = requests.get(base_url + courses_endpoint, headers=headers, verify=False)
    
    if response.status_code == 200:
        courses = response.json()
        # Print each course details
        for course in courses.get('results', []):
            print(f"Course ID: {course['id']}, Course Name: {course['name']}, Description: {course.get('description', 'No description')}")
    else:
        print("Failed to retrieve courses:", response.status_code, response.text)

# Configuration
base_url = "https://ec2-54-160-110-4.compute-1.amazonaws.com"
headers = {
    'Authorization': 'Bearer WwORYUzhB00lkRHfHhW09DFBUvj5pfvh',
    'Content-Type': 'application/json'
}

# Execution
get_all_courses(base_url, headers)
