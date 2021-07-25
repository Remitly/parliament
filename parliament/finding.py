class Finding:
    """Class for storing findings"""

    issue = ""
    detail = ""
    location = {}
    associated_statement = {} # a dict representing the associated statement
    severity = "MEDIUM"
    title = ""
    description = ""
    ignore_locations = {}

    def __init__(self, issue, detail, location, associated_statement={}):
        self.issue = issue
        self.detail = detail
        self.location = location
        self.associated_statement = associated_statement

    def dict(self):
        return {
            "issue" : self.issue,
            # "detail" : self.detail,
            "location": self.location,
            "severity": self.severity,
            "title": self.title,
            "description": self.description,
            "ignore_locations": self.ignore_locations,
            "associated_statement": self.associated_statement,
            }

    def __repr__(self):
        """Return a string for printing"""
        return "{} - {} - {}".format(self.issue, self.detail, self.location)
