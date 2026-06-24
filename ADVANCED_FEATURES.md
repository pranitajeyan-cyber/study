# 🚀 Advanced Features & Customization Guide

Customize Mochi's Study Planner to match your unique style and needs!

---

## 🎨 Customizing the Kawaii Aesthetic

### Change the Color Scheme

Edit `styles.css` and modify the CSS variables:

```css
:root {
    --sakura-pink: #FFD6E7;      /* Primary color */
    --lavender: #E6D6FF;          /* Secondary color */
    --baby-blue: #D6F0FF;         /* Accent 1 */
    --mint-green: #D8FFE3;        /* Accent 2 */
    --cream-white: #FFF9F3;       /* Background */
    --peach: #FFE4CC;             /* Accent 3 */
}
```

#### Pre-made Color Schemes

**🌙 Midnight Dream**
```css
--sakura-pink: #B19CD9;
--lavender: #9370DB;
--baby-blue: #7B68EE;
--mint-green: #9932CC;
--cream-white: #1A0033;
--peach: #8A2BE2;
```

**🌊 Ocean Vibes**
```css
--sakura-pink: #40E0D0;
--lavender: #3FADDC;
--baby-blue: #00CED1;
--mint-green: #48D1CC;
--cream-white: #E0F6F6;
--peach: #5F9EA0;
```

**🍓 Cherry Blossom**
```css
--sakura-pink: #FFB6C1;
--lavender: #DDA0DD;
--baby-blue: #FFE4E1;
--mint-green: #FFC0CB;
--cream-white: #FFF0F5;
--peach: #FFB347;
```

**🌻 Sunflower Dream**
```css
--sakura-pink: #FFD700;
--lavender: #FFDA03;
--baby-blue: #FFF44F;
--mint-green: #FFEE58;
--cream-white: #FFFACD;
--peach: #FFE135;
```

### Modify Font Styles

Add custom fonts in `app.py`:

```python
def load_css():
    css_file = Path(__file__).parent / "styles.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            custom_css = """
            @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');
            
            * {
                font-family: 'Quicksand', sans-serif !important;
            }
            """
            st.markdown(f"<style>{custom_css}{f.read()}</style>", unsafe_allow_html=True)
```

#### Popular Kawaii Fonts
- **Quicksand**: Rounded, modern aesthetic
- **Comfortaa**: Ultra-rounded, very cute
- **Poppins**: Clean and playful
- **Nunito**: Soft and friendly

---

## 🐰 Customize Mochi the Mascot

### Add Custom Mochi Messages

In `app.py`, expand the message system:

```python
mochi_messages = {
    "greeting": [
        "🐰 Hi! I'm Mochi, your study buddy! Let's make studying fun today!",
        "✨ Welcome back! Ready to crush your study goals?",
        "🌸 Great to see you! Let's turn study chaos into organized fun!",
        "💕 I'm so glad you're here! Today's the day we shine!",
        "🌟 You're back! Mochi missed you! Let's do this!",
    ],
    "encouragement": [
        "💪 You're doing amazing! Keep up the great work!",
        "🌟 One step closer to your goals! You've got this!",
        "🎉 That's the spirit! Mochi believes in you!",
        "💎 You're unstoppable! Keep going!",
        "🌸 Every step counts! You're making progress!",
    ],
    "exam_warning": [
        "⏰ Exam coming up! Let's focus on this subject!",
        "🔥 Crunch time! But you're ready for this!",
        "📚 Getting close! Let's boost those study hours!",
        "💪 Show that exam who's boss!",
        "🎯 Time to shine! You've prepared for this!",
    ],
    # Add more categories as needed
}
```

### Create Multiple Mascots

Add more mascot characters:

```python
def get_mascot_emoji(mascot_type="mochi"):
    mascots = {
        "mochi": "🐰",
        "cat": "😺",
        "bear": "🐻",
        "penguin": "🐧",
        "otter": "🦦",
        "fox": "🦊",
    }
    return mascots.get(mascot_type, "🐰")
```

---

## 📊 Advanced Study Planning Features

### Customize Difficulty Weights

Adjust how difficulty affects study recommendations:

