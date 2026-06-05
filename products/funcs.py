import requests as req
import os
usesqlite = os.getenv('DEBUG')=='True' or os.getenv('HOME')=='/home/aaliali'
# using sqlite meqns we are in dev mode then use qnother ip server
if usesqlite:
    serverip = 'localhost:8000'
else:
    serverip = '157.245.74.156:8000'
def updatestockinremoteserver(products, serverip):
    url = f"http://{serverip}/products/updatestockfromthread"
    headers = {'Content-Type': 'application/json'}
    try:
        response = req.post(url, json=products, headers=headers)
        response.raise_for_status()
        return True
    except req.exceptions.RequestException as e:
        print(f"Error updating stock on remote server: {e}")
        return False