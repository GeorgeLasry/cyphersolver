import locapi, json, re, sys
d = locapi.get(sys.argv[1])
s = json.dumps(d)
print(sorted(set(re.findall(r'ms\d{6}|mm\s?\d{8}|eadmss\.ms\d+|findingaids\.loc\.gov[^"\s]*', s))))
