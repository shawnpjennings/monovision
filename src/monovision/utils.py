"""Helper utilities."""


def slugify(text: str) -> str:
    """Lowercase and hyphenate a string."""
    return "-".join(text.lower().split())
