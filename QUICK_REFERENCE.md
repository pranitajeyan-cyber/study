# 🚀 Quick Reference Card

Everything you need to know about Mochi's Study Planner at a glance!

---

## ⚡ 5-Minute Quick Start

### Installation
```bash
# 1. Navigate to folder
cd mochiStudyPlanner

# 2. Create virtual environment
python -m venv venv

# 3. Activate (Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate)

# 4. Install packages
pip install -r requirements.txt

# 5. Run app
streamlit run app.py
```

### First Use
1. **Add subjects** → Subject Management tab
2. **View schedule** → Generated automatically
3. **Start studying** → Use Pomodoro timer
4. **Earn achievements** → Complete tasks!

---

## 📚 File Reference

| File | Purpose | Edit For |
|------|---------|----------|
| `app.py` | Main application | Features, logic, messages |
| `styles.css` | Visual design | Colors, fonts, layout |
| `requirements.txt` | Dependencies | Adding new packages |
| `README.md` | Full docs | Understanding everything |
| `SETUP_GUIDE.md` | Setup help | Installation issues |
| `ADVANCED_FEATURES.md` | Customization | Color schemes, new features |
| `PROJECT_STRUCTURE.md` | Architecture | Code organization |

---

## 🎨 Colors Cheat Sheet

```css
Primary:     #FFD6E7  (Sakura Pink)
Secondary:   #E6D6FF  (Lavender)
Accent 1:    #D6F0FF  (Baby Blue)
Accent 2:    #D8FFE3  (Mint Green)
Background:  #FFF9F3  (Cream White)
Accent 3:    #FFE4CC  (Peach)
```

**Change Colors**: Edit `:root { }` in `styles.css`

---

## 🐰 Mochi Commands Quick Guide

### Key Functions
```python
# Get mascot message
get_mochi_message(message_type)  # Options: greeting, encouragement, break, deadline

# Calculate study priority
calculate_priority(difficulty, days_remaining)

# Generate study schedule
generate_study_schedule(subjects, total_hours=20)

# Get progress stage
get_progress_stage(percentage)  # Returns emoji + color

# Check for achievements
check_achievements()

# Award achievement
award_achievement(name, description)
```

---

## 🎯 Feature Access Map

```
🏠 Home Page
├── View features overview
├── Meet Mochi
└── Start button

📊 Dashboard
├── Quick stats (4 widgets)
├── Mochi's recommendation
├── Progress visualization
├── Subject cards
└── Achievement badges

📚 Subject Management
├── Add new subject
├── View all subjects
├── AI Study Schedule
├── Daily breakdown
└── Download options

⏱️ Study Session
├── Pomodoro timer (25 min)
├── Break timer (5 min)
├── Music link
├── Session stats
└── Today's focus
```

---

## 💾 Data Locations

```
Session Memory (Disappears on refresh)
└── st.session_state

Optional Local Storage (if implemented)
└── study_data.json

Optional Cloud Storage (if enabled)
└── Firebase / Database
```

---

## 🔧 Common Customizations

### Change Primary Color
```css
/* In styles.css */
--sakura-pink: #FFD6E7;  /* Change this hex code */
```

### Change Mochi's Greeting
```python
# In app.py, modify mochi_messages dictionary
mochi_messages = {
    "greeting": [
        "Your custom message here! 🐰",
    ]
}
```

### Change Study Hours
```python
# In app.py, modify this line:
schedule = generate_study_schedule(st.session_state.subjects, total_hours=25)
```

### Change Timer Duration
```python
# In app.py, pomodoro_timer() function:
total_seconds = 25 * 60  # Change 25 to your preferred minutes
```

---

## ❌ Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Port 8501 in use | `streamlit run app.py --server.port 8502` |
| CSS not loading | Ctrl+Shift+Delete, clear cache, refresh |
| Module not found | `pip install -r requirements.txt` |
| App not starting | Check Python version: `python --version` |
| Virtual env not activating | Check path, or create new one |

---

## 📱 Access from Phone/Tablet

1. Find your computer's IP:
   - Windows: `ipconfig` → IPv4 Address
   - Mac/Linux: `ifconfig` → inet

2. Run with: `streamlit run app.py --server.address=0.0.0.0`

3. On phone: `http://YOUR_IP:8501`

---

## 🎓 Study Tips Built-In

### Difficulty Weights
```
Easy:   1x multiplier
Medium: 2x multiplier
Hard:   3x multiplier
```

### Priority Calculation
```
Priority = Difficulty Weight / Days Remaining
(Higher = More urgent)
```

### Progress Stages
```
0%   → 🌱 Seed
25%  → 🌿 Sprout
50%  → 🌸 Plant
75%  → 🌳 Flower
100% → ✨ Magical Tree
```

