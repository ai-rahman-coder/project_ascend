class AIProviderError(Exception):
    """Base exception for all AI provider related errors."""


class RateLimitExceededError(AIProviderError):
    """Raised when an AI provider exceeds its rate limit."""


class ProviderUnavailableError(AIProviderError):
    """Raised when an AI provider is unavailable or down."""


class InvalidProviderResponseError(AIProviderError):
    """Raised when an AI provider returns an invalid or unexpected response."""


class UnauthorizedAccessError(AIProviderError):
    """Raised when an AI provider returns an unauthorized access error (e.g., 401)."""