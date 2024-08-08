from . import __version__ as app_version

app_name = "mexico_einvoice"
app_title = "Mexico Einvoice"
app_publisher = "Beveren-Software-Inc"
app_description = "Mexico Einvoice"
app_email = "info@beverensoftware.ca"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mexico_einvoice/css/mexico_einvoice.css"
# app_include_js = "/assets/mexico_einvoice/js/mexico_einvoice.js"

# include js, css files in header of web template
# web_include_css = "/assets/mexico_einvoice/css/mexico_einvoice.css"
# web_include_js = "/assets/mexico_einvoice/js/mexico_einvoice.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mexico_einvoice/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Invoice" : "public/js/sales_invoice.js"
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "mexico_einvoice.utils.jinja_methods",
#	"filters": "mexico_einvoice.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mexico_einvoice.install.before_install"
# after_install = "mexico_einvoice.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mexico_einvoice.uninstall.before_uninstall"
# after_uninstall = "mexico_einvoice.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mexico_einvoice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"on_submit": "factura_com.api.create_sales_invoice",
        # "on_cancel": [
        #     "mexico_einvoice.utils.validate_cancel",
        #     "mexico_einvoice.utils.cancel_einvoice"
		# ]
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"mexico_einvoice.tasks.all"
#	],
#	"daily": [
#		"mexico_einvoice.tasks.daily"
#	],
#	"hourly": [
#		"mexico_einvoice.tasks.hourly"
#	],
#	"weekly": [
#		"mexico_einvoice.tasks.weekly"
#	],
#	"monthly": [
#		"mexico_einvoice.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "mexico_einvoice.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "mexico_einvoice.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "mexico_einvoice.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mexico_einvoice.utils.before_request"]
# after_request = ["mexico_einvoice.utils.after_request"]

# Job Events
# ----------
# before_job = ["mexico_einvoice.utils.before_job"]
# after_job = ["mexico_einvoice.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"mexico_einvoice.auth.validate"
# ]
