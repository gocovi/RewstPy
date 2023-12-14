import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="run", auth_level=func.AuthLevel.FUNCTION)
def ScriptRunner(req: func.HttpRequest) -> func.HttpResponse:
    encoded = req.params.get('encoded')
    # If encoded is true, convert the body from base64 to string
    if encoded == "true":
        # body = b64decode(req.get_body()).decode('utf-8')
        body = req.get_body()
    else:
        body = req.get_body()

    script_content = body.decode('utf-8')
    logging.info(script_content)

    try:
        locals = { "rewst_response": None }
        exec(script_content, None, locals)

        return func.HttpResponse(
            json.dumps({ 
                "response": locals["rewst_response"] 
            }),
            mimetype = "application/json",
            status_code = 200
        )

    except Exception as e:
        logging.info(str(e))
        return func.HttpResponse(
            json.dumps({ 
                "error": str(e) 
            }),
            mimetype = "application/json",
            status_code = 400
        )
