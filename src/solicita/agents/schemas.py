from pyasn1.type.univ import Boolean
from pydantic import BaseModel, Field


class AgentIn(BaseModel):

    mensage : Field(min_length= 1, max_length= 300)


class OrderItem(BaseModel):

    name : str = Field(description= "nome do produto solicitado")
    quantity : int = Field(description= "quantidade do produto solicitado")

class AgentOut(BaseModel):

    is_order : bool = Field(
        description= "indica se a mensagem contem um pedido"
    )

    itens : list[OrderItem] = Field(
        default_factory= list,
        description= "Lista de produtos solicitados"
    )

