# Copyright (c) 2023, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DisasterHomeSeeker(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from home_portal.home_portal.doctype.references.references import References

		accommodations_for_mobility: DF.Check
		additional_applicants: DF.ReadOnly | None
		ages_of_each_child: DF.Data | None
		attach_image_xntu: DF.AttachImage | None
		brief_description_of_disaster: DF.Text | None
		children_in_home: DF.Check
		contact_information: DF.Link | None
		detached_dwelling_unit: DF.Check
		expected_duration_of_temporary_housing: DF.Data | None
		general_transportation_assistance: DF.Check
		ground_floor_access: DF.Check
		interested_in_long_term_match: DF.Check
		just_drop_off_pickup: DF.Check
		language_assistance: DF.Check
		livestock_boarding: DF.Check
		name_field: DF.Data | None
		need_for_case_management_services: DF.Check
		no_children_in_home: DF.Check
		non_residential_unit: DF.Check
		other_accommodations_for_mobility: DF.Data | None
		other_names_used: DF.Data | None
		placement_with_disaster_survivor_home_provider: DF.Check
		preferred_language_of_household: DF.Data | None
		private_bathroom: DF.Check
		private_entrance: DF.Check
		proximity_to_public_transportation: DF.Check
		references: DF.Table[References]
		required_accommodations: DF.Check
		room_in_home: DF.Check
		rv: DF.Check
		rv_parking_space: DF.Check
		shower_access: DF.Check
		special_accommodations_explanation: DF.Data | None
		special_accommodations_required: DF.Check
		support_from_other_organizations: DF.Check
		tobacco_smoking_ok: DF.Check
		total_children_in_household: DF.Int
		total_livestock_needing_accommodations: DF.Int
		total_people_seeking_accommodations: DF.Int
		total_pets_in_household: DF.Int
		transportation_assistance: DF.Check
		type_of_disaster_recovery_accommodations_interested_in: DF.Check
		type_of_livestock: DF.Data | None
		types_of_each_pet_and_weights: DF.Data | None
		wheelchair_access: DF.Check
	# end: auto-generated types
	pass
