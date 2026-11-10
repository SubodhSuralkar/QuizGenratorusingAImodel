# 🤖 AI-Powered Quiz Game 🎮

Yo! Welcome to my Quiz Game repo! 👋 

Ever got tired of boring static quizzes where you already know all the questions? Yeah, me too. So I decided to do something special and upgraded this bad boy from square to round tires 🛞✨ by hooking it up with **Gemini AI**! 

Now, you can type literally *any* topic you want—whether it's Python functions, rocket science, or random lore—and the AI will generate 10 fresh, custom quiz questions just for you on the fly! 🚀🔥

---

## ✨ What's Cool About This?

* 🧠 **Infinite Topics:** Not locked into boring pre-defined questions. Ask for whatever topic is on your mind!
* 🤖 **Gemini Powered:** Uses Google's Gemini models to whip up smart quiz questions instantly.
* 💯 **Score Tracking:** Calculates your percentage at the end and tells you how you did with some nice emojis 🥹👌🙌.
* 🛡️ **Fail-Safe Mode:** If the AI servers ever take a quick nap, it gracefully falls back to default questions so the game never stops!

---

## 🛠️ Tech Stack

* **Python** 🐍
* **Google GenAI SDK** ⚡
* **JSON** 📄

---

## 🚀 How to Run This on Your Machine

Want to test it out? Let's get it running:

1. **Clone the repo:**
   ```bash
   git clone https://github.com/SubodhSuralkar/Quiz-Game.git
   cd Quiz-Game
   ```

2. **Set up a virtual environment (Good practice!):**
   ```bash
   python -m venv .venv
   ```
   * Activate it:
     * Windows (CMD): `.venv\Scripts\activate`
     * Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
     * Mac/Linux: `source .venv/bin/activate`

3. **Install dependencies:**
   ```bash
   pip install google-genai
   ```

4. **Set your Gemini API Key:**
   * Get your key from [Google AI Studio](https://aistudio.google.com/) 🔑
   * Set it in your terminal:
     * Windows CMD: `set GEMINI_API_KEY="your_api_key_here"`
     * Windows PowerShell: `$env:GEMINI_API_KEY="your_api_key_here"`
     * Mac/Linux: `export GEMINI_API_KEY="your_api_key_here"`

5. **Run the game:**
   ```bash
   python quiz.py
   ```

---

## 🎯 Example Gameplay

```text
Do you wanna play? yes
What do you want the quiz to be about? 
 Enter the topic--> python functions
Processing-------%----
Correct Answer

Incorrect Answer
You got 80.0%. 🥹👌🙌
```

---

Made with 💻 and lots of debugging by **Subodh**! If you like it, drop a ⭐ on the repo! Catch you later! 😉✌️