### Pomodoro Math
```
1 Session = 25 min study + 5 min break = 30 min
= 0.42 hours per session
```

---

## 🏆 Achievement Progress

| Achievement | Requirement | Reward |
|-------------|-------------|--------|
| Study Starter | 1 task | 🌟 |
| Bookworm | 10 tasks | 📚 |
| 7-Day Streak | 7 days | 🔥 |
| Focus Master | 20 sessions | 💎 |
| Exam Warrior | 5 subjects | 🏆 |

---

## 📊 Key Metrics

### Calculate Your Score
```
Productivity Score = Pomodoro Sessions × 5%
(20 sessions = 100% score)

Study Hours = Sessions × 0.42
(10 sessions ≈ 4.2 hours)

Exam Readiness = Hours Studied / Recommended Hours
```

---

## 🚀 Deployment Options

| Platform | Ease | Cost | Command |
|----------|------|------|---------|
| Streamlit Cloud | ⭐⭐⭐⭐⭐ | Free | Connect GitHub |
| Heroku | ⭐⭐⭐⭐ | Free-10$/mo | `git push heroku` |
| Docker | ⭐⭐⭐ | Varies | `docker build .` |
| Local Server | ⭐⭐ | Free | `streamlit run app.py` |

---

## 🎨 Preset Color Schemes

### Midnight Dream (Dark)
```css
Primary:  #B19CD9
Accent:   #9370DB
```

### Ocean Vibes (Cool)
```css
Primary:  #40E0D0
Accent:   #3FADDC
```

### Sunflower Dream (Warm)
```css
Primary:  #FFD700
Accent:   #FFF44F
```

---

## 📖 Documentation Map

```
README.md                  ← Start here!
├─ Features overview
├─ Installation
└─ Full guide

SETUP_GUIDE.md            ← Quick setup
├─ Commands
├─ Troubleshooting
└─ Tips

ADVANCED_FEATURES.md      ← Customize
├─ Colors
├─ New features
└─ Extensions

PROJECT_STRUCTURE.md      ← Understand code
├─ File structure
├─ Architecture
└─ Components
```

---

## ⚙️ Configuration Constants

```python
# In app.py, easy to modify:

# Timer durations
STUDY_DURATION = 25  # minutes
BREAK_DURATION = 5   # minutes

# Study hours
TOTAL_WEEKLY_HOURS = 20  # recommended

# Difficulty weights
DIFFICULTY_WEIGHTS = {
    "Easy": 1,
    "Medium": 2,
    "Hard": 3
}

# Progress stages
PROGRESS_STAGES = [
    (0, "🌱 Seed"),
    (25, "🌿 Sprout"),
    (50, "🌸 Plant"),
    (75, "🌳 Flower"),
    (100, "✨ Magical Tree")
]
```

---

## 🔗 Useful Links

- **Streamlit Docs**: https://docs.streamlit.io
- **Plotly Charts**: https://plotly.com/python/
- **Pandas Guide**: https://pandas.pydata.org/docs/
- **CSS Reference**: https://developer.mozilla.org/en-US/docs/Web/CSS
- **Python Docs**: https://docs.python.org/3/

---

## 💡 Pro Tips

- 🌙 Use Dark Mode for late-night study sessions
- 📱 Access from phone for on-the-go planning
- 📥 Download CSV schedule to share with friends
- 🎵 Study with lofi music (link in app)
- 🔥 Build your study streak for motivation
- 💎 Unlock all achievements for mastery
- 📊 Check dashboard daily for recommendations
- 🐰 Listen to Mochi's tips!

---

## 🎯 Next Steps

1. **Install** (5 minutes)
   - Run commands in SETUP_GUIDE.md

2. **Explore** (5 minutes)
   - Click around, add a subject

3. **Customize** (10 minutes)
   - Change colors in styles.css

4. **Study** (25 minutes)
   - Use Pomodoro timer!

5. **Share** (Optional)
   - Deploy to cloud
   - Share with friends

---

## 📞 Getting Help

**Question?** Check:
1. `README.md` - Main documentation
2. `SETUP_GUIDE.md` - Setup issues
3. `ADVANCED_FEATURES.md` - Customization
4. `PROJECT_STRUCTURE.md` - Code understanding

**Still stuck?** Common fixes:
- Refresh browser (Ctrl+F5)
- Restart app (Ctrl+C, then run again)
- Check Python version (3.8+)
- Reinstall packages (pip install -r requirements.txt)

---

<div align="center">

## 🎉 You're Ready to Go!

Everything is set up. Now just run:

```bash
streamlit run app.py
```

Let Mochi help you ace those exams! 🐰✨

**Made with 💜 for students**

</div>
