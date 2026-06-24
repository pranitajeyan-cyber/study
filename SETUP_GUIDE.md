# 🚀 Quick Setup Guide - Mochi's Study Planner

Get your cute study planner up and running in 5 minutes! 🐰✨

---

## 📋 Requirements Checklist

- [ ] Python 3.8 or higher installed
- [ ] pip or conda package manager
- [ ] A modern web browser
- [ ] About 100MB free disk space

---

## ⚡ Quick Start (Copy-Paste Commands)

### For Windows Users 🪟

```bash
# 1. Open Command Prompt and navigate to the project folder
cd path\to\mochiStudyPlanner

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

### For macOS/Linux Users 🍎🐧

```bash
# 1. Open Terminal and navigate to the project folder
cd path/to/mochiStudyPlanner

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

---

## 🎯 What Happens Next

When you run `streamlit run app.py`:
1. Streamlit will start a local server
2. Your default browser will open to `http://localhost:8501`
3. You'll see the Mochi Study Planner home page
4. Start by clicking "Subject Management" to add your first subject

---

## ✅ Verify Installation

### Test Python Version
```bash
python --version
# Should be 3.8 or higher
```

### Test Dependencies
```bash
python -c "import streamlit; import pandas; import plotly; print('✅ All dependencies installed!')"
```

---

## 🎨 First Time User Tips

1. **Add Your Subjects First**
   - Go to "📚 Subject Management"
   - Add all your subjects with exam dates
   - The AI will automatically generate your study schedule

2. **View Your Dashboard**
   - Check "📊 Dashboard" for personalized recommendations
   - See your growth visualization

3. **Start a Study Session**
   - Go to "⏱️ Study Session"
   - Use the Pomodoro timer (25 min focus, 5 min break)
   - Watch your achievements unlock!

4. **Enable Dark Mode**
   - Toggle "🌙 Moonlight Mode" in the sidebar for late-night studying

---

## 🔧 Troubleshooting

### ❌ "streamlit: command not found"
**Solution**: You haven't activated the virtual environment
```bash
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### ❌ "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Dependencies aren't installed
```bash
pip install -r requirements.txt
```

### ❌ "Port 8501 is already in use"
**Solution**: Use a different port
```bash
streamlit run app.py --server.port 8502
```

### ❌ Page looks broken or CSS isn't loading
**Solution**: Clear browser cache
1. Press `Ctrl+Shift+Delete` (or `Cmd+Shift+Delete` on Mac)
2. Clear "Cached images and files"
3. Refresh the page

### ❌ Pomodoro timer not working
**Solution**: Make sure JavaScript is enabled in your browser

---

## 📱 Access from Other Devices

Want to access the app from your phone or another computer?

1. Find your computer's IP address:
   - **Windows**: Open Command Prompt, type `ipconfig`, look for IPv4 Address
   - **Mac/Linux**: Open Terminal, type `ifconfig`, look for inet address

2. Run Streamlit with this option:
   ```bash
   streamlit run app.py --server.address=0.0.0.0
   ```

3. On another device, visit:
   ```
   http://YOUR_IP_ADDRESS:8501
   ```

---

## 🌍 Deploy to Cloud (Optional)

### Deploy to Streamlit Cloud (Easiest)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and app.py
5. Click "Deploy"

### Deploy to Heroku
```bash
# Install Heroku CLI
# Then run:
heroku create your-app-name
git push heroku main
```

---

## 📚 Project Structure Explained

```
mochiStudyPlanner/
├── app.py              ← Main application (everything runs here)
├── styles.css          ← Beautiful Kawaii design styles
├── requirements.txt    ← List of Python packages needed
├── README.md           ← Full documentation
└── SETUP_GUIDE.md      ← This file!
```

---

## 🎯 Keyboard Shortcuts

Once the app is running:
- `Ctrl + C`: Stop the app
- `R`: Rerun the app
- `C`: Clear console
- `V`: Toggle verbose output

---

## 🆘 Getting Help

### Common Questions

**Q: Can I customize the colors?**
A: Yes! Edit `styles.css` and change the color values

**Q: Can I add more subjects?**
A: Unlimited! Add as many as you need

**Q: Is my data saved?**
A: Data is saved in your browser session. Refresh the page to reset (we'll add cloud sync soon!)

**Q: Can I export my schedule?**
A: Yes! Download as CSV from the Subjects page

---

## 🎓 Next Steps

After setup:
1. Add your subjects and exam dates
2. Review the AI-generated study schedule
3. Use the Pomodoro timer for focused studying
4. Check your dashboard for recommendations
5. Earn achievements and build study streaks!

---

## 💡 Pro Tips

✨ **Best Study Practices**
- Study the most difficult subjects first
- Take breaks every 25 minutes (use Pomodoro timer)
- Review subjects with the closest exam dates
- Keep your study streak going!

🌙 **For Night Owls**
- Enable Dark Mode for less eye strain
- Study your hardest subjects during peak focus time
- Use the lofi music link during study sessions

📱 **Mobile Friendly**
- The app works on mobile! Access from your phone
- It automatically adjusts to your screen size
- Perfect for studying on the go

---

## 🎉 You're All Set!

Everything is ready. Now just run:
```bash
streamlit run app.py
```

And let Mochi help you ace those exams! 🐰✨

---

<div align="center">

**Questions? Found a bug? Let us know!** 

Made with 💜 for students everywhere

</div>
