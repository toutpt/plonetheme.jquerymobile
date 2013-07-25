from zope.formlib.widget import renderElement
from zope.formlib import itemswidgets


class MultiSelectSetWidget(itemswidgets.MultiSelectSetWidget):
    def renderValue(self, value):
        self.extra += ' data-native-menu="false"'
        return super(MultiSelectSetWidget, self).renderValue(value)


class MultiSelectFrozenSetWidget(itemswidgets.MultiSelectFrozenSetWidget):
    def renderValue(self, value):
        self.extra += ' data-native-menu="false"'
        return super(MultiSelectFrozenSetWidget, self).renderValue(value)
