from models.bed import Bed
from services.bed_service import BedService

bed_service = BedService()

bed1 = Bed("B101", "General", "R101")
bed2 = Bed("B102", "ICU", "R102")

bed_service.add_bed(bed1)
bed_service.add_bed(bed2)

print("\nAll Beds:")
bed_service.view_all_beds()
