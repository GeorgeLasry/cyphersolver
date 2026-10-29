import subprocess,json,urllib.parse,time
U="https://discovery.nationalarchives.gov.uk/API/search/records"
def q(**p):
    url=U+"?"+urllib.parse.urlencode(p)
    for i in range(4):
        r=subprocess.run(["curl","-s","-m","60",url],capture_output=True)
        try: return json.loads(r.stdout.decode("utf8"))
        except Exception: time.sleep(3)
    return None
