from logging.config import dictConfig

dictConfig({
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(lineno)d | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO"
        }
    },
    "loggers": {
        "httpx": {
            "level": "WARNING"
        },
    "google_genai":{
            "level": "WARNING"
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO"
    }
})