import unittest

import robotsuite
from plonetheme.jquerymobile.testing import ROBOT
from plone.testing import layered


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite('test_functional.robot'),
                layer=ROBOT),
    ])
    return suite
