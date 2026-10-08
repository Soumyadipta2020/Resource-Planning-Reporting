import re

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_chart4 = """      series.metrics[key] = {
        label: metric.label,
        unit: metric.unit,
        actuals: metric.actuals.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * actScale))),
        forecast: metric.forecast.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * fcScale)))
      };"""
new_chart4 = """      series.metrics[key] = {
        label: metric.label,
        unit: metric.unit,
        actuals: metric.actuals.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * actScale))),
        forecast: metric.forecast.map(v => {
            if (!mults.isPlanActive) return null;
            return v === null ? null : (isPercentOrRatio ? v : Math.round(v * fcScale));
        })
      };"""
js = js.replace(old_chart4, new_chart4)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated js/app.js for sheet4")
