from typing import Dict, Any

from src.contexts.shared.domain.Interface import Interface


class Response(Interface):

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError()
