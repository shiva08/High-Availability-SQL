# ARM

Prerequisites
1. A Virtual Network
2. A domain controller VM
3. Accounts - LocalAdmin, SQL service, DomainAdmin
4. Subnets for VMs 


Multi subnet template(nested.json) has these features:
1. Create multiple SQL VMs
2. Join the domain
3. Setup AG prerequisites - Failover cluster, configuration
5. Create AG, AGListener



[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/?feature.armendpointprefix=eastus2euap#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fshiva08%2FARM%2Fmain%2Fnested.json)


Maximum VMs = 9

Listenername length <=15

![image](https://user-images.githubusercontent.com/7246619/161142128-97d2f8af-ae41-4d51-9e9c-0d2ed9f58625.png)
