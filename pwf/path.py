"""pwf.path -- path handling."""


def split_path(path):
    """Split the path into its parts.

    Strips trailing slash and removes multiple slashes if any.

    Args:
        path (str)

    Returns:
        list of path components (strings).
    """
    return filter(None, path.split('/'))


def is_error_path(path):
    """Determine if the path is an error path."""
    return len(path) == 1 and path[0].startswith('#err_')
