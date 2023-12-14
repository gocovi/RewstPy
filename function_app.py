import azure.functions as func
import datetime
import base64
import json
import logging

app = func.FunctionApp()

@app.route(route="run", auth_level=func.AuthLevel.FUNCTION)
def ScriptRunner(req: func.HttpRequest) -> func.HttpResponse:
    encoded = req.params.get('encoded')
    body = req.get_body().decode('utf-8')
    # If encoded is true, convert the body from base64 to string
    if encoded == "true":
        script_content = base64.b64decode(body)
    else:
        script_content = body

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
