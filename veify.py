import json

# Load the JSON file containing Bandit scan results
with open('bandit_results.json', 'r') as file:
    data = json.load(file)

# Iterate through each entry in the JSON data
for entry in data:
    # Check if the results section is not empty for the current file
    if entry['results']:
        file_name = entry['filename']
        found_issue = False
        # Iterate through each result in the current file
        for result in entry['results']:
            # Check if the issue confidence is high or the issue severity is high
            if result.get('issue_confidence') == 'HIGH' or result.get('issue_severity') == 'HIGH':
                found_issue = True
                issue_cwe = result['issue_cwe']['link'] if 'issue_cwe' in result else 'N/A'
                issue_text = result['issue_text']
                more_info = result['more_info']
                test_name = result['test_name']
                # Print the file name, issue CWE, issue text, more info, and test name
                print(f"File Name: {file_name}")
                if issue_cwe:
                    print(f"Issue CWE: {issue_cwe}")
                if issue_text:
                    print(f"Issue Text: {issue_text}")
                if more_info:
                    print(f"More Info: {more_info}")
                if test_name:
                    print(f"Test Name: {test_name}")
                print()
        if not found_issue:
            print(f"No issues detected in {file_name}")
