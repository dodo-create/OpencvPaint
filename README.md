🖐️ HandPaint — Paint with Just Your Hands (Like a Tech Wizard)
=============================================================

“I’m not saying I’m Iron Man… but I *did* build a screenless GUI using OpenCV and questionable sleep habits.”
— Not Tony Stark, but definitely the vibe

🎨 What is This?
----------------
*HandPaint* is a Python-based paint application that lets you draw, erase, and change colors using just your fingers in front of a webcam. 
No mouse. No touchscreen. No problem.

Just OpenCV, MediaPipe, and a little bit of digital chaos.

🧠 Why Did I Build This?
------------------------
I could’ve made a calculator. I could’ve made a to-do list. 
But no. I woke up and chose ✨gesture-controlled creative expression✨.

Also, I wanted to explore OpenCV… and this sounded cooler than blinking at my screen.

✋ How It Works
--------------
Using your webcam and the power of MediaPipe’s hand tracking, this app detects how many fingers you're holding up and performs actions based on that.

Finger Combo     | Action
-----------------|------------------------------
1 Finger         | Move the on-screen cursor
2 Fingers        | Draw on the canvas
3 Fingers        | Switch to the next color
5 Fingers        | Erase (whiteout style)
C key            | Clear the whole canvas
Q key            | Quit the program

You can also see a small video of yourself in the top-right corner — because watching yourself wave your hands like a magician is part of the experience.

🧰 Tech Stack
-------------
- Python
- OpenCV
- MediaPipe
- Just enough math to make lines draw properly



🚀 Features
-----------
- Paint with your index finger
- Switch between 5 colors (including purple, obviously)
- Erase with 5 fingers
- Picture-in-picture webcam view for feedback
- On-screen instructions so you don't forget what finger does what

🛠️ What I Want to Add Next
---------------------------
- Autoshape Detection: So your potato-looking circle becomes an actual circle.
- Gesture to Save Artwork: Because masterpieces deserve to be remembered.
- AI voice that roasts your art: (Might name it RoastJarvis)

📁 How to Run
-------------
1. Clone this repository:
   git clone https://github.com/yourusername/handpaint.git
   cd handpaint

2. Install the required packages:
   pip install opencv-python mediapipe numpy

3. Run the script:
   python handpaint.py

Then just wave your hand around like you’re summoning a spell. 🎨✨

💻 Made With
------------
❤ by Dhvani Gohel
Wit, caffeine, and an unexplainable obsession with Iron Man interfaces.

📽️ Watch It In Action
----------------------


⚠️ Disclaimer
-------------
This is a fun student project.
It won’t replace Photoshop, but it might make you feel like a tech wizard for a few minutes.

Use responsibly. And don’t try to finger-paint on your actual screen. Trust me.



“Part paint app, part sci-fi UI experiment. All chaos.”
