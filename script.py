import requests
import os
import time
import re

# Replace this with your LEETCODE_SESSION cookie value
# to find your cookie value go to leetcode.com ,open dev tools(CTRL+SHIFT+I)
# and go to the network tab. Then open any request (eg graphql/)
# and copy the value of the cookie named LEETCODE_SESSION
#ensure that you are logged in to leetcode during the script execution
session_cookies = {
    "LEETCODE_SESSION": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfcGFzc3dvcmRfcmVzZXRfa2V5IjoiY2ozZXN5LTBkOGZjMGVkNTMzYzZjYTRhZWViYTZlZWM5ZTQwODUzIiwiX2F1dGhfdXNlcl9pZCI6IjExMTcwOTAxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiM2U2MWM2M2U2N2E4YzY3OGY3ZjQ3ZDkyMzYxZTVjNTEwNWZkNTVhMGU2YzE5MTE1NGU4MWZjM2I4ZGY2ZTIzMSIsInNlc3Npb25fdXVpZCI6ImZiYzVkNDZmIiwiaWQiOjExMTcwOTAxLCJlbWFpbCI6ImhhcnNocGFuY2hhbDUyMkBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImhhcnNocGFuY2hhbDUyMiIsInVzZXJfc2x1ZyI6ImhhcnNocGFuY2hhbDUyMiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9oYXJzaHBhbmNoYWw1MjIvYXZhdGFyXzE3MTg5NzkxODcucG5nIiwicmVmcmVzaGVkX2F0IjoxNzM2MDAyMDQ1LCJpcCI6IjI0MDU6MjAxOjIwMjM6ODQ0Ojk5ZmI6ZWI5YTo0YzAyOjMwNmUiLCJpZGVudGl0eSI6ImY1MWJiNDgyYzY2MGQwZWVhZGQxZjA1ODA1OGEyYjM1IiwiZGV2aWNlX3dpdGhfaXAiOlsiZTU5MzE2ZmFkZDI2ZTUyNDFmODY5OTJhZWM3NWIzZWIiLCIyNDA1OjIwMToyMDIzOjg0NDo5OWZiOmViOWE6NGMwMjozMDZlIl0sIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.blG_WCJB8ETH1dkyWhGxp2d8K19-4ZbE_bVsenfNQMw"
}

# Create a session object
session = requests.Session()
session.cookies.update(session_cookies)

# URL to get submissions for the logged-in user
submissions_url = "https://leetcode.com/api/submissions/"
os.makedirs("correct_submissions", exist_ok=True)

offset = 580 # You will get an error and when you do replace this variable with your last offset 

while True:
    try:
        response = session.get(submissions_url, params={"offset": offset})
        response.raise_for_status()  
        submissions = response.json()
        if "submissions_dump" not in submissions or not submissions["submissions_dump"]:
            break

        for submission in submissions["submissions_dump"]:
            if submission.get("status_display") == "Accepted": # only fetches accepted submissions
                problem_title = submission["title"]
                # Sanitize the title to make it a valid file name
                sanitized_title = re.sub(r'[\\/*?:"<>|]', "", problem_title)
                file_name = f"correct_submissions/{sanitized_title}.txt"
                # Save the code to the file
                # change this code to save the submission as you want , by default it saves the code as .txt file
                code = submission["code"]
                with open(file_name, "w") as file:
                    file.write(code)
                print("Downloaded submission:", submission["title"])

        
        if len(submissions["submissions_dump"]) < 20:
            break

        offset += 20 # Max increment allowed is 20 due to LeetCode's API limitations
        # To prevent overwhelming the server, add a small delay between requests
        
        time.sleep(1)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        break

print("Correct submissions downloaded successfully!")
