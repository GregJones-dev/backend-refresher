records = [
    {"id": 101, "dept": "Logistics", "status": "Active", "budget": 45000},
    {"id": 102, "dept": "IT", "status": "Inactive", "budget": 12000},
    {"id": 103, "dept": "Logistics", "status": "Active", "budget": 82000},
    {"id": 104, "dept": "Finance", "status": "Active", "budget": 60000},
]

high_value_active = [
    r for r in records if r["status"] == "Active" and r["budget"] >= 50000
]

print(f"Filtered {len(high_value_active)} qualifying records:")
for item in high_value_active:
    print(f"ID: {item['id']} | Dept: {item['dept']} | Budget: ${item['budget']:,}")
