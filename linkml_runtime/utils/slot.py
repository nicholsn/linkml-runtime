from dataclasses import dataclass
import re
from typing import Type, List, Optional, Any

from rdflib import URIRef


@dataclass
class Slot:
    """ Runtime slot definition """
    uri: URIRef
    name: str
    curie: Optional[str]
    model_uri: URIRef

    domain: Optional[Type]
    range: Any
    mappings: Optional[List[URIRef]] = None
    pattern: Optional[re] = None
