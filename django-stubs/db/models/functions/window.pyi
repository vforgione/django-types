from typing import Any, Optional, Dict, List

from django.db.models import Func

class CumeDist(Func):
    function: str = ...
    name: str = ...
    output_field: Any = ...
    window_compatible: bool = ...

class DenseRank(Func):
    extra: Dict[Any, Any]
    source_expressions: List[Any]
    function: str = ...
    name: str = ...
    output_field: Any = ...
    window_compatible: bool = ...

class FirstValue(Func):
    arity: int = ...
    function: str = ...
    name: str = ...
    window_compatible: bool = ...

class LagLeadFunction(Func):
    window_compatible: bool = ...
    def __init__(self, expression: Optional[str], offset: int = ..., default: None = ..., **extra: Any) -> Any: ...

class Lag(LagLeadFunction):
    function: str = ...
    name: str = ...

class LastValue(Func):
    arity: int = ...
    function: str = ...
    name: str = ...
    window_compatible: bool = ...

class Lead(LagLeadFunction):
    function: str = ...
    name: str = ...

class NthValue(Func):
    function: str = ...
    name: str = ...
    window_compatible: bool = ...
    def __init__(self, expression: Optional[str], nth: int = ..., **extra: Any) -> Any: ...

class Ntile(Func):
    function: str = ...
    name: str = ...
    output_field: Any = ...
    window_compatible: bool = ...
    def __init__(self, num_buckets: int = ..., **extra: Any) -> Any: ...

class PercentRank(Func):
    function: str = ...
    name: str = ...
    output_field: Any = ...
    window_compatible: bool = ...

class Rank(Func):
    function: str = ...
    name: str = ...
    output_field: Any = ...
    window_compatible: bool = ...

class RowNumber(Func):
    function: str = ...
    name: str = ...
    output_field: Any = ...
    window_compatible: bool = ...