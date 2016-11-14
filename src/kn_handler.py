"""Handle errors."""

class KnError(Exception):
    """Base class."""

    def __init__(self, error_msg='Knotty error.'):
        self.error_msg = error_msg

    def __str__(self):
        return '\n\n' '{}'.format(self.error_msg) + '\n'

class PreprocessingError(KnError):
    """Checked before lexical error."""

    def __init__(self, error_msg='Preprocessing error.'):
        super().__init__(error_msg)
