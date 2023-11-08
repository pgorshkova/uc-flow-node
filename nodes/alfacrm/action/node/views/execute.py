from uc_flow_schemas.flow import RunState
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_http_requester.requester import Request


from nodes.alfacrm.action.node.schemas.enums import (
    Action,
    Operation,
    URL_LOGIN,
    URL_GET_CUSTOMER,
    URL_CREATE_CUSTOMER,
    URL_UPDATE_CUSTOMER,
)

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            action = json.node.data.properties['action']

            if action == Action.authorization:
                hostname = json.node.data.properties['hostname']
                email = json.node.data.properties['email']
                api_key = json.node.data.properties['api_key']
                branch = json.node.data.properties['branch']

                url = f'https://{hostname}/v2api/{URL_LOGIN}'

                headers = {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                        }
            
                data = {"email" : email,"api_key" : api_key}

                request = Request(
                    url=url,
                    method=Request.Method.post,
                    json=data,
                    headers=headers)
            
                result = await request.execute()

                result_data = result.json()
                token = result_data['token']

                await json.save_result({
                    "token": token,
                    "branch": branch,
                    "hostname": hostname
                    })
                json.state = RunState.complete

            if action == Action.customer:
                customer_params = json.node.data.properties['parameters']
                token = json.node.data.properties['result']['token']
                branch = json.node.data.properties['result']['branch']
                hostname = json.node.data.properties['result']['hostname']
                operation = json.node.data.properties['operation']

                headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-ALFACRM-TOKEN': token}

                if operation == Operation.index_:
                    url = f'https://{hostname}/v2api/{branch}/{URL_GET_CUSTOMER}'
                
                if operation == Operation.create:
                    url = f'https://{hostname}/v2api/{branch}/{URL_CREATE_CUSTOMER}'
                    customer_params["branch"] = [branch]

                if operation == Operation.update:
                    id = customer_params.pop('id')
                    url = f'https://{hostname}/v2api/{branch}/{URL_UPDATE_CUSTOMER}?id={id}'

                data = Request(
                    url=url,
                    method=Request.Method.post,
                    json=customer_params,
                    headers=headers)

                result = await data.execute()

                await json.save_result({
                "result": result.json()
                })

                json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json