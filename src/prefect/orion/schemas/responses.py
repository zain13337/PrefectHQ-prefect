from enum import auto

from prefect.orion.schemas.states import State, RunDetails
from prefect.orion.utilities.enum import AutoEnum
from prefect.orion.utilities.schemas import PrefectBaseModel


class SetStateStatus(AutoEnum):
    ACCEPT = auto()
    REJECT = auto()
    ABORT = auto()


class SetStateResponse(PrefectBaseModel):
    status: SetStateStatus
    new_state: State = None
    run_details: RunDetails = None
