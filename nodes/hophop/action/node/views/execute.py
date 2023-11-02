from uc_flow_schemas.flow import RunState
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            properties: dict = json.node.data.properties
            result = {}

            if properties.get('switch'):
                if properties.get('first_field') == 'first_value_first_field' and properties.get('second_field') == 'first_value_second_field' and properties.get('email'):
                    result = {
                        'switcher': [True],
                        'first_field': ['first_value_first_field'],
                        'second_field':['first_value_second_field'],
                        'email': properties['email'],
                    }
                elif properties.get('first_field') == 'second_value_first_field' and properties.get('second_field') == 'second_value_second_field' and properties.get('datetime'):
                    result = {
                        'switcher': [True],
                        'first_field': ['second_value_first_field'],
                        'second_field':['second_value_second_field'],
                        'datetime': properties['datetime'],
                    }

            await json.save_result(result)
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json
