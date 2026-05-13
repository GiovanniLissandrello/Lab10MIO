from dataclasses import dataclass

from model.country import Country


@dataclass
class Arco:
    u : Country
    v : Country