import os
import pickle

# Vulnerable to CWE-78 (Command Injection)
os.system(request.args.get('cmd'))

# Vulnerable to CWE-502 (Deserialization)
data = pickle.loads(request.data)
