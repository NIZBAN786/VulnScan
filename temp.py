import nmap as nm

nm = nm.PortScanner()

result = nm.scan('127.0.0.1')

# rs = result.pop('nmap')

# rs = result['nmap']['scanstats']

# rs = result['nmap']['scanstats']['uphosts']

rs = result['nmap']['scanstats']['timestr']
# print(result)
print(rs)