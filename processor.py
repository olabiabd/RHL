def process_vehicle_availability(response_data):
    processed_data = []

    for vehicle in response_data:
        row = {
            "vehicleId": vehicle.get("vehicleId", ""),
            "registration": vehicle.get("registration", ""),
            "type": vehicle.get("type", ""),
            "customId": vehicle.get("customId", ""),
            "fleetNumber": vehicle.get("fleetNumber", ""),
            "fleetName": vehicle.get("fleetName", ""),
            "inactive": vehicle.get("inactive", ""),
            "inactiveDate": vehicle.get("inactiveDate", ""),
            "inactiveReason": vehicle.get("inactiveReason", ""),
            "inactiveDescription": vehicle.get("inactiveDescription", ""),
            "nonFleetVehicle": vehicle.get("nonFleetVehicle", ""),
            "categoryType": vehicle.get("categoryType", ""),
            "categoryName": vehicle.get("categoryName", ""),
            "ownerDivision": vehicle.get("ownerDivision", ""),
            "division": vehicle.get("division", ""),
            "currentStatus": vehicle.get("currentStatus", "")
        }

        vor = vehicle.get("vehicleOffRoadDetails") or {}
        row.update({
            "VOR_currentStatus": vor.get("currenctVORStatus", ""),
            "VOR_daysOffRoad": vor.get("daysOffRoad", ""),
            "VOR_reason": vor.get("reason", ""),
            "VOR_description": vor.get("description", ""),
            "VOR_plannedUnplanned": vor.get("plannedUnplanned", "")
        })

        curr = vehicle.get("currentMaintenaceEvent") or {}
        row.update({
            "currentMaint_status": curr.get("status", ""),
            "currentMaint_maintenanceType": curr.get("maintenanceType", ""),
            "currentMaint_date": curr.get("date", ""),
            "currentMaint_endDate": curr.get("endDate", ""),
            "currentMaint_plannedUnplanned": curr.get("plannedUnplanned", ""),
            "currentMaint_purpose": curr.get("purpose", ""),
            "currentMaint_notesForWorkshop": curr.get("notesForWorkshop", "")
        })

        upcoming = (vehicle.get("upcomingMaintenaceEvents") or [{}])[0]
        row.update({
            "upcomingMaint_maintenanceType": upcoming.get("maintenanceType", ""),
            "upcomingMaint_date": upcoming.get("date", ""),
            "upcomingMaint_endDate": upcoming.get("endDate", ""),
            "upcomingMaint_plannedUnplanned": upcoming.get("plannedUnplanned", ""),
            "upcomingMaint_purpose": upcoming.get("purpose", ""),
            "upcomingMaint_notesForWorkshop": upcoming.get("notesForWorkshop", "")
        })

        processed_data.append(row)

    return processed_data
