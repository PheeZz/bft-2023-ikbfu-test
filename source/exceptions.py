class EnvNotFoundError(Exception):
    def __init__(self, env_name):
        self.env_name = env_name

    def __str__(self):
        return f"Environment variable '{self.env_name}' not found. Check your .env file."
