# 📁 Project Structure & File Organization

Complete guide to the Mochi Study Planner project structure and file organization.

---

## 📂 Directory Tree

```
mochiStudyPlanner/
│
├── 📄 README.md                    # Main documentation
├── 📄 SETUP_GUIDE.md              # Quick setup instructions
├── 📄 ADVANCED_FEATURES.md        # Customization guide
├── 📄 PROJECT_STRUCTURE.md        # This file
├── 📄 requirements.txt            # Python dependencies
│
├── 🐍 app.py                      # Main Streamlit application
├── 🎨 styles.css                  # Custom Kawaii CSS styles
│
├── 📁 assets/                     # (Optional) Static assets
│   ├── 🎨 mochi.svg              # Mascot SVG
│   ├── 📸 screenshots/           # Screenshots for docs
│   └── 🎵 sounds/                # Optional sound effects
│
├── 📁 data/                       # (Optional) Data storage
│   ├── 📊 study_data.json        # Saved study sessions
│   ├── 📋 subjects.json          # Saved subjects
│   └── 🏆 achievements.json      # Achievement records
│
├── 📁 config/                     # Configuration files
│   ├── ⚙️ config.yaml            # App configuration
│   └── 🎨 themes.json            # Color schemes
│
├── 📁 utils/                      # Helper functions
│   ├── 🔢 calculations.py        # Math utilities
│   ├── 🎯 ai_recommendations.py  # AI logic
│   └── 📊 analytics.py           # Analytics functions
│
├── 📁 tests/                      # Test files
│   ├── ✅ test_calculations.py   # Unit tests
│   ├── ✅ test_achievements.py   # Achievement tests
│   └── ✅ test_integration.py    # Integration tests
│
├── 📁 docs/                       # Extended documentation
│   ├── 📖 user_guide.md          # User manual
│   ├── 🎨 design_guide.md        # Design specifications
│   ├── 🔌 api_documentation.md   # API reference
│   └── 🚀 deployment_guide.md    # Deployment instructions
│
└── .gitignore                     # Git ignore rules
```

---

## 📄 File Descriptions

### Core Files

#### **app.py** (Main Application)
- **Purpose**: Main Streamlit application
- **Size**: ~800 lines
- **Contains**:
  - Page configuration
  - Session state management
  - UI components
  - Navigation logic
  - All core functionality
- **Key Functions**:
  - `landing_page()`: Welcome screen
  - `dashboard_view()`: Main dashboard
  - `subject_management()`: Subject CRUD
  - `study_session_view()`: Pomodoro timer
  - `pomodoro_timer()`: Timer logic
  - `generate_study_schedule()`: AI schedule generation
  - `create_progress_visualization()`: Progress display

#### **styles.css** (Styling)
- **Purpose**: All visual styling and animations
- **Size**: ~600 lines
- **Contains**:
  - CSS variables (color palette)
  - Component styles
  - Animations and transitions
  - Responsive design rules
  - Dark mode styles
  - Custom scrollbar styling
- **Key Sections**:
  - Root variables
  - Base element styles
  - Component classes
  - Animation definitions
  - Media queries

#### **requirements.txt** (Dependencies)
- **Purpose**: List of Python packages to install
- **Packages**:
  - `streamlit==1.28.1` - Web framework
  - `pandas==2.1.3` - Data manipulation
  - `plotly==5.18.0` - Interactive charts
  - `numpy==1.26.2` - Numerical computing
  - `python-dateutil==2.8.2` - Date utilities
  - `pytz==2023.3` - Timezone handling

---

### Documentation Files

#### **README.md**
- Complete project overview
- Feature list
- Installation instructions
- Usage guide
- Customization guide
- Deployment options
- Roadmap
- 7,000+ words

#### **SETUP_GUIDE.md**
- Quick start commands
- System requirements
- Troubleshooting
- Common issues & solutions
- Tips and tricks
- Cloud deployment instructions

#### **ADVANCED_FEATURES.md**
- Custom color schemes (4 pre-made themes)
- Font customization
- Mascot customization
- Achievement system extensions
- Analytics & insights
- Data persistence options
- Performance optimization

#### **PROJECT_STRUCTURE.md** (This File)
- Directory organization
- File descriptions
- Content mapping
- Development workflow

---

## 🔄 Development Workflow

### Setting Up Development Environment

```bash
# 1. Clone/Download project
git clone [repository-url]
cd mochiStudyPlanner

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run application
streamlit run app.py
```

### Making Changes

1. **Styling Changes**
   - Edit `styles.css`
   - Browser will auto-reload
   - No Python restart needed

2. **Feature Changes**
   - Edit `app.py`
   - Save file
   - Streamlit will rerun app
   - No server restart needed

3. **Dependencies**
   - Add to `requirements.txt`
   - Run `pip install -r requirements.txt`
   - Import in your code

### Testing Changes

```bash
# Run tests (if available)
pytest tests/

# Check for errors
python -m py_compile app.py

# Format code
black app.py
```

---

## 📊 Code Statistics

### File Breakdown

| File | Lines | Type | Purpose |
|------|-------|------|---------|
| app.py | ~850 | Python | Main application |
| styles.css | ~550 | CSS | Visual styling |
| README.md | ~400 | Markdown | Main docs |
| SETUP_GUIDE.md | ~300 | Markdown | Setup instructions |
| ADVANCED_FEATURES.md | ~400 | Markdown | Advanced guide |
| requirements.txt | ~6 | Text | Dependencies |
| **Total** | **~2,500** | Mixed | Complete project |

---

## 🔌 Component Architecture

