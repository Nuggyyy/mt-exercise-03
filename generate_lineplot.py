import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV table
df = pd.read_csv('validation_ppl_comparison.csv')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Validation ppl'], df['Baseline'], label='Baseline')
plt.plot(df['Validation ppl'], df['Prenorm'], label='Prenorm')
plt.plot(df['Validation ppl'], df['Postnorm'], label='Postnorm')
plt.xlabel('Validation Step')
plt.ylabel('Perplexity (ppl)')
plt.title('Validation Perplexity Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('validation_ppl_comparison.png')
plt.show()