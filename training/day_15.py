data_struct ={
    "id": "create_stock_item_attribute",
    "folder": "attributes",
    "main": {
        "data": {
            "attributeCode": "${uuid}"
        },
        "steps": {
            "start": {
                "type": "side_panel_actions",
                "action": "create",
                "args": {
                    "entity": "Attribute",
                    "changes": {
                        "code": "$d{attributeCode}",
                        "description": "$d{attributeCode}",
                        "permissionTreeCode": "VIRTUAL - GLOBAL"
                    },
                    "submit": "save and close"
                },
                "next_step": "create_stock_item_attribute"
            },
            "create_stock_item_attribute": {
                "type": "side_panel_actions",
                "action": "create",
                "args": {
                    "entity": "Stock Item Attribute",
                    "changes": {
                        "stockItemMaterialMasterCode": "CHAIN",
                        "permissionTreeCode": "VIRTUAL - GLOBAL",
                        "attributeCode": "$d{attributeCode}"
                    },
                     "submit": "save and update"
                },
                "next_step": "perform_update"
            },
            "perform_update": {
                "type": "edit_screen",
                "action": "update",
                "args": {
                    "changes": {
                        "sequenceNumber": 5,
                        "notes": "${uuid}"
                    }
                }
            }
        }
    }
}

filter_strings = []
for step in data_struct["main"]["steps"].values():
    changes = step["args"].get("changes", {})
    for key, value in changes.items():
        filter_string = f"{key} eq '{value}'"
        filter_strings.append(filter_string)

print(filter_strings)