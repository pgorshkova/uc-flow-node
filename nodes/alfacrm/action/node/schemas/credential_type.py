from typing import List, Optional

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Property,
    CredentialProtocol,
)

from nodes.alfacrm.action.node.static.icon import ICON


class CredentialType(flow.CredentialType):
    id: str = "alfacrm_api_auth"
    is_public: bool = True
    displayName: str = 'AlfaCRM API Auth'
    protocol: CredentialProtocol = CredentialProtocol.ApiKey
    protected_properties: List[Property] = []
    properties: List[Property] = [
        Property(
            displayName='Hostname',
            name='hostname',
            type=Property.Type.STRING,
            default='',
        ),
        Property(
            displayName='Email',
            name='email',
            type=Property.Type.EMAIL,
            default='',
        ),
        Property(
            displayName='API key (v2api)',
            name='api_key',
            type=Property.Type.STRING,
            default='',
        ),
        Property(
            displayName='Branch',
            name='branch',
            type=Property.Type.NUMBER,
            default='',
        ),
    ]
    extends: Optional[List[str]] = []
    icon: Optional[str] = ICON