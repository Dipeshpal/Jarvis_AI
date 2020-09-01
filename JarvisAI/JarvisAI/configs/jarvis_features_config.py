
jarvis_features_config = [
  {
    "regex": "weather|temperature|wind|clouds|rainy",
    "import": "JarvisAI.features.weather.weather",
    "function_name": "weather_app"
  },
  {
    "regex": "setup|set up",
    "import": "JarvisAI.features.setup.user_setup",
    "function_name": "setup_mode"
  },
  {
    "regex": "tell me date|date|today is what day",
    "import": "JarvisAI.features.date_time.jarvis_date_time",
    "function_name": "tell_me_date"
  },
  {
    "regex": "time",
    "import": "JarvisAI.features.date_time.jarvis_date_time",
    "function_name": "tell_me_time"
  }
]
