# 🐰 Mochi's AI-Powered Kawaii Study Planner

<div align="center">

![Mochi's Study Planner](https://img.shields.io/badge/Mochi-Study%20Planner-FF87B2?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Turn your study chaos into a cute and organized journey** ✨🌸

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Usage](#-usage) • [Screenshots](#-screenshots)

</div>

---

## 🌟 Overview

Mochi's Study Planner is a premium, AI-powered study management application with a delightful Kawaii aesthetic. It combines productivity features with an adorable design that makes studying fun and rewarding.

Perfect for students who want to:
- 📚 Organize multiple subjects and exam schedules
- 📊 Generate AI-powered personalized study plans
- 🌱 Track progress with cute visual growth animations
- 🎯 Manage study sessions with the Pomodoro technique
- 🏆 Earn achievements and maintain streaks
- 🐰 Get encouraging tips from Mochi, your study buddy

---

## ✨ Features

### 🎨 Premium Kawaii Design
- **Pastel Color Palette**: Sakura pink, lavender, baby blue, mint green
- **Smooth Animations**: Floating cards, hover effects, progress growth
- **Responsive UI**: Works beautifully on desktop and mobile
- **Dark Mode**: Moonlight Mode for late-night study sessions

### 📚 Subject Management
- Add, view, and delete subjects easily
- Set difficulty levels (Easy, Medium, Hard)
- Track exam dates and prioritize studies
- Automatically calculate priority scores

### 🧠 AI Study Schedule Generator
- Generates personalized study plans based on:
  - Subject difficulty
  - Time until exam
  - Priority levels
- **Smart Allocation**: Automatically distributes study hours
- **Daily Breakdown**: View recommended hours for each day
- **Weekly Overview**: See the complete study schedule

### 🌱 Progress Tracking System
- Visual growth animation: Seed → Sprout → Plant → Flower → Magical Tree
- Real-time progress percentage
- Beautiful progress visualization with Plotly
- Study streak counter

### ⏱️ Pomodoro Timer
- 🍅 25-minute study sessions
- ☕ 5-minute break sessions
- 📊 Track total sessions completed
- 🎉 Confetti celebration when you complete sessions
- 🎵 Links to lofi study music

### 🏆 Achievement System
Unlock badges as you progress:
- **🌟 Study Starter**: Complete your first task
- **📚 Bookworm**: Complete 10 tasks
- **🔥 7-Day Streak**: Study for 7 consecutive days
- **💎 Focus Master**: Complete 20 Pomodoro sessions
- **🏆 Exam Warrior**: Manage 5+ subjects

### 🐰 Mochi Mascot System
- Dynamic messages based on your study status
- Encouragement and motivation
- Smart recommendations based on upcoming exams
- Emotional reactions to your progress

### 📊 Dashboard Widgets
- Weekly study progress
- Study streak counter
- Productivity score
- Subjects remaining
- Upcoming exams countdown

### 📥 Export Options
- Download study schedules as CSV
- PDF export (coming soon)
- Easy sharing capabilities

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project

```bash
git clone https://github.com/yourusername/mochiStudyPlanner.git
cd mochiStudyPlanner
```

Or simply download the files and extract them.

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Streamlit**: Web app framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive charts
- **NumPy**: Numerical computing

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 💡 Quick Start

### First Time Setup
1. **Launch the App**: Run `streamlit run app.py`
2. **Welcome Screen**: You'll see Mochi greeting you with a cute message
3. **Add Your First Subject**: Click "Subject Management" in the sidebar
4. **Fill in Details**:
   - Subject name (e.g., "Statistics")
   - Difficulty level
   - Exam date
   - Hours per week
   - Priority level
5. **View Your Schedule**: The app will generate a personalized study plan
6. **Start Studying**: Use the "Study Session" tab with the Pomodoro timer

---

## 📖 Usage Guide

### 🏠 Home Page
The landing page features:
- A warm welcome from Mochi
- Key features highlighting
- Quick navigation to main sections

### 📊 Dashboard
Your personal study hub:
- **Quick Stats**: Progress, streaks, productivity score
- **Mochi's Recommendation**: AI-powered study tips
- **Growth Visualization**: Watch your progress grow
- **Subject Cards**: All your subjects at a glance
- **Achievements**: Track your unlocked badges

### 📚 Subject Management
Organize your studies:
1. **Add Subject**: Enter subject name, difficulty, exam date
2. **View Schedule**: Get AI-generated study recommendations
3. **Daily Breakdown**: See what to study each day
4. **Download Plan**: Export your schedule as CSV

### ⏱️ Study Session
Focus mode with Pomodoro timer:
1. **Start Study**: Begin a 25-minute focused session
2. **Timer Display**: Watch the countdown with animations
3. **Take Break**: 5-minute rest sessions
4. **Track Sessions**: Monitor your total study hours
5. **Today's Focus**: See recommended subjects for the day

### 🌙 Dark Mode
Toggle "Moonlight Mode" in the sidebar for a cozy dark theme with:
- Soft purple backgrounds
- Glowing pastel accents
- Perfect for late-night studying

---

## 🎨 Design Highlights

### Color Palette
```
Sakura Pink:    #FFD6E7 (Primary)
Lavender:       #E6D6FF (Secondary)
Baby Blue:      #D6F0FF (Accent 1)
Mint Green:     #D8FFE3 (Accent 2)
Cream White:    #FFF9F3 (Background)
Peach:          #FFE4CC (Accent 3)
```

### Typography
- **Display**: Bold sans-serif for headers
- **Body**: Clear, readable sans-serif
- **Icons**: Emoji for personality

### Animations
- **Floating Cards**: Hover effects on all interactive elements
- **Progress Growth**: Animated plant growth visualization
- **Smooth Transitions**: All interactions feel polished
- **Confetti**: Celebration animations on achievements

---

## 📁 Project Structure

```
mochiStudyPlanner/
├── app.py                 # Main Streamlit application
├── styles.css            # Custom CSS for Kawaii aesthetic
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── assets/              # (Optional) Images and resources
    └── mochi.svg        # Mascot SVG
```

---

## 🔧 Customization

### Change Colors
Edit the CSS variables in `styles.css`:
```css
:root {
    --sakura-pink: #FFD6E7;  /* Modify any color here */
    --lavender: #E6D6FF;
    /* ... other colors ... */
}
```

### Add Custom Messages
Modify Mochi's messages in `app.py`:
```python
mochi_messages = {
    "greeting": ["Your custom message here"],
    # ... more messages ...
}
```

### Adjust Study Hours
Change the total recommended hours in the schedule generator:
```python
schedule = generate_study_schedule(st.session_state.subjects, total_hours=25)
```

---

## 🚀 Deployment

### Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select this app and deploy!

### Deploy to Heroku
```bash
# Create Procfile
echo "web: sh setup.sh && streamlit run app.py" > Procfile

# Create setup.sh
echo "mkdir -p ~/.streamlit/" > setup.sh
echo "echo '[server]' > ~/.streamlit/config.toml" >> setup.sh
echo "echo 'headless = true' >> ~/.streamlit/config.toml" >> setup.sh

# Deploy
git push heroku main
```

---

## 📊 Features Roadmap

- [ ] User authentication & cloud sync
- [ ] PDF study plan export
- [ ] Custom theme builder
- [ ] Progress analytics dashboard
- [ ] Group study features
- [ ] Mobile app version
- [ ] Integration with calendar apps
- [ ] AI-powered smart recommendations
- [ ] Study habit tracking
- [ ] Social sharing features

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Inspired by Duolingo, Notion, and Sanrio's cute aesthetic
- Built with ❤️ for students everywhere
- Special thanks to Streamlit for the amazing framework

---

## 📞 Support

### Common Issues

**Q: The app looks different on my screen**
A: Make sure you're using the latest version of Streamlit. Run `pip install --upgrade streamlit`

**Q: Colors aren't loading correctly**
A: Clear your browser cache or try an incognito window

**Q: Pomodoro timer doesn't work**
A: Ensure JavaScript is enabled in your browser

---

## 🎉 Have Fun Studying!

Remember, studying doesn't have to be boring. With Mochi by your side and a cute planner to organize your goals, you've got this! 

**Happy studying! 🐰✨**

---

<div align="center">

Made with 💜 by your study buddy Mochi

*"Great job! You're getting closer to your goal!"* 🌸

</div>
