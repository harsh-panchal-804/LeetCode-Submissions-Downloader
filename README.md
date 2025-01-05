# Project Title

This python script downloads all the accepted submissions from leetcode.com and saves them in a folder called "correct_submissions" in the same directory as the script. All the submissions are saved as .txt files.

## Prerequisites

- Python 3.x


## Demo

Watch the demonstration video below:

<video src="./resources//Recording 2025-01-05 183854.mp4" controls width="720"></video>


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harsh-panchal-804/LeetCode-Submissions-Downloader.git
   ```
   
2. Run the project:
   ```
   python script.py
   ```

## Usage

Provide a step-by-step guide on how to use your project:

1. Step 1: Get your LeetCode session cookie from the browser's dev tools.
2. Step 2: Replace the `session_cookies` dictionary with your LeetCode session cookie.
3. Step 3: Run the script.
4. If you get an error like `An error occurred: 403 Client Error: Forbidden for url: https://leetcode.com/api/submissions/?offset=580`.Replace the `offset` variable with your last offset and run the script again. Continue this until you have downloaded all the submissions.



