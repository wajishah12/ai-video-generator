import sys

with open(sys.argv[1], 'r') as f:
    transcript = f.read()

# Implement your script generation logic here
hindi_script = transcript  # Replace with your logic

with open('hindi_script.txt', 'w') as f:
    f.write(hindi_script)
