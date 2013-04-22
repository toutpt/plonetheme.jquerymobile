from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-plonetheme.jquerymobile:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)
