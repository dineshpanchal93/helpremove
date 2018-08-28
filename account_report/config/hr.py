from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Over Time"),
			"items": [
				
				{
					"type": "doctype",
					"name": "overtime",
					"description": _("For Overtime.")
				},
				{
					"type": "report",
					"name": "Monthly Overtime",
					"doctype": "overtime",
					"is_query_report": True,
					"label": _("Monthly Overtime Report"),
					"color": "green",
					"icon": "octicon octicon-file-directory"
				},
				{
					"type": "doctype",
					"name": "Overtime Approved",
					"description": _("For Overtime Approved.")
				}
			]

		}

	]
