mode = 'pro'

if mode != 'dev':
    from . import jarvis
    from . import configs
if mode != 'pro':
    import jarvis
    import configs


jarvis_features_config = configs.jarvis_features_config
user_config = configs.user_config

jarvis.start(jarvis_features_config, user_config)
