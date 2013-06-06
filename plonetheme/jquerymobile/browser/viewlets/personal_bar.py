from plone.app.layout.viewlets import common


class PersonalBarViewlet(common.PersonalBarViewlet):
    def getIcon(self, action):
        return "user"
