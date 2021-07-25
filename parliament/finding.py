class Finding:
    """Class for storing findings"""

    issue = ""
    detail = ""
    location = {}
    severity = "MEDIUM"
    title = ""
    description = ""
    ignore_locations = {}

    def __init__(self, issue, detail, location):
        self.issue = issue
        self.detail = detail
        self.location = location

    def dict(self):
        return {
            "issue" : self.issue,
            # "detail" : self.detail,
            "location": self.location,
            "severity": self.severity,
            "title": self.title,
            "description": self.description,
            "ignore_locations": self.ignore_locations,
            }

    def __repr__(self):
        """Return a string for printing"""
        return "{} - {} - {}".format(self.issue, self.detail, self.location)
