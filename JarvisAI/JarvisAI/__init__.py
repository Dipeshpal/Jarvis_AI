mode = 'pro'

if mode == 'pro':
    from . import jarvis
    from . import configs
if mode == 'dev':
    import jarvis
    import configs

if mode == 'dev':
    jarvis_features_config = configs.jarvis_features_config_dev
else:
    jarvis_features_config = configs.jarvis_features_config
user_config = configs.user_config

jarvis.start(jarvis_features_config, user_config)
