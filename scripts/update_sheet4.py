with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('tableColumns: {')
end_str = '        hasSparkbar: false\n      }\n    ]\n  },'
end_idx = content.find(end_str, start_idx)

if start_idx == -1 or end_idx == -1:
    # Try another end string just in case
    end_str2 = 'hasSparkbar: false\\n        }\\n      ]\\n    },'
    end_idx = content.find(end_str2.replace('\\\\n', '\\n'), start_idx)
    if end_idx == -1:
        # let's just use regex but carefully: find 'tableRows: [\s*{.*}\s*]'
        import re
        pattern = re.compile(r'tableColumns:\s*\{.*?tableRows:\s*\[.*?\n    \]\n  \},', re.DOTALL)
        match = pattern.search(content)
        if match:
            start_idx = match.start()
            end_idx = match.end() - len('\n  },')
        else:
            print('Could not find boundaries')
            exit(1)
    else:
        end_idx += len(end_str2.replace('\\\\n', '\\n'))
else:
    end_idx += len(end_str) - len('\n  },')

new_table = '''tableColumns: {
        actualsHeaders: ["17 Aug", "24 Aug", "31 Aug", "07 Sep", "14 Sep"],
        currentWeek: {
          weekLabel: "21 Sep",
          subHeaders: ["Actual", "Forecast", "Variance"]
        },
        forecastHeaders: ["28 Sep", "05 Oct", "12 Oct", "19 Oct", "26 Oct"]
      },
      tableRows: [
        { metric: "DL Headcount", actuals: ["691", "692", "692", "691", "689"], currentActual: "690", currentForecast: "698", variance: "8", varDir: "down", varType: "negative", futureForecast: ["697", "708", "708", "708", "708"], hasSparkbar: false },
        { metric: "DL Gross Hours", actuals: ["25,696", "25,820", "26,110", "25,390", "25,689"], currentActual: "25,762", currentForecast: "26,927", variance: "-1,165", varDir: "down", varType: "negative", futureForecast: ["27,271", "27,326", "27,326", "27,326", "27,326"], hasSparkbar: false },
        { metric: "DL Holiday", actuals: ["5,740", "6,723", "3,178", "2,776", "3,399"], currentActual: "3,220", currentForecast: "3,150", variance: "70", varDir: "down", varType: "negative", futureForecast: ["2,616", "2,444", "2,444", "2,444", "2,444"], hasSparkbar: false },
        { metric: "DL Holiday %", actuals: ["22.3%", "26.0%", "12.2%", "10.9%", "13.2%"], currentActual: "12.5%", currentForecast: "11.7%", variance: "0.8%", varDir: "down", varType: "negative", futureForecast: ["9.6%", "8.9%", "8.9%", "8.9%", "8.9%"], hasSparkbar: false },
        { metric: "DL Sickness", actuals: ["1,539", "1,663", "1,225", "1,547", "1,338"], currentActual: "1,382", currentForecast: "1,141", variance: "241", varDir: "down", varType: "negative", futureForecast: ["1,254", "1,258", "1,258", "1,258", "1,258"], hasSparkbar: false },
        { metric: "DL Sickness %", actuals: ["6.0%", "6.4%", "4.7%", "6.1%", "5.2%"], currentActual: "5.4%", currentForecast: "4.2%", variance: "1.1%", varDir: "down", varType: "negative", futureForecast: ["4.6%", "4.6%", "4.6%", "4.6%", "4.6%"], hasSparkbar: false },
        { metric: "DL Downtime excl. Hol & Sick", actuals: ["2,932", "2,568", "7,246", "2,927", "2,586"], currentActual: "4,005", currentForecast: "3,759", variance: "246", varDir: "down", varType: "negative", futureForecast: ["5,009", "3,814", "3,814", "3,814", "3,814"], hasSparkbar: false },
        { metric: "DL Downtime % excl. Hol & Sick", actuals: ["11.4%", "9.9%", "27.8%", "11.5%", "10.1%"], currentActual: "15.5%", currentForecast: "14.0%", variance: "1.5%", varDir: "down", varType: "negative", futureForecast: ["18.4%", "14.0%", "14.0%", "14.0%", "14.0%"], hasSparkbar: false },
        { metric: "Total DL Downtime", actuals: ["10,211", "10,954", "11,650", "7,250", "7,324"], currentActual: "8,607", currentForecast: "8,051", variance: "556", varDir: "down", varType: "negative", futureForecast: ["8,879", "7,515", "7,515", "7,515", "7,515"], hasSparkbar: false },
        { metric: "Total DL Downtime %", actuals: ["39.7%", "42.4%", "44.6%", "28.6%", "28.5%"], currentActual: "33.4%", currentForecast: "29.9%", variance: "3.5%", varDir: "down", varType: "negative", futureForecast: ["32.6%", "27.5%", "27.5%", "27.5%", "27.5%"], hasSparkbar: false },
        { metric: "DL Available Hours", actuals: ["15,485", "14,866", "14,460", "18,140", "18,365"], currentActual: "17,155", currentForecast: "18,877", variance: "-1,722", varDir: "down", varType: "negative", futureForecast: ["18,392", "19,810", "19,810", "19,810", "19,810"], hasSparkbar: false },
        { metric: "DL Availability %", actuals: ["60.3%", "57.6%", "55.4%", "71.4%", "71.5%"], currentActual: "66.6%", currentForecast: "70.1%", variance: "-3.5%", varDir: "down", varType: "negative", futureForecast: ["67.4%", "72.5%", "72.5%", "72.5%", "72.5%"], hasSparkbar: false },
        { metric: "DL Utilisation %", actuals: ["53.7%", "51.4%", "46.0%", "63.0%", "63.0%"], currentActual: "59.4%", currentForecast: "65.7%", variance: "-6.3%", varDir: "down", varType: "negative", futureForecast: ["63.2%", "68.0%", "68.0%", "68.0%", "68.0%"], hasSparkbar: false },
        { metric: "DL Gaps", actuals: ["1,691", "1,607", "2,450", "2,141", "2,194"], currentActual: "1,852", currentForecast: "1,191", variance: "661", varDir: "down", varType: "negative", futureForecast: ["1,147", "1,231", "1,231", "1,231", "1,231"], hasSparkbar: false },
        { metric: "DL Gaps %", actuals: ["6.6%", "6.2%", "9.4%", "8.4%", "8.5%"], currentActual: "7.2%", currentForecast: "4.4%", variance: "2.8%", varDir: "down", varType: "negative", futureForecast: ["4.2%", "4.5%", "4.5%", "4.5%", "4.5%"], hasSparkbar: false },
        { metric: "DL Productivity", actuals: ["1.9", "1.9", "1.9", "1.9", "1.9"], currentActual: "2.0", currentForecast: "2.2", variance: "-0.2", varDir: "down", varType: "negative", futureForecast: ["2.3", "2.4", "2.4", "2.4", "2.4"], hasSparkbar: false },
        { metric: "DL Productive Hrs", actuals: ["13,794", "13,259", "12,010", "15,999", "16,171"], currentActual: "15,303", currentForecast: "17,686", variance: "-2,383", varDir: "down", varType: "negative", futureForecast: ["17,245", "18,579", "18,579", "18,579", "18,579"], hasSparkbar: false },
        { metric: "DL Installs", actuals: ["781", "775", "726", "920", "944"], currentActual: "897", currentForecast: "1,073", variance: "-176", varDir: "down", varType: "negative", futureForecast: ["1,101", "1,217", "1,217", "1,217", "1,217"], hasSparkbar: false },
        { metric: "Total Installs", actuals: ["1,450", "1,460", "1,247", "1,696", "1,734"], currentActual: "1,689", currentForecast: "1,988", variance: "-299", varDir: "down", varType: "negative", futureForecast: ["2,160", "2,276", "2,276", "2,276", "2,276"], hasSparkbar: false },
        { metric: "DL Planning Efficeincy %", actuals: ["89.1%", "89.2%", "83.1%", "88.2%", "88.1%"], currentActual: "89.2%", currentForecast: "93.7%", variance: "-4.5%", varDir: "down", varType: "negative", futureForecast: ["93.8%", "93.8%", "93.8%", "93.8%", "93.8%"], hasSparkbar: true }
      ]'''

new_content = content[:start_idx] + new_table + content[end_idx:]
with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Updated data.js')
