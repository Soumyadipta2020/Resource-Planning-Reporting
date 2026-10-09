import json

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

sheet5_data = '''  capacitySheet5: {
    title: "Capacity Waterfall",
    waterfallData: [
      { label: "Base", value: 17686, type: "total" },
      { label: "DL Gross Hours", value: -1166, type: "down" },
      { label: "DL Holiday", value: -70, type: "down" },
      { label: "DL Sickness", value: -241, type: "down" },
      { label: "DL Downtime", value: -246, type: "down" },
      { label: "Prod Impact", value: -661, type: "down" },
      { label: "Final", value: 15303, type: "total" }
    ],
    tableColumns: [
      "Gross Hrs", "Holiday", "Holiday %", "Sickness", "Sickness %", "Training", "Training %", "Meeting", "Meeting %", "Other", "Other %", "Total Downtime", "Total Downtime %", "Available Hours", "Prod", "Productive Hrs"
    ],
    tableRows: [
      {
        rowLabel: "GFF1 2026",
        values: ["26,927", "3,150", "11.7%", "1,141", "4.2%", "932", "3.5%", "822", "3.1%", "1,422", "5.3%", "8,051", "29.9%", "18,877", "2.19", "17,686"]
      },
      {
        rowLabel: "Actuals",
        values: ["25,762", "3,220", "11.7%", "1,382", "5.4%", "352", "1.4%", "2,202", "8.5%", "1,023", "4.0%", "8,607", "33.4%", "17,155", "1.95", "15,303"]
      },
      {
        rowLabel: "Variance",
        values: [
          { val: "-1166", dir: "down", color: "text-red-700" },
          { val: "-70", dir: "down", color: "text-red-700" },
          { val: "-0.8%", dir: "down", color: "text-red-700" },
          { val: "-241", dir: "down", color: "text-red-700" },
          { val: "-1.1%", dir: "down", color: "text-red-700" },
          { val: "580", dir: "up", color: "text-emerald-700" },
          { val: "2.1%", dir: "up", color: "text-emerald-700" },
          { val: "-1381", dir: "down", color: "text-red-700" },
          { val: "-5.5%", dir: "down", color: "text-red-700" },
          { val: "399", dir: "up", color: "text-emerald-700" },
          { val: "1.3%", dir: "up", color: "text-emerald-700" },
          { val: "-556", dir: "down", color: "text-red-700" },
          { val: "-3.5%", dir: "down", color: "text-red-700" },
          { val: "-1722", dir: "down", color: "text-red-700" },
          { val: "-0.24", dir: "down", color: "text-red-700" },
          { val: "-2383", dir: "down", color: "text-red-700" }
        ]
      }
    ]
  },
'''

content = content.replace('  regionalData: {', sheet5_data + '\\n  regionalData: {')

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated js/data.js")
