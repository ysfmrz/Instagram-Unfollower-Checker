
# Instagram Unfollower Checker

A Python script to track Instagram followers and detect unfollowers using Selenium and Firefox.

## Features
- **Create Follower File (F)**: Saves the current list of followers to `followers.txt`.
- **Check Unfollowers (C)**: Compares current followers with the saved list to find unfollowers.

## Prerequisites
- **Firefox**: Must be installed and closed before running.
- **Python 3.x**: Install dependencies:
  ```bash
  pip install selenium

 Geckodriver: Download from here and add to PATH.
 Firefox Profile: Log in to Instagram manually in Firefox once to save your credentials.

Setup:
    Clone the Repository:
    
    bash

    git clone https://github.com/ysfmrz/Instagram-Unfollower-Checker.git
    cd Instagram-Unfollower-Checker

Usage:
    Before running the script, open Firefox, go to your Instagram profile, log in manually, and then close Firefox. This ensures the script uses your logged-in session.
    Run the script:
    
    bash

    python instagram_unfollower_checker.py

   Choose an option:
        F: Create a new follower list.
        C: Check for unfollowers.
    Firefox opens and loads Instagram:
        If it’s slow, press Ctrl+Shift+R to refresh.
        Click "Followers" and scroll manually to the last follower.
    Return to the console and press Enter:
        For F: Saves followers to followers.txt.
        For C: Shows unfollowers and asks if you want to update the file (y/n).

Tutorial Video
Watch the step-by-step guide: Insert Video Link Here (#) (Upload your video to YouTube and replace this link.)

Important Notes:
    Firefox must be closed before starting the script.
    Log in to Instagram manually in Firefox beforehand for smooth operation.
    Scroll to the last follower to capture all usernames.
    The script uses the profile path in path.txt to access your logged-in session.

License
MIT License - free to use and modify!

