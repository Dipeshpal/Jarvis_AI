from . import jarvis
from . import configs


jarvis_features_config = configs.jarvis_features_config
user_config = configs.user_config

jarvis.start(jarvis_features_config, user_config)
