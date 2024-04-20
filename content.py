import requests

# Your API base URL
base_url = "https://ec2-54-160-110-4.compute-1.amazonaws.com"

# Endpoint for getting course data
courses_endpoint = "/learn/api/public/v1/courses"

# Headers including the bearer token for authorization
headers = {
    'Authorization': 'Bearer WwORYUzhB00lkRHfHhW09DFBUvj5pfvh',  # Use your actual token here
    'Content-Type': 'application/json'
}

# Make a GET request to fetch courses
courses_response = requests.get(base_url + courses_endpoint, headers=headers, verify=False)

# Check if the request for courses was successful
if courses_response.status_code == 200:
    courses = courses_response.json()
    print("Course Data:", courses)

    # Iterate through each course and fetch contents
    for course in courses.get('results', []):  # Assuming the results are under 'results'
        course_id = course['id']
        content_endpoint = f"{courses_endpoint}/{course_id}/contents"
        
        # Make a GET request for each course's content
        content_response = requests.get(base_url + content_endpoint, headers=headers, verify=False)

        if content_response.status_code == 200:
            content = content_response.json()
            print(f"Content for Course ID {course_id}:", content)
        else:
            print(f"Failed to retrieve content for Course ID {course_id}:", content_response.status_code, content_response.text)
else:
    print("Failed to retrieve courses:", courses_response.status_code, courses_response.text)
