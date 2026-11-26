from models.bed import Bed
import json
from pathlib import Path
class BedService:

    def __init__(self):
        self.beds = []
        self.file_path = Path(__file__).resolve().parent.parent / "data" / "beds.json"
        self.load_beds()

    def load_beds(self):
        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self.file_path.write_text("[]", encoding="utf-8")
        with open(self.file_path, "r") as file:
            data = json.load(file)
        self.beds = [Bed.from_dict(item) for item in data]

    def save_beds(self):
        data = [bed.to_dict() for bed in self.beds]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_bed(self, bed):
        for existing_bed in self.beds:
            if existing_bed.bed_id == bed.bed_id:
                print("Bed ID already exists!")
                return

        self.beds.append(bed)
        self.save_beds() 
        print("Bed added successfully!")

    def view_all_beds(self):
        if not self.beds:
            print("No beds available.")
            return
        for bed in self.beds:
            print(f"Bed ID: {bed.bed_id}, Ward: {bed.ward}, Room: {bed.room}, Status: {bed.status}")

    def search_bed(self, bed_id):
        for bed in self.beds:
            if bed.bed_id == bed_id:
                return bed
        return None
