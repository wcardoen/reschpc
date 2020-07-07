import requests
import sys
from . import aux

# Make sure you use ?pages_size=1000 (MAX LIMIT TO GET ALL THE INFO)
# Retrieves the COMPLETE information on analyses

def getinfo(auth,typeid):
    """
    Method to create the job in the Rescale Cloud
        :param auth: Authentication instance
        :param typeid: 0 (analyses) or 1 (coretypes)
        :return: None
    """ 
    dtypes={0:'analyses',1:'coretypes'}
    try:
        r = requests.get(
               'https://platform.rescale.com/api/v2/' + dtypes[typeid] + '/?page_size=1000',
               headers={'Authorization': 'Token ' + auth.TOKEN} 
            )

        if r.status_code == requests.codes.ok:
            print(f"  Info         : {dtypes[typeid]}")
            print(f"  Encoding     : {r.encoding}")
            print(f"  Status Code  : {r.status_code}")

            d = aux.byte2dict(r.content)
            dres = d['results']
            print(f"  #Results:{len(dres)}")
            print(f"  Description::")
            for i,el in enumerate(dres):
                print(f"  #{i+1}::")
                for k in el.keys():
                    print(f"    '{k}'  ->  {el[k]}")
                print("")
        else:
            print(f"  ERROR in requests:{r.status_code}")
    except Exception as err:
        print(f"  ERROR info::getinfo -> {err}")
        sys.exit()

