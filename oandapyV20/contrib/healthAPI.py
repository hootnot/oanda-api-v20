# -*- coding: utf-8 -*-
"""Handle instruments endpoints."""
from oandapyV20.endpoints.apirequest import APIRequest
from oandapyV20.endpoints.decorators import endpoint


@endpoint("api/v1/services")
class Services(APIRequest):
    """Get a list of services."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self):
        """Instantiate a Services request."""
        endpoint = self.ENDPOINT
        super(Services, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/services/{serviceID}")
class ServiceByID(APIRequest):
    """Get a list of services."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self, serviceID):
        """Instantiate a Service request."""
        endpoint = self.ENDPOINT.format(serviceID=serviceID)
        super(ServiceByID, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/service-lists")
class ServiceLists(APIRequest):
    """Get a list of service lists."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self):
        """Instantiate a ServiceList request."""
        endpoint = self.ENDPOINT
        super(ServiceLists, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/services-lists/{serviceListID}")
class ServiceListByID(APIRequest):
    """Get a single service list."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self, serviceListID):
        """Instantiate a ServiceList request."""
        endpoint = self.ENDPOINT.format(serviceListID=serviceListID)
        super(ServiceListByID, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/services/{serviceID}/events")
class ServiceEventsList(APIRequest):
    """Get a list of events for a service."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self, serviceID, params=None):
        """Instantiate an EventsList request."""
        endpoint = self.ENDPOINT.format(serviceID=serviceID)
        super(ServiceEventsList, self).__init__(endpoint, method=self.METHOD)
        self.params = params


@endpoint("api/v1/services/{serviceID}/events/current")
class ServiceEventCurrent(APIRequest):
    """Get a list of events for a service."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self, serviceID):
        """Instantiate an EventsList request."""
        endpoint = self.ENDPOINT.format(serviceID=serviceID)
        super(ServiceEventCurrent, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/services/{serviceID}/events/{eventID}")
class ServiceEventByID(APIRequest):
    """Get a service event by ID."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self, serviceID, eventID):
        """Instantiate an EventsList request."""
        endpoint = self.ENDPOINT.format(serviceID=serviceID, eventID=eventID)
        super(ServiceEventByID, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/statuses")
class Statuses(APIRequest):
    """Get a list of all statuses."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self):
        """Instantiate a Statuses request."""
        endpoint = self.ENDPOINT
        super(Statuses, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/statuses/{statusID}")
class StatusByID(APIRequest):
    """Get a status by ID."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self, statusID):
        """Instantiate a StatusByID request."""
        endpoint = self.ENDPOINT.format(statusID=statusID)
        super(StatusByID, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/status-images")
class StatusImages(APIRequest):
    """Get a all status images."""
    ENDPOINT = ""
    METHOD = "GET"

    def __init__(self):
        """Instantiate a StatusImages request."""
        endpoint = self.ENDPOINT
        super(StatusImages, self).__init__(endpoint, method=self.METHOD)
