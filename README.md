
# Instagram Follower Checker

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

Setup

    Create path.txt:
        Open Firefox, go to about:profiles, copy your profile path (e.g., C:\Users\YourName\AppData\Roaming\Mozilla\Firefox\Profiles\xxxx.default-release), and paste it into path.txt.
    Clone the Repository:
    bash

    git clone https://github.com/YOUR_USERNAME/Instagram-Follower-Checker.git
    cd Instagram-Follower-Checker

Usage

    Run the script:
    bash

    python instagram_follower_checker.py

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
Important Notes

    Firefox must be closed before starting the script.
    Log in to Instagram manually in Firefox beforehand for smooth operation.
    Scroll to the last follower to capture all usernames.
    The script uses the profile path in path.txt to access your logged-in session.

License
MIT License - free to use and modify!



### کد اصلی رو هم همین‌طور آپلود کن
همون کد اصلی که دادی (`instagram_follower_checker.py`) رو هم توی همون مخزن آپلود کن:
- فایل رو توی کامپیوترت ذخیره کن با اسم `instagram_follower_checker.py`.
- توی گیتهاب، دوباره "Add file" > "Upload files" رو بزن و این فایل رو هم آپلود کن.

حالا دو تا فایل توی مخزن داری: `instagram_follower_checker.py` و `README.md`. همه چیز آماده‌ست! اگه باز سوالی بود، بگو.
