from jinja2.ext import Extension
from slugify import slugify as pyslugify


class SlugifyExtension(Extension):
    """Jinja2 Extension to slugify string."""

    def __init__(self, environment):
        """Jinja2 Extension constructor."""
        super().__init__(environment)

        def slugify(value, **kwargs):
            """Slugifies the value."""
            return pyslugify(value, **kwargs)

        environment.filters["slugify"] = slugify
