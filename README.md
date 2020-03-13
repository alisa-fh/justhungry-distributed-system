# justhungry-distributed-system

# How to run

Using python 3.x:

```
pip install pyro4
```
Open 8 command line/terminals - one for each of the following commmands


```
pyro4-ns   

python backend-server-R1.py

python backend-server-R2.py

python backend-server-R3.py

python frontend-server.py

python webservice1.py

python webservice2.py

python client.py
```

Next answer Prompts to user input that client.py was run in to make your order!

# External Services adopted

Two webservices were used in order to retrieve information about the users address from their posctode. They were
https://api.postcodes.io/postcodes/ and http://api.getthedata.com/postcode/

Go to https://pyro4.readthedocs.io/en/stable/ for information on the RMI used