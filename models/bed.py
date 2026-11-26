from datetime import datetime
class Bed:

    def __init__(self, bed_id, ward, room,
                 gender_rule="any",
                 isolation_type="none",
                 status="available",
                 status_since=None):

        self.bed_id = bed_id
        self.ward = ward
        self.room = room
        self.gender_rule = gender_rule
        self.isolation_type = isolation_type
        self.status = status
        self.status_since = status_since or datetime.now().isoformat()

    def to_dict(self):
        return {
            "bed_id": self.bed_id,
            "ward": self.ward,
            "room": self.room,
            "gender_rule": self.gender_rule,
            "isolation_type": self.isolation_type,
            "status": self.status,
            "status_since": self.status_since
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["bed_id"],
            data["ward"],
            data["room"],
            data["gender_rule"],
            data["isolation_type"],
            data["status"],
            data["status_since"]
        )
