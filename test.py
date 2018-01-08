from astuteclient import client

astute = client.Client(
    auth_version = 2,
    username = "admin",
    password = "admin",
    endpoint = "http://198.100.181.73:9080/v2",
    auth_url = "http://198.100.181.73:35357/v2",
    endpoint_type="publicURL",
    region_name = "RegionOne",
    tenant_name = "admin",
    timeout = 10,
    insecure = False,
)

print astute
