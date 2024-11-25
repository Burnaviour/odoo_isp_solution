# __manifest__.py
{
    "name": "ISP Management",
    "version": "1.0",
    "summary": "Manage ISP Customers, Services, and Billing",
    "description": "A module to manage ISP customers, services, and billing with prorated invoicing.",
    "author": "Your Name",
    "depends": ["base", "mail", "account", "subscription_oca", "crm"],
    "data": [
        "security/ir.model.access.csv",
        "views/isp_customer_configuration_views.xml",
        "views/isp_vlans_views.xml",
        "views/views.xml",
    ],
    "installable": True,
    "application": True,
}
