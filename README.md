# Index-samle-side
Notebook med kode som viser hvordan man kan bruke Jinja til å lage en samleside med dokumentasjon.

Starten av notebooken er for å lage HTML sidene. Det skal ikke gjøre hver gang.

For template seksjonen i notebooken er tanken skal være i en Azure function som trigger dette hver gang det er et event på blob storage. 

Så flyten blir 
1) pipeline i Azure DevOps - bygg Sphinx og last opp til dokumentasjon - Blob. 
2) Azure Functions blir [trigget av event på blob store](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python) og legger til link og beskrivelse i en samleside (template i notebook)
3) Samlesiden med linker til alle API'er lagres direkte på hovedmappen i Blob-store hvis det er mulig med sikkerhet, eller oppdaterer en [Azure Static Web App](https://azure.microsoft.com/en-us/services/app-service/static/).
