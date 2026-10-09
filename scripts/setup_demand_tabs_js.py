import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add demandSheet to state
content = re.sub(r'capacitySheet: "sheet-2",', r'capacitySheet: "sheet-2",\n    demandSheet: "dsheet-1",', content)

# 2. Add switchDemandSheet and updateDemandSheet
methods_code = """
  switchDemandSheet(sheetId) {
    this.state.demandSheet = sheetId;

    document.querySelectorAll(".dsheet-toggle-btn").forEach(btn => {
      if (btn.getAttribute("data-dsheet") === sheetId) {
        btn.classList.add("bg-blue-700", "text-white", "shadow-sm");
        btn.classList.remove("bg-slate-100", "text-slate-700", "hover:bg-slate-200");
      } else {
        btn.classList.remove("bg-blue-700", "text-white", "shadow-sm");
        btn.classList.add("bg-slate-100", "text-slate-700", "hover:bg-slate-200");
      }
    });

    document.querySelectorAll(".demand-sheet-content").forEach(content => {
      if (content.id === `demand-${sheetId}`) {
        content.classList.remove("hidden");
      } else {
        content.classList.add("hidden");
      }
    });

    setTimeout(() => {
      this.updateDemandSheet();
    }, 50);
  },

  updateDemandSheet() {
    // Add logic here to render specific demand sheets if needed
    if (this.state.demandSheet === "dsheet-1") {
       // Render demand overview
    } else if (this.state.demandSheet === "dsheet-2") {
       // Render yearly comparison
    } else if (this.state.demandSheet === "dsheet-3") {
       // Render ES weekly workload
    } else if (this.state.demandSheet === "dsheet-4") {
       // Render demand waterfall
    }
  },
"""
content = re.sub(r'  switchCapacitySheet\(sheetId\) \{', methods_code + '\n  switchCapacitySheet(sheetId) {', content)

# 3. Add to bindEvents
bind_code = """
    // Demand Overview Sheet sub-navigation buttons
    document.querySelectorAll(".dsheet-toggle-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const sheetId = btn.getAttribute("data-dsheet");
        if (sheetId) {
          this.switchDemandSheet(sheetId);
        }
      });
    });

"""
content = re.sub(r'    // Sheet 4 Business Unit filter buttons', bind_code + '    // Sheet 4 Business Unit filter buttons', content)

# 4. Show/hide demand-nav-tabs in switchTab
nav_code = """
    // Show/hide demand views sub-navigation bar
    const demandTabs = document.getElementById("demand-nav-tabs");
    if (demandTabs) {
      if (tabId === "demand") {
        demandTabs.style.setProperty("display", "flex", "important");
        demandTabs.classList.remove("hidden");
      } else {
        demandTabs.style.setProperty("display", "none", "important");
        demandTabs.classList.add("hidden");
      }
    }
"""
content = re.sub(r'    // Update visible view container', nav_code + '\n    // Update visible view container', content)


with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js")

