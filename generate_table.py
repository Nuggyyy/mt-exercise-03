import re
import csv

# File paths
baseline_file = 'models/deen_transformer_baseline/validations.txt'
pre_file = 'models/deen_transformer_pre/validations.txt'
post_file = 'models/deen_transformer_post/validations.txt'
output_csv = 'validation_ppl_comparison.csv'

def extract_steps_ppl(filepath):
    step_ppl = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                match = re.search(r'Steps: (\d+).*?ppl: ([\d\.]+)', line)
                if match:
                    step = int(match.group(1))
                    ppl = float(match.group(2))
                    step_ppl[step] = ppl
    except FileNotFoundError:
        pass  # If the file doesn't exist, just skip it
    return step_ppl

# Extract data
baseline_data = extract_steps_ppl(baseline_file)
pre_data = extract_steps_ppl(pre_file)
post_data = extract_steps_ppl(post_file)

# Get all unique steps, sorted
all_steps = sorted(set(baseline_data.keys()) | set(pre_data.keys()) | set(post_data.keys()))

# Write to CSV
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Validation ppl', 'Baseline', 'Prenorm', 'Postnorm'])
    for step in all_steps:
        baseline_ppl = baseline_data.get(step, '')
        pre_ppl = pre_data.get(step, '')
        post_ppl = post_data.get(step, '')
        writer.writerow([step, baseline_ppl, pre_ppl, post_ppl])

print(f"CSV written to {output_csv}")