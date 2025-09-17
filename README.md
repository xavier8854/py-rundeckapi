# py-rundeckapi
Client for Rundeck's REST API

# Usage :

```
from py_rundeckapi import Rundeck

rundeck = Rundeck(
                rundeck_url = "http://myrundeckserver.company.com:4440",
                token = "<your_token_here>",
                api_version=44,
                timeout = 10,
                verify=True,
                proxy = "http://proxy.company.com:3128"
                )

print(rundeck.get("system/info"))
```