```python
def calculate_priority(difficulty, days_remaining, custom_weights=None):
    default_weights = {"Easy": 1, "Medium": 2, "Hard": 3}
    difficulty_weights = custom_weights or default_weights
    
    weight = difficulty_weights.get(difficulty, 1)
    
    # Add exponential factor for urgency
    urgency_factor = 1 + (1 / max(days_remaining, 1)) ** 1.5
    
    if days_remaining <= 0:
        return weight * urgency_factor * 10
    return (weight / days_remaining) * urgency_factor
```

### Add Learning Styles

Include personalized study methods:

```python
learning_styles = {
    "visual": [
        "Create colorful mind maps",
        "Watch educational videos",
        "Use flashcards with images",
        "Draw diagrams and charts",
    ],
    "auditory": [
        "Read notes aloud",
        "Join study groups",
        "Listen to lectures",
        "Discuss topics with others",
    ],
    "kinesthetic": [
        "Practice problems",
        "Do hands-on experiments",
        "Create study models",
        "Teach others the material",
    ],
    "reading_writing": [
        "Take detailed notes",
        "Create outlines",
        "Write summaries",
        "Read textbooks thoroughly",
    ],
}
```

### Smart Study Duration Calculation

```python
def calculate_study_hours(subject_difficulty, exam_distance_days, proficiency=0.5):
    """
    Calculate optimal study hours based on multiple factors
    
    Args:
        subject_difficulty: 1-3 scale
        exam_distance_days: days until exam
        proficiency: 0-1 scale (0=beginner, 1=expert)
    """
    base_hours = subject_difficulty * 2
    urgency_multiplier = 10 / max(exam_distance_days, 1)
    proficiency_adjustment = 1 - (proficiency * 0.3)
    
    return base_hours * urgency_multiplier * proficiency_adjustment
```

---

## 🏆 Achievement System Extensions

### Add More Achievements

```python
achievements_database = {
    "study_starter": {
        "name": "🌟 Study Starter",
        "description": "Complete your first task",
        "icon": "🌟",
        "requirement": lambda: st.session_state.completed_tasks >= 1
    },
    "bookworm": {
        "name": "📚 Bookworm",
        "description": "Complete 10 tasks",
        "icon": "📚",
        "requirement": lambda: st.session_state.completed_tasks >= 10
    },
    "night_owl": {
        "name": "🌙 Night Owl",
        "description": "Study after 10 PM",
        "icon": "🌙",
        "requirement": lambda: check_study_time_night()
    },
    "speed_reader": {
        "name": "⚡ Speed Reader",
        "description": "Complete 3 sessions in one day",
        "icon": "⚡",
        "requirement": lambda: st.session_state.daily_sessions >= 3
    },
    "consistency_king": {
        "name": "👑 Consistency King",
        "description": "30-day study streak",
        "icon": "👑",
        "requirement": lambda: st.session_state.study_streak >= 30
    },
}
```

### Create Leaderboard System

```python
def create_leaderboard(achievements):
    achievement_points = {
        "study_starter": 10,
        "bookworm": 50,
        "night_owl": 30,
        "speed_reader": 75,
        "consistency_king": 200,
    }
    
    total_points = sum(
        achievement_points.get(ach, 0) 
        for ach in achievements
    )
    
    return total_points
```

---

## 📱 Adding New Features

### Track Study Breaks

```python
def track_break_quality(break_duration, activity):
    """
    Log quality breaks for better study recommendations
    """
    if "break_log" not in st.session_state:
        st.session_state.break_log = []
    
    st.session_state.break_log.append({
        "duration": break_duration,
        "activity": activity,
        "timestamp": datetime.now()
    })
```

### Study Notes Integration

```python
def save_study_notes(subject, notes):
    """
    Save quick notes during study sessions
    """
    if "study_notes" not in st.session_state:
        st.session_state.study_notes = {}
    
    if subject not in st.session_state.study_notes:
        st.session_state.study_notes[subject] = []
    
    st.session_state.study_notes[subject].append({
        "content": notes,
        "date": datetime.now(),
        "session_id": st.session_state.current_session_id
    })
```

### Distraction Tracker

```python
def log_distraction(distraction_type, duration_minutes):
    """
    Track what distracts you to improve future sessions
    """
    if "distractions" not in st.session_state:
        st.session_state.distractions = {}
    
    if distraction_type not in st.session_state.distractions:
        st.session_state.distractions[distraction_type] = 0
    
    st.session_state.distractions[distraction_type] += duration_minutes
```

