# main.py
import assignments
import courses
import token
import os

def main():
    base_url = "https://ec2-54-160-110-4.compute-1.amazonaws.com"
    
    # Assuming token.py has a function to get the access token
    client_id = 'd2005857-4fe4-4717-b223-f8636f1c8504'
    client_secret = 'whdxgoh9BnY3MxPeOCN58rO0Bac6eRSy'
    access_token = token.get_access_token(base_url, client_id, client_secret)

    if not access_token:
        print("Failed to retrieve access token. Exiting...")
        return

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Assuming courses.py can fetch all courses and returns a list of course IDs
    try:
        course_ids = courses.fetch_all_courses(base_url, headers)
    except Exception as e:
        print(f"Failed to fetch courses: {e}")
        return

    if not course_ids:
        print("No courses found. Exiting...")
        return

    # Loop through each course and fetch assignments
    for course_id in course_ids:
        try:
            print(f"Fetching assignments for course ID: {course_id}")
            assignments.fetch_assignments_for_course(base_url, course_id, headers)
        except Exception as e:
            print(f"Failed to fetch assignments for course ID {course_id}: {e}")

if __name__ == "__main__":
    main()
