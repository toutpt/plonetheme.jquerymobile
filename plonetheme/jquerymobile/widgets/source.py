from zope.formlib.source import IterableSourceVocabulary

from .multiselect import MultiSelectSetWidget


class SourceMultiSelectSetWidget(MultiSelectSetWidget):
    """Provide a selection list for the set to be selected."""

    def __init__(self, field, source, request):
        super(SourceMultiSelectSetWidget, self).__init__(
            field, IterableSourceVocabulary(source, request), request)
