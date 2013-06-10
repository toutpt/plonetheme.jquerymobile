import unittest2 as unittest
from zope import component
from plonetheme.jquerymobile.tests import base
from zope.publisher.interfaces.browser import IBrowserSkinType
ACTION_IDS = ("portlets", "history")


class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_default_profile_actions(self):
        document_actions = self.layer['portal'].portal_actions.object
        actions = [
            action for action in document_actions.listActions()
            if action.visible and action.id in ACTION_IDS
        ]
        self.assertEqual(len(actions), 2)
        action_info = actions[0].getInfoData()[0]
        self.assertEqual(action_info['category'], 'object')
        self.assertEqual(action_info['available'], True)
        self.assertEqual(action_info['description'], u"")
        self.assertEqual(action_info['title'], u'manage_portlets_link')
        self.assertEqual(
            action_info['url'].text,
            u'string:${object_url}/@@manage-portlets'
        )
        self.assertEqual(action_info['permissions'], ('Manage portlets',))
        self.assertIsNone(action_info['link_target'])
        self.assertEqual(action_info['id'], 'portlets')
        self.assertEqual(action_info['icon'], '')

        action_info = actions[1].getInfoData()[0]
        self.assertEqual(action_info['category'], 'object')
        self.assertEqual(action_info['available'], True)
        self.assertEqual(action_info['description'], u"")
        self.assertEqual(action_info['title'], u'label_history')
        self.assertEqual(
            action_info['url'].text,
            u'string:${object_url}/@@historyview'
        )
        self.assertEqual(
            action_info['permissions'],
            ('CMFEditions: Access previous versions',)
        )
        self.assertIsNone(action_info['link_target'])
        self.assertEqual(action_info['id'], 'history')
        self.assertEqual(action_info['icon'], '')

    def test_browserlayer(self):
        from plonetheme.jquerymobile import layer
        skin = component.queryUtility(
            IBrowserSkinType,
            name="plonetheme.jquerymobile"
        )
        self.assertIsNotNone(skin)
        self.assertEqual(skin, layer.Layer)

    def test_upgrades(self):
        profile = 'plonetheme.jquerymobile:default'
        setup = self.layer['portal'].portal_setup
        upgrades = setup.listUpgrades(profile, show_old=True)
        self.assertTrue(len(upgrades) > 0)
        for upgrade in upgrades:
            upgrade['step'].doStep(setup)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
