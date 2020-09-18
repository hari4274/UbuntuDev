# Extract URL parameters from URL


url = 'https://checkout.getaclearrear.com/rearodfulfill/checkout?fulfill=false'

try:
    from urllib.parse import urlparse, parse_qsl
except ImportError:
    from urlparse import urlparse, parse_qsl

parsed = urlparse(url)

params = parse_qsl(parsed.query)

data = {}

for k, v in params:
  if v.lower() == 'true':
    v = 1
  if v.lower() == 'false':
    v = 0

  data[k] = v
  print(f"Parameter = {k}, Value = {v}")

print(params)
print(data)

# Result
# Parameter = fulfill, Value = 0
# [('fulfill', 'false')]
# {'fulfill': 0}