---

## 🔐 Data Persistence

### Save to Local JSON

```python
import json

def save_data():
    """Save session data to JSON file"""
    data = {
        "subjects": st.session_state.subjects,
        "completed_tasks": st.session_state.completed_tasks,
        "study_streak": st.session_state.study_streak,
        "achievements": st.session_state.achievements,
    }
    
    with open("study_data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    """Load session data from JSON file"""
    try:
        with open("study_data.json", "r") as f:
            data = json.load(f)
            st.session_state.subjects = data.get("subjects", [])
            st.session_state.completed_tasks = data.get("completed_tasks", 0)
            st.session_state.study_streak = data.get("study_streak", 0)
            st.session_state.achievements = data.get("achievements", [])
    except FileNotFoundError:
        initialize_session_state()
```

### Cloud Sync (Firebase Example)

```python
# Install: pip install firebase-admin

import firebase_admin
from firebase_admin import credentials, db

def sync_to_firebase(user_id, data):
    """Sync study data to Firebase"""
    ref = db.reference(f"users/{user_id}")
    ref.set(data)

def fetch_from_firebase(user_id):
    """Fetch study data from Firebase"""
    ref = db.reference(f"users/{user_id}")
    return ref.get()
```

---

## 📈 Analytics & Insights

### Study Time Analytics

```python
def analyze_study_patterns():
    """Analyze when you study best"""
    if "study_sessions" not in st.session_state:
        return None
    
    sessions = st.session_state.study_sessions
    
    # Analysis by hour
    hours = [session["hour"] for session in sessions]
    most_productive_hour = max(set(hours), key=hours.count)
    
    # Analysis by day
    days = [session["day"] for session in sessions]
    most_productive_day = max(set(days), key=days.count)
    
    return {
        "best_hour": most_productive_hour,
        "best_day": most_productive_day,
        "total_hours": len(sessions) * 0.42
    }
```

### Progress Forecasting

```python
def forecast_exam_readiness(subject, exam_date):
    """Predict if you'll be ready for exam"""
    subject_data = next((s for s in st.session_state.subjects if s["name"] == subject), None)
    
    if not subject_data:
        return "Unknown"
    
    hours_studied = subject_data.get("hours_studied", 0)
    days_remaining = (datetime.strptime(exam_date, "%Y-%m-%d") - datetime.now()).days
    recommended_hours = days_remaining * 2
    
    readiness = (hours_studied / recommended_hours) * 100 if recommended_hours > 0 else 0
    
    if readiness >= 100:
        return "✅ Ready!"
    elif readiness >= 75:
        return "🟢 Good"
    elif readiness >= 50:
        return "🟡 Fair"
    else:
        return "🔴 Needs Work"
```

---

## 🎯 Integration Ideas

### Calendar Integration
```python
# Sync study schedule with Google Calendar
# Install: pip install google-calendar-simple-api
```

### Study Group Features
```python
# Enable collaborative studying
# Real-time study session sharing
# Group progress tracking
```

### Mobile App
```python
# Convert to React Native
# Native iOS/Android app
# Offline functionality
```

### Browser Extension
```python
# Quick Pomodoro timer
# Study blocker for distracting sites
# Quick note-taking
```

---

## 🔧 Performance Optimization

### Caching

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_priority(difficulty, days_remaining):
    """Cache priority calculations"""
    # ... calculation code ...
    return priority
```

### Lazy Loading

```python
def lazy_load_achievements():
    """Only load achievements when needed"""
    if "achievements_loaded" not in st.session_state:
        st.session_state.achievements = check_achievements()
        st.session_state.achievements_loaded = True
```

---

## 📚 Resources

- **Streamlit Documentation**: https://docs.streamlit.io
- **Plotly Charts**: https://plotly.com/python/
- **Pandas Tutorial**: https://pandas.pydata.org/docs/
- **CSS Animations**: https://developer.mozilla.org/en-US/docs/Web/CSS/animation

---

## 🎓 Have Fun Customizing!

Make Mochi's Study Planner truly yours. Add features, change colors, and make it the perfect study companion! 🐰✨

