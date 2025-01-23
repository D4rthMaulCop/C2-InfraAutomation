from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import NetworkSecurityGroup, SecurityRule, VirtualNetwork, Subnet, NetworkInterface, PublicIPAddress
from azure.mgmt.compute.models import HardwareProfile, StorageProfile, OSDisk, ManagedDiskParameters, OSProfile, NetworkInterfaceReference, VirtualMachine, DiagnosticsProfile, BootDiagnostics
from azure.mgmt.compute.models import VirtualMachineExtension
import random
import string
import time
import termcolor
import uuid

def generate_uuid():
    return str(uuid.uuid4())

def generate_complex_string():
    characters = string.ascii_letters + string.digits + string.punctuation
    complex_string = ''.join(random.choices(characters, k=24))
    return complex_string


# Azure Configuration
subscription_id = ''
resource_group_name = generate_uuid() + '_Azure-Red-Team-Infra'
location = 'centralus'
vm_name = 'c2-deploy'
ssh_username = 'operator'
ssh_password = generate_complex_string()
c2_port = random.randint(30000, 60000)

print(resource_group_name)
print(ssh_password)
