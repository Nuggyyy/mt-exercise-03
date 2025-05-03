import re
import matplotlib.pyplot as plt

# File paths
pre_file = 'models/deen_transformer_pre/validations.txt'
post_file = 'models/deen_transformer_post/validations.txt'

def extract_steps_ppl(filepath):
    step_list = []
    ppl_list = []
    with open(filepath, 'r') as f:
        for line in f:
            match = re.search(r'Steps: (\d+).*?ppl: ([\d\.]+)', line)
            if match:
                step = int(match.group(1))
                ppl = float(match.group(2))
                step_list.append(step)
                ppl_list.append(ppl)
    return step_list, ppl_list

# Extract data
pre_steps, pre_ppl = extract_steps_ppl(pre_file)
post_steps, post_ppl = extract_steps_ppl(post_file)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(pre_steps, pre_ppl, label='Prenorm')
plt.plot(post_steps, post_ppl, label='Postnorm')
plt.xlabel('Validation Step')
plt.ylabel('Perplexity (ppl)')
plt.title('Validation Perplexity Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('validation_ppl_comparison.png')
plt.show()