import datetime
import os

current_path = os.path.abspath(__file__)
print("the current filepath is :",current_path)

project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
print("the project root path is :", project_root)

dir_path = project_root +'\\report'
# dir_path = r'C:\Users\PRASANNA\PycharmProjects\taf_automation\report'
print("the report dir path is :",dir_path)

os.makedirs(dir_path,exist_ok=True)
# Ensure the 'report' directory exists
# report_dir = "/Users/admin/PycharmProjects/taf/report"
# os.makedirs(report_dir, exist_ok=True)

# Create a single report filename for the session
timestamp = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
# timestamp = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
report_file_name = os.path.join(dir_path,f"report_{timestamp}.txt")
# report_filename = os.path.join(report_dir, f"report_{timestamp}.txt")
# print(report_filename)

def write_output(validation_type, status, details):
    # Write the output to the report file
    with open(report_file_name, "a") as report:
        report.write(f"{validation_type}: {status}\nDetails: {details}\n\n")