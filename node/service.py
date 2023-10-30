import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = '8a0e986a-6d84-4cd6-9bda-fa0a53c61a9f'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'Sum'
    displayName: str = 'Sum'
    icon: str = '<svg><text x="8" y="50" font-size="50">👻</text></svg>'
    description: str = 'Sum of string and number'
    properties: List[Property] =[
        Property(
            displayName='Text field',
            name='first_value',
            type=Property.Type.JSON,
            placeholder='Write first number',
            description='String',
            required=True,
            default='0',
        ),
        Property(
            displayName='Number field',
            name='second_value',
            type=Property.Type.NUMBER,
            placeholder='Write second number',
            description='Number',
            required=True,
            default=0,
        ),
        Property(
            displayName='Format of answer',
            name='answer_format',
            type=Property.Type.BOOLEAN,
            placeholder='Choose needed format:text or number',
            description='Format',
            required=True,
            default=False,
        ),
    ]
    

class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            properties = json.node.data.properties
            the_first_value = int(properties.get('first_value', "0")) if properties is not None else 0
            the_second_value = properties.get('second_value', 0) if properties is not None else 0
            the_answer_format = properties.get('answer_format', False) if properties is not None else False
            
            sum = the_first_value + the_second_value
            sum = sum if the_answer_format else str(sum)
            await json.save_result({"result": sum})
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json

class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView