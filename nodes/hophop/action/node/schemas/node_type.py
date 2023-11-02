from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Defaults,
    Property,
    NodeType as  BaseNodeType, DisplayOptions, OptionValue,
)

from nodes.hophop.action.node.static.icon import ICON


class NodeType(flow.NodeType):
    id: str = 'e99f19bc-2506-4265-b368-763fa8e4c1e2'
    type: BaseNodeType.Type = BaseNodeType.Type.action
    displayName: str = 'Hophop'
    icon: str = ICON
    version: int = 1
    description: str = 'switcher of hophop box'
    defaults: Defaults = Defaults(name='hophop-action', color='#DDA0DD')
    properties: List[Property] = [
        Property(
            displayName='Switcher',
            name='switcher',
            type=Property.Type.BOOLEAN,
            placeholder='turn on switcher',
            description='Switcher which turn on extra fields😁',
            required=True,
            default=False,
        ),
        Property(
            displayName='Поле №1',
            name='first_field',
            type=Property.Type.OPTIONS,
            description='Выберите значение для поля №1',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'switcher': [True],
                },
            ),
            options=[
                OptionValue(
                    name='Значение №1',
                    value = 'first_value_first_field',
                    description='Значение №1',
                ),
                OptionValue(
                    name='Значение №2',
                    value='second_value_first_field',
                    description='Значение №2',
                )
            ],
        ),
        Property(
            displayName='Поле №2',
            name='second_field',
            type=Property.Type.OPTIONS,
            description='Выберите значение для поля №2',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'switcher': [True],
                },
            ),
            options=[
                OptionValue(
                    name='Значение №1',
                    value = 'first_value_second_field',
                    description='Значение №1',
                ),
                OptionValue(
                    name='Значение №2',
                    value='second_value_second_field',
                    description='Значение №2',
                )
            ],
        ),
        Property(
            displayName='Поле для ввода почты',
            name='email',
            type=Property.Type.EMAIL,
            placeholder='example@mail.com',
            description='Введите электронную почту',
            displayOptions=DisplayOptions(
                show={
                    'switcher': [True],
                    'first_field': ['first_value_first_field'],
                    'second_field':['first_value_second_field'],
                },
            ),
        ),
        Property(
            displayName='Поле для ввода даты и времени',
            name='datetime',
            type=Property.Type.DATETIME,
            placeholder='ДД.ММ.ГГГГ',
            description='Введите дату и время',
            displayOptions=DisplayOptions(
                show={
                    'switcher': [True],
                    'first_field': ['second_value_first_field'],
                    'second_field':['second_value_second_field'],
                },
            ),
        ),
    ]