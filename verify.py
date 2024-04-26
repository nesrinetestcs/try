import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the JSON file containing Bandit scan results
with open('bandit_results.json', 'r') as file:
    data = json.load(file)

# Create a PDF file to write the results
pdf_file = 'bandit_results.pdf'
c = canvas.Canvas(pdf_file, pagesize=letter)

# Set the initial y-coordinate for writing text
y_coordinate = 750

# Iterate through each entry in the JSON data
for entry in data:
    # Check if the results section is not empty for the current file
    if entry['results']:
       
        found_issue = False
        # Iterate through each result in the current file
        for result in entry['results']: 
            file_name = result['filename']
            # Check if the issue confidence is high or the issue severity is high
            if result.get('issue_confidence') == 'HIGH' or result.get('issue_severity') == 'HIGH':
                found_issue = True
                issue_cwe = result['issue_cwe']['link'] if 'issue_cwe' in result else 'N/A'
                issue_text = result['issue_text']
                more_info = result['more_info']
                test_name = result['test_name']
                # Write the file name, issue CWE, issue text, more info, and test name to the PDF
                c.drawString(100, y_coordinate, f"File Name: {file_name}")
                y_coordinate -= 20
                if issue_cwe:
                    c.drawString(100, y_coordinate, f"Issue CWE: {issue_cwe}")
                    y_coordinate -= 20
                if issue_text:
                    c.drawString(100, y_coordinate, f"Issue Text: {issue_text}")
                    y_coordinate -= 20
                if more_info:
                    c.drawString(100, y_coordinate, f"More Info: {more_info}")
                    y_coordinate -= 20
                if test_name:
                    c.drawString(100, y_coordinate, f"Test Name: {test_name}")
                    y_coordinate -= 20
                y_coordinate -= 20  # Add some space between each result
        if not found_issue:
            c.drawString(100, y_coordinate, f"No issues detected in {file_name}")
            y_coordinate -= 20

# Save the PDF file
c.save()
