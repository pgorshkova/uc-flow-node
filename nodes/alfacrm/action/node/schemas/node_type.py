from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Defaults,
    Property,
    NodeType as  BaseNodeType, DisplayOptions, OptionValue,
)

from nodes.alfacrm.action.node.static.icon import ICON
from nodes.alfacrm.action.node.schemas.enums import Action, Operation, Resource, Parameters


class NodeType(flow.NodeType):
    id: str = '37172e68-7b2e-4e19-bd8b-ee983c3defa6'
    type: BaseNodeType.Type = BaseNodeType.Type.action
    displayName: str = 'AlfaCRMpg'
    icon: str = ICON
    version: int = 1
    description: str = 'AlfaCRM integration'
    defaults: Defaults = Defaults(name='alfacrm-action', color='#DDA0DD')
    properties: List[Property] = [
        Property(
            displayName='Action',
            name='action',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            description='Выберите действие кубика',
            options=[
                OptionValue(
                    name='Авторизация',
                    value=Action.authorization,
                    description='Авторизация пользователя',
                ),
                OptionValue(
                    name='Customer',
                    value=Action.customer,
                    description='Customer',
                ),
            ],
        ),
        Property(
            displayName='Hostname',
            name='hostname',
            type=Property.Type.STRING,
            description='Введите hostname',
            noDataExpression=True,
            placeholder='https://example.com',
            default='uiscom.s20.online',
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='Branch',
            name='branch',
            type=Property.Type.NUMBER,
            description='Введите ID филиала',
            default=1,
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='Email',
            name='email',
            type=Property.Type.EMAIL,
            description='Введите email',
            noDataExpression=True,
            placeholder='example@mail.ru',
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='API key (v2api)',
            name='api_key',
            type=Property.Type.STRING,
            description='Введите ваш API ключ (v2api)',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='Result',
            name='result',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.customer,
                    ],
                },
            ),
        ),
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            description='Выберите нужную модель',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.customer,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Customer',
                    value=Resource.customer,
                    description='Пользователь',
                ),
            ],
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            description='Выберите нужную операцию',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.customer,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Index',
                    value=Operation.index_,
                    description='Чтение списка с фильтрацией и пейджинацией',
                ),
                OptionValue(
                    name='Create',
                    value=Operation.create,
                    description='Создание новой модели',
                ),
                OptionValue(
                    name='Update',
                    value=Operation.update,
                    description='Изменение свойств модели',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.customer,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.index_,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='id',
                    name=Parameters.id,
                    description='Id клиента',
                    type=Property.Type.NUMBER,
                    default=1,
                ),
                Property(
                    displayName='is_study',
                    name=Parameters.is_study,
                    description='Состояние клиента ( 0 - лид, 1 - клиент)',
                    type=Property.Type.BOOLEAN,
                    default=True,
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='Имя клиента',
                    type=Property.Type.STRING,
                    default='',
                ),
                Property(
                    displayName='lead_status_id',
                    name=Parameters.lead_status_id,
                    type=Property.Type.NUMBER,
                    description='Статус id лида',
                ),
                Property(
                    displayName='page',
                    name=Parameters.page,
                    type=Property.Type.NUMBER,
                    description='Страница',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.customer,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.create,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='is_study',
                    name=Parameters.is_study,
                    description='Состояние клиента ( 0 - лид, 1 - клиент)',
                    type=Property.Type.BOOLEAN,
                    default=True,
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='Имя клиента',
                    type=Property.Type.STRING,
                    default='',
                ),
                Property(
                    displayName='legal_type',
                    name=Parameters.legal_type,
                    description='Тип клиента (1 - физ. лицо, 2 - юр. лицо)',
                    values=[
                        Property(
                            type=Property.Type.BOOLEAN,
                            default=True,
                            name=Parameters.legal_type,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        Action.customer,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.update,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='id',
                    name=Parameters.id,
                    description='Id клиента',
                    type=Property.Type.NUMBER,
                    default=1,
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='Имя клиента',
                    type=Property.Type.STRING,
                    default='',
                ),
            ],
        ),
    ]