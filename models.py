from dataclasses import dataclass


@dataclass
class Product:
    name: str
    sugar_content: float
    processed_level: int
    ingredients: list
    cost: float
    spike_delta: int
    energy_delta: int

    @classmethod
    def from_dict(cls, data):
        """Creates a Product object from stored product data."""
        return cls(
            name=data["name"],
            sugar_content=data["sugar_content"],
            processed_level=data["processed_level"],
            ingredients=data["ingredients"],
            cost=data["cost"],
            spike_delta=data["spike_delta"],
            energy_delta=data["energy_delta"]
        )