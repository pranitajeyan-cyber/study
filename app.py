import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
from pathlib import Path
import random
import time

# Page configuration
st.set_page_config(
    page_title="Mochi's Study Planner ✨",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load custom CSS
def load_css():
    css_file = Path(__file__).parent / "styles.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Initialize session state
def initialize_session_state():
    if "subjects" not in st.session_state:
        st.session_state.subjects = []
    if "completed_tasks" not in st.session_state:
        st.session_state.completed_tasks = 0
    if "total_tasks" not in st.session_state:
        st.session_state.total_tasks = 0
    if "study_streak" not in st.session_state:
        st.session_state.study_streak = 0
    if "achievements" not in st.session_state:
        st.session_state.achievements = []
    if "pomodoro_sessions" not in st.session_state:
        st.session_state.pomodoro_sessions = 0
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

initialize_session_state()

# Mochi Mascot Messages
mochi_messages = {
    "greeting": [
        "🐰 Hi! I'm Mochi, your study buddy! Let's make studying fun today!",
        "✨ Welcome back! Ready to crush your study goals?",
        "🌸 Great to see you! Let's turn study chaos into organized fun!",
    ],
    "encouragement": [
        "💪 You're doing amazing! Keep up the great work!",
        "🌟 One step closer to your goals! You've got this!",
        "🎉 That's the spirit! Mochi believes in you!",
    ],
    "break": [
        "☕ Time for a well-deserved break! Rest those eyes!",
        "🍪 You've earned a snack break! Recharge!",
        "😴 Don't forget to take care of yourself!",
    ],
    "deadline": [
        "⏰ Exam coming up! Let's focus on this subject!",
        "🔥 Crunch time! But you're ready for this!",
        "📚 Getting close! Let's boost those study hours!",
    ]
}

def get_mochi_message(message_type="greeting"):
    return random.choice(mochi_messages.get(message_type, mochi_messages["greeting"]))

# Progress growth visualization
def get_progress_stage(percentage):
    if percentage < 25:
        return "🌱 Seed", "#FFD6E7"
    elif percentage < 50:
        return "🌿 Sprout", "#D8FFE3"
    elif percentage < 75:
        return "🌸 Flower", "#FFE4CC"
    elif percentage < 100:
        return "🌳 Blooming Tree", "#E6D6FF"
    else:
        return "✨ Magical Tree", "#D6F0FF"

# Calculate priority score
def calculate_priority(difficulty, days_remaining):
    difficulty_weights = {"Easy": 1, "Medium": 2, "Hard": 3}
    weight = difficulty_weights.get(difficulty, 1)
    
    if days_remaining <= 0:
        return weight * 10
    return weight / days_remaining

# Get AI recommendation
def get_ai_recommendation(subjects):
    if not subjects:
        return get_mochi_message("greeting")
    
    # Find most urgent subject
    most_urgent = None
    highest_priority = 0
    
    for subject in subjects:
        exam_date = datetime.strptime(subject["exam_date"], "%Y-%m-%d")
        days_left = (exam_date - datetime.now()).days
        priority = calculate_priority(subject["difficulty"], days_left)
        
        if priority > highest_priority:
            highest_priority = priority
            most_urgent = subject
    
    if most_urgent and (datetime.strptime(most_urgent["exam_date"], "%Y-%m-%d") - datetime.now()).days <= 7:
        return f"🐰 **{most_urgent['name']}** exam is coming up! Let's focus on it today. You've got this! 💪"
    elif most_urgent:
        return f"📚 **{most_urgent['name']}** needs attention. Let's build a strong foundation! 🌱"
    else:
        return get_mochi_message("encouragement")

# Generate study schedule
def generate_study_schedule(subjects, total_hours=20):
    if not subjects:
        return None
    
    # Calculate priorities
    schedule = {}
    total_priority = 0
    
    subject_priorities = []
    for subject in subjects:
        exam_date = datetime.strptime(subject["exam_date"], "%Y-%m-%d")
        days_left = max(1, (exam_date - datetime.now()).days)
        priority = calculate_priority(subject["difficulty"], days_left)
        subject_priorities.append({
            "name": subject["name"],
            "priority": priority,
            "difficulty": subject["difficulty"]
        })
        total_priority += priority
    
    # Allocate study hours based on priority
    for item in subject_priorities:
        hours = (item["priority"] / total_priority) * total_hours
        schedule[item["name"]] = round(hours, 1)
    
    return schedule

# Create animated progress bar
def create_progress_visualization(completed, total):
    if total == 0:
        percentage = 0
    else:
        percentage = (completed / total) * 100
    
    stage, color = get_progress_stage(percentage)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        fig = go.Figure(data=[
            go.Bar(
                x=[percentage],
                orientation='h',
                marker=dict(color=color, line=dict(color='#FFD6E7', width=3)),
                text=f'{int(percentage)}%',
                textposition='auto',
                hovertemplate='%{text} Complete<extra></extra>',
                name='Progress'
            )
        ])
        
        fig.update_layout(
            xaxis=dict(range=[0, 100], showgrid=False, zeroline=False),
            yaxis=dict(visible=False),
            height=80,
            margin=dict(l=0, r=0, t=0, b=0),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            hovermode=False
        )
        
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    
    with col2:
        st.markdown(f"<div class='progress-stage'>{stage}</div>", unsafe_allow_html=True)

# Create subject cards
def create_subject_card(subject, index):
    col1, col2 = st.columns([5, 1])
    
    with col1:
        with st.container():
            st.markdown(f"""
                <div class='subject-card'>
                    <div class='card-header'>
                        <h3 style='margin: 0; color: #FFD6E7;'>📚 {subject['name']}</h3>
                    </div>
                    <div class='card-body'>
                        <div class='card-row'>
                            <span class='card-label'>🌟 Difficulty:</span>
                            <span class='card-value'>{subject['difficulty']}</span>
                        </div>
                        <div class='card-row'>
                            <span class='card-label'>📅 Exam Date:</span>
                            <span class='card-value'>{subject['exam_date']}</span>
                        </div>
                        <div class='card-row'>
                            <span class='card-label'>🔥 Priority:</span>
                            <span class='card-value'>{subject['priority']}</span>
                        </div>
                        <div class='card-row'>
                            <span class='card-label'>📖 Study Hours/Week:</span>
                            <span class='card-value'>{subject['study_hours']} hrs</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if st.button("✕", key=f"delete_{index}", help="Delete subject"):
            st.session_state.subjects.pop(index)
            st.rerun()

# Achievement badge system
def award_achievement(achievement_name, description):
    if achievement_name not in st.session_state.achievements:
        st.session_state.achievements.append(achievement_name)
        return True
    return False

# Check achievements
def check_achievements():
    if st.session_state.completed_tasks >= 1:
        award_achievement("Study Starter", "🌟 Complete your first task!")
    
    if st.session_state.completed_tasks >= 10:
        award_achievement("Bookworm", "📚 Complete 10 tasks!")
    
    if st.session_state.study_streak >= 7:
        award_achievement("7-Day Streak", "🔥 Study for 7 days straight!")
    
    if st.session_state.pomodoro_sessions >= 20:
        award_achievement("Focus Master", "💎 Complete 20 Pomodoro sessions!")
    
    if len(st.session_state.subjects) >= 5:
        award_achievement("Exam Warrior", "🏆 Manage 5+ subjects!")

# Pomodoro Timer
def pomodoro_timer():
    st.subheader("🍅 Pomodoro Timer")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("Start Study (25 min)", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            total_seconds = 25 * 60
            for i in range(total_seconds):
                progress = (i / total_seconds)
                progress_bar.progress(progress)
                
                minutes = (total_seconds - i) // 60
                seconds = (total_seconds - i) % 60
                status_text.markdown(f"<h3 style='text-align: center;'>⏱️ {minutes:02d}:{seconds:02d}</h3>", unsafe_allow_html=True)
                time.sleep(1)
            
            progress_bar.progress(1.0)
            st.session_state.pomodoro_sessions += 1
            st.success("🎉 Great work! Mochi is proud of you!")
            st.balloons()
    
    with col2:
        if st.button("Start Break (5 min)", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            total_seconds = 5 * 60
            for i in range(total_seconds):
                progress = (i / total_seconds)
                progress_bar.progress(progress)
                
                minutes = (total_seconds - i) // 60
                seconds = (total_seconds - i) % 60
                status_text.markdown(f"<h3 style='text-align: center;'>☕ {minutes:02d}:{seconds:02d}</h3>", unsafe_allow_html=True)
                time.sleep(1)
            
            progress_bar.progress(1.0)
            st.info("✨ Break time's over! Ready to get back to studying?")
    
    with col3:
        st.markdown("### 🎵 Study Music\n[Lo-fi Study Beats](https://www.youtube.com/watch?v=jfKfPfyJRdk)")

# Main landing page
def landing_page():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='landing-hero'>
                <h1 style='font-size: 3.5em; margin-bottom: 0.2em;'>🌸 Mochi's Study Planner</h1>
                <p style='font-size: 1.3em; color: #E6D6FF; margin-bottom: 2em;'>
                    Turn your study chaos into a cute and organized journey ✨
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
                <div class='feature-highlight'>
                    <h3>📚 Smart Scheduling</h3>
                    <p>AI-powered study plans tailored to your exams</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            st.markdown("""
                <div class='feature-highlight'>
                    <h3>🌱 Progress Tracking</h3>
                    <p>Watch your knowledge grow from seed to tree</p>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='mascot-container'>
                <div style='font-size: 6em; text-align: center;'>🐰</div>
                <p style='text-align: center; color: #FFD6E7; font-weight: bold;'>Mochi says:</p>
                <p style='text-align: center; color: #E6D6FF;'>
                    {}
                </p>
            </div>
        """.format(get_mochi_message("greeting")), unsafe_allow_html=True)

# Dashboard view
def dashboard_view():
    st.markdown("<h2 style='color: #FFD6E7;'>📊 Your Study Dashboard</h2>", unsafe_allow_html=True)
    
    # Top widgets
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class='dashboard-widget'>
                <div style='font-size: 2em;'>📈</div>
                <div class='widget-label'>Weekly Progress</div>
                <div class='widget-value'>{st.session_state.completed_tasks}/{st.session_state.total_tasks if st.session_state.total_tasks > 0 else 1}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class='dashboard-widget'>
                <div style='font-size: 2em;'>🔥</div>
                <div class='widget-label'>Study Streak</div>
                <div class='widget-value'>{st.session_state.study_streak} days</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class='dashboard-widget'>
                <div style='font-size: 2em;'>⭐</div>
                <div class='widget-label'>Productivity Score</div>
                <div class='widget-value'>{min(100, st.session_state.pomodoro_sessions * 5)}%</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class='dashboard-widget'>
                <div style='font-size: 2em;'>📚</div>
                <div class='widget-label'>Subjects</div>
                <div class='widget-value'>{len(st.session_state.subjects)}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Mochi's recommendation
    if st.session_state.subjects:
        st.markdown(f"""
            <div class='mochi-bubble'>
                <div style='font-size: 1.5em; margin-bottom: 0.5em;'>🐰</div>
                <p style='margin: 0;'>{get_ai_recommendation(st.session_state.subjects)}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Progress tracking
    if st.session_state.total_tasks > 0:
        st.subheader("🌱 Your Study Growth")
        create_progress_visualization(st.session_state.completed_tasks, st.session_state.total_tasks)
    
    # Subjects section
    if st.session_state.subjects:
        st.subheader("📚 Your Subjects")
        for i, subject in enumerate(st.session_state.subjects):
            create_subject_card(subject, i)
    else:
        st.info("🌸 No subjects yet! Add your first subject to get started.")
    
    st.markdown("---")
    
    # Achievements
    check_achievements()
    if st.session_state.achievements:
        st.subheader("🏆 Your Achievements")
        achievement_cols = st.columns(min(3, len(st.session_state.achievements)))
        for idx, achievement in enumerate(st.session_state.achievements):
            if idx < len(achievement_cols):
                with achievement_cols[idx]:
                    st.markdown(f"""
                        <div class='achievement-badge'>
                            {achievement}
                        </div>
                    """, unsafe_allow_html=True)

# Subject management
def subject_management():
    st.markdown("<h2 style='color: #FFD6E7;'>📚 Subject Management</h2>", unsafe_allow_html=True)
    
    with st.form("add_subject_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            subject_name = st.text_input("Subject Name", placeholder="e.g., Statistics")
        
        with col2:
            difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])
        
        with col3:
            exam_date = st.date_input("Exam Date")
        
        col4, col5 = st.columns(2)
        
        with col4:
            study_hours = st.slider("Study Hours/Week", 1, 20, 5)
        
        with col5:
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        
        submit_button = st.form_submit_button("➕ Add Subject", use_container_width=True)
        
        if submit_button:
            if subject_name:
                st.session_state.subjects.append({
                    "name": subject_name,
                    "difficulty": difficulty,
                    "exam_date": exam_date.strftime("%Y-%m-%d"),
                    "study_hours": study_hours,
                    "priority": priority
                })
                st.session_state.total_tasks += 1
                st.success(f"✨ {subject_name} added! Mochi is excited to help!")
                st.rerun()
            else:
                st.error("Please enter a subject name")
    
    st.markdown("---")
    
    # Generate schedule
    if st.session_state.subjects:
        st.subheader("🗓️ AI-Generated Study Schedule")
        
        schedule = generate_study_schedule(st.session_state.subjects, total_hours=20)
        
        if schedule:
            # Display as table
            schedule_df = pd.DataFrame([
                {"Subject": name, "Recommended Hours": hours}
                for name, hours in sorted(schedule.items(), key=lambda x: x[1], reverse=True)
            ])
            
            st.dataframe(schedule_df, use_container_width=True, hide_index=True)
            
            # Create visualization
            fig = px.bar(
                schedule_df,
                x="Subject",
                y="Recommended Hours",
                color="Recommended Hours",
                color_continuous_scale=["#FFD6E7", "#E6D6FF", "#D6F0FF"],
                title="📊 Recommended Study Hours Distribution",
                labels={"Recommended Hours": "Hours/Week"}
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color="#333"),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='rgba(200,200,200,0.2)'),
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Daily schedule breakdown
            st.subheader("📅 Daily Study Schedule")
            
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            
            for day in days:
                with st.expander(f"{day}"):
                    daily_schedule = []
                    total_daily = 0
                    
                    for subject_name, hours in schedule.items():
                        daily_hours = hours / 7
                        if daily_hours > 0:
                            daily_schedule.append(f"📚 {subject_name} → {daily_hours:.1f} hours")
                            total_daily += daily_hours
                    
                    for item in daily_schedule:
                        st.markdown(item)
                    
                    st.markdown(f"☕ **Break Time** → 0.5 hours")
                    st.markdown(f"**Total: {total_daily + 0.5:.1f} hours**")
            
            # Download options
            col1, col2, col3 = st.columns(3)
            
            with col1:
                csv = schedule_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download CSV",
                    data=csv,
                    file_name="study_schedule.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            with col2:
                st.markdown("*📄 PDF download coming soon!*")
            
            with col3:
                if st.button("📋 Copy Schedule", use_container_width=True):
                    st.success("Schedule copied! 📋")

# Study Session view
def study_session_view():
    st.markdown("<h2 style='color: #FFD6E7;'>⏱️ Study Session</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        pomodoro_timer()
    
    with col2:
        st.subheader("🎯 Quick Stats")
        st.metric("Today's Sessions", st.session_state.pomodoro_sessions)
        st.metric("Total Study Hours", st.session_state.pomodoro_sessions * 0.42)
    
    st.markdown("---")
    
    st.subheader("📋 Today's Focus")
    
    if st.session_state.subjects:
        schedule = generate_study_schedule(st.session_state.subjects)
        
        top_3 = sorted(schedule.items(), key=lambda x: x[1], reverse=True)[:3]
        
        for i, (subject, hours) in enumerate(top_3, 1):
            st.markdown(f"""
                <div class='focus-card'>
                    <h4>#{i} {subject}</h4>
                    <p style='margin: 0;'>Recommended: {hours:.1f} hours</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Add subjects to see today's focus recommendations!")

# Main app
def main():
    # Sidebar
    with st.sidebar:
        st.markdown("<div class='sidebar-title'>🐰 Mochi's Study Planner</div>", unsafe_allow_html=True)
        
        page = st.radio(
            "Navigation",
            ["🏠 Home", "📊 Dashboard", "📚 Subjects", "⏱️ Study Session"],
            use_container_width=True
        )
        
        st.markdown("---")
        
        # Dark mode toggle
        dark_mode = st.checkbox("🌙 Moonlight Mode", value=st.session_state.dark_mode)
        if dark_mode != st.session_state.dark_mode:
            st.session_state.dark_mode = dark_mode
            st.rerun()
        
        st.markdown("---")
        
        # Quick actions
        st.subheader("⚡ Quick Actions")
        
        if st.button("➕ Add Task", use_container_width=True):
            st.session_state.completed_tasks = min(st.session_state.completed_tasks + 1, st.session_state.total_tasks)
        
        if st.button("🔥 Update Streak", use_container_width=True):
            st.session_state.study_streak += 1
        
        st.markdown("---")
        
        st.markdown("""
            <div class='sidebar-footer'>
                <p style='font-size: 0.9em; color: #999;'>
                    Made with 💜 for students<br>
                    v1.0.0
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Main content
    if page == "🏠 Home":
        landing_page()
    elif page == "📊 Dashboard":
        dashboard_view()
    elif page == "📚 Subjects":
        subject_management()
    elif page == "⏱️ Study Session":
        study_session_view()

if __name__ == "__main__":
    main()