```
Streamlit App (app.py)
│
├── Session State
│   ├── subjects[]
│   ├── completed_tasks
│   ├── study_streak
│   ├── achievements[]
│   ├── pomodoro_sessions
│   └── dark_mode
│
├── Data Processing
│   ├── calculate_priority()
│   ├── generate_study_schedule()
│   ├── get_progress_stage()
│   └── check_achievements()
│
├── UI Components
│   ├── landing_page()
│   ├── dashboard_view()
│   ├── subject_management()
│   ├── study_session_view()
│   └── pomodoro_timer()
│
├── Styling (styles.css)
│   ├── CSS Variables
│   ├── Component Classes
│   ├── Animations
│   └── Responsive Design
│
└── Mascot System
    ├── get_mochi_message()
    ├── get_ai_recommendation()
    └── Emotional Reactions
```

---

## 🎨 Design System

### Color Palette
```css
--sakura-pink:   #FFD6E7  (Primary)
--lavender:      #E6D6FF  (Secondary)
--baby-blue:     #D6F0FF  (Accent 1)
--mint-green:    #D8FFE3  (Accent 2)
--cream-white:   #FFF9F3  (Background)
--peach:         #FFE4CC  (Accent 3)
```

### Typography
- **Headers (h1, h2, h3)**: Bold, playful
- **Body Text**: Clear, readable
- **Code**: Monospace
- **Emojis**: For personality and navigation

### Components
- **Dashboard Widgets**: Cards with hover effects
- **Subject Cards**: Full-featured study cards
- **Badges**: Achievements and status
- **Buttons**: Colorful, interactive
- **Forms**: Styled inputs and selects
- **Charts**: Plotly-based visualizations

---

## 🚀 Deployment Structure

### Streamlit Cloud
```
GitHub Repository
    └── mochiStudyPlanner/
        ├── app.py
        ├── styles.css
        ├── requirements.txt
        ├── README.md
        └── .streamlit/
            └── config.toml (optional)
```

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

### Heroku
```
Procfile:
web: sh setup.sh && streamlit run app.py

setup.sh:
mkdir -p ~/.streamlit/
echo "[server]" > ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
```

---

## 📈 Scaling Considerations

### Small Scale (Personal Use)
- Single file: `app.py`
- In-memory session state
- Local CSS file

### Medium Scale (Multiple Users)
- Separate utilities folder
- Database integration (optional)
- CDN for assets
- Error logging

### Large Scale (Production)
- Microservices architecture
- Database backend
- User authentication
- Cloud storage
- Analytics platform
- API layer

---

## 🔐 Security Considerations

### Current Implementation
- No authentication required
- All data in session memory
- No external API calls
- No database access

### For Production
- Add user authentication
- Implement data encryption
- Add rate limiting
- Use environment variables
- Validate all inputs
- Add CSRF protection
- Implement logging

---

## 📝 Future Expansion Areas

### Feature Modules to Add
```
utils/
├── authentication.py      # User login/signup
├── database.py           # Database operations
├── notifications.py      # Push notifications
├── analytics.py          # Usage analytics
├── export.py             # PDF/Excel export
├── cloud_sync.py         # Cloud storage
└── ai_assistant.py       # Advanced AI features
```

### New Components
```
components/
├── calendar_widget.py     # Calendar integration
├── timer_advanced.py      # Enhanced timer
├── study_tracker.py       # Detailed tracking
├── social_features.py     # Group study
└── gamification.py        # Game mechanics
```

---

## 🎯 Navigation Map

### User Flow
```
Landing Page (Home)
    ↓
Add Subjects
    ↓
View Dashboard
    ↓
Generate Schedule
    ↓
Study Sessions (Pomodoro)
    ↓
Track Progress
    ↓
Earn Achievements
```

### Feature Access
```
Sidebar Navigation
├── Home
├── Dashboard
├── Subject Management
└── Study Session

Quick Actions
├── Add Task
├── Update Streak
└── Settings
```

---

## 💾 Data Storage Structure

### Session State
```python
st.session_state = {
    "subjects": [
        {
            "name": "Statistics",
            "difficulty": "Hard",
            "exam_date": "2024-02-15",
            "study_hours": 5,
            "priority": "High"
        }
    ],
    "completed_tasks": 42,
    "total_tasks": 100,
    "study_streak": 15,
    "achievements": ["study_starter", "bookworm"],
    "pomodoro_sessions": 87,
    "dark_mode": False
}
```

### Optional JSON Storage
```json
{
    "subjects": [...],
    "completed_tasks": 42,
    "study_streak": 15,
    "achievements": [...],
    "last_updated": "2024-01-20T15:30:00Z"
}
```

---

## 🔗 External Dependencies

### Production Dependencies
- **Streamlit**: Web framework
- **Pandas**: Data manipulation
- **Plotly**: Visualizations
- **NumPy**: Numerical operations
- **python-dateutil**: Date utilities
- **pytz**: Timezone support

### Optional Extensions
- **firebase-admin**: Cloud database
- **stripe**: Payment processing
- **sendgrid**: Email service
- **pusher**: Real-time features
- **pytest**: Testing framework

---

## ✅ Quality Checklist

- [x] Clean code structure
- [x] Comprehensive documentation
- [x] Error handling
- [x] Responsive design
- [x] Accessibility considerations
- [x] Performance optimization
- [x] User-friendly interface
- [x] Customization options
- [x] Deployment ready
- [ ] User authentication
- [ ] Database backend
- [ ] Advanced analytics
- [ ] Mobile app version
- [ ] API endpoints

---

<div align="center">

**Everything you need to understand and extend Mochi's Study Planner!**

📚 Read the documentation  
🚀 Follow the setup guide  
🎨 Customize the design  
🔧 Extend the features  

Made with 💜 for students

</div>
