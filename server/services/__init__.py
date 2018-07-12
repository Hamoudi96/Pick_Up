# The content of this file was generated by IBM Cloud
# Do not modify it as it might get overridden

from ibmcloudenv import IBMCloudEnv
from . import service_manager
IBMCloudEnv.init()

from . import service_alert_notification
from . import service_appid
from . import service_cloudant
from . import service_push


def initServices(app):
	
	name, service = service_alert_notification.getService()
	service_manager.set(name, service)

	name, service = service_appid.getService()
	service_manager.set(name, service)

	name, service = service_cloudant.getService()
	service_manager.set(name, service)

	name, service = service_push.getService()
	service_manager.set(name, service)

	return
