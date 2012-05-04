from plone.app.registry.browser import controlpanel

from semicinternet.theme.mequinensa.browser.interfaces import IMequinensaSettings, _

class MequinensaSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IMequinensaSettings
    label = _(u"Mequinensa settings")
    description = _(u"""""")

    def updateFields(self):
        super(MequinensaSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(MequinensaSettingsEditForm, self).updateWidgets()

class MequinensaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MequinensaSettingsEditForm
