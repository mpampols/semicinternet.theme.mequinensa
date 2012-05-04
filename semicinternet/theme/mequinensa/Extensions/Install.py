import transaction
from Products.CMFCore.utils import getToolByName

UNINSTALL_PROFILES = [
    'semicinternet.theme.mequinensa:uninstall'
]

def uninstall(self):
    portal_setup = getToolByName(self, 'portal_setup')
    for extension_id in UNINSTALL_PROFILES:
        portal_setup.runAllImportStepsFromProfile('profile-%s' % extension_id)
        product_name = extension_id.split(':')[0]
        transaction.savepoint()
