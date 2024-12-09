# Overview

Use this project and workflow to run raw Python directly in Azure Functions. This is similar to my [RewstPS project](https://github.com/gocovi/RewstPS).

# Setup

1. Fork this repository.
1. Create a Function App in Azure. You'll want to the latest version of Python and Linux as your operating system..
1. In your Function App in Azure, go to **Deployment Center** and connect it to the forked GitHub repository.
1. In Overview, copy your URL. We'll use this later to setup our Custom Integration. It will look like the following: https://yourfunctionapp.azurewebsites.net/api/run.
1. Navigate to your function app in Azure, then go to Overview. Under functions, click **ScriptRunner**.
1. Under Function Keys, copy your default key. We'll also be using this in the Custom Integration.
1. In Rewst, navigate to Configuration > Integrations > Custom Integrations. Add a new one called "Rewst Python" and match the settings below:

    | Hostname                          | API Key            | Authentication Method | API Key Header Name |
    | --------------------------------- | ------------------ | --------------------- | ------------------- |
    | yourfunctionapp.azurewebsites.net | The key you copied | API Key               | x-functions-key     |

1. Import the `run-python.bundle.json` file as a new workflow.
1. In the `run_script` action under Advanced, you may need to add an Integration Override for your new Rewst Python integration as well and then click publish.

# Usage

1. Create a Python script under Scripts in Rewst. If you want to return results, assign something to a variable named `rewst_response`.
1. Open the `Run Python` workflow and click Test.
1. For script content, enter select your test script.
1. See your result in `RESULT.result`.

# Packages

If you wish to use any packages, you'll need to put them in a `requirements.txt` file in your own repo. Currently, there's an issue I haven't had time to fully diagnose where GitHub Actions won't deploy a package with the required packages. A workaround would be to instead use Azure Functions Tools and deploy locally. The high-level process is:

1. Install [Azure Functions Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python).
1. Run `func azure functionapp publish YOUR_APP_NAME --python` from the root of your forked repo.
