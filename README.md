# Project Title

This python script downloads all of your accepted submissions and saves them in a folder called "correct_submissions" in the same directory as the script. All the submissions are saved as .txt files.


## Demo

Watch the demonstration below:

![Demo GIF](./resources/Recording%202025-01-05%20183854%20(1).gif)




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

1. Step 1: Get your LeetCode session cookie from the browser's dev tools.
2. Step 2: Replace the `session_cookies` dictionary with your LeetCode session cookie.
3. Step 3: Run the script.
4. If you get an error like `An error occurred: 403 Client Error: Forbidden for url: https://leetcode.com/api/submissions/?offset=580`.Replace the `offset` variable with your last offset and run the script again. Continue this until you have downloaded all the submissions.



