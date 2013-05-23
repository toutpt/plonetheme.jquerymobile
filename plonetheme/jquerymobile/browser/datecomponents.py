from plone.app.form.widgets import datecomponents as base
from Products.CMFPlone import PloneMessageFactory
_ = PloneMessageFactory


class DateComponents(base.DateComponents):
    """override date components to change the label of empty value"""
    def result(
        self, date=None,
        use_ampm=False,
        starting_year=None,
        ending_year=None,
        future_years=None,
        minute_step=5
    ):
        result = base.DateComponents.result(
            self,
            date=date,
            use_ampm=use_ampm,
            starting_year=starting_year,
            ending_year=ending_year,
            future_years=future_years,
            minute_step=minute_step
        )
        if result["years"][0]["id"] == "--":
            result["years"][0]["id"] = _(u"Year")
        if result["months"][0]["title"] == "--":
            result["months"][0]["title"] = _(u"Month")
        if result["days"][0]["id"] == "--":
            result["days"][0]["id"] = _(u"Day")
        if result["hours"][0]["id"] == "--":
            result["hours"][0]["id"] = _(u"Hour")
        if result["minutes"][0]["id"] == "--":
            result["minutes"][0]["id"] = _(u"Minute")
        if result["ampm"] and result["ampm"][0]["id"] == "--":
            result["ampm"][0]["id"] = _(u"AM/PM")
        return result
