
jarvis_features_config = [
  {
    "regex": "weather|temperature|wind|clouds|rainy",
    "import": "features.weather.weather",
    "function_name": "weather_app"
  },
  {
    "regex": "setup|set up",
    "import": "features.setup.user_setup",
    "function_name": "setup_mode"
  },
  {
    "regex": "tell me date|date|today is what day",
    "import": "features.date_time.jarvis_date_time",
    "function_name": "tell_me_date"
  },
  {
    "regex": "time",
    "import": "features.date_time.jarvis_date_time",
    "function_name": "tell_me_time"
  }
]
