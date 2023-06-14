"""Exception for communicating with the Loqio Charging Station API."""


class LoqioError(Exception):
    """Generic API exception."""


class LoqioAuthError(LoqioError):
    """API authentication/authorization exception."""


class LoqioConnectionError(LoqioError):
    """API connection exception."""


class LoqioResultsError(LoqioError):
    """API results exception."""


class LoqioTimeoutError(LoqioError):
    """API request timed out."""
