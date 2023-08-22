from dataclasses import dataclass


@dataclass
class BaseStatus:
    text: str
    code: int
    mean: bool

    def __int__(self) -> int:
        return self.code

    def __str__(self) -> str:
        return self.text

    def __bool__(self) -> bool:
        return self.mean

    def __format__(self, format_spec):
        return "a"


STATUS_NO_ERR_SUCCESSFUL = BaseStatus("scraper ending", 200, True)
STATUS_HAS_ERR_SUCCESSFUL = BaseStatus("scraper end {0}", 310, True)
status = format(STATUS_HAS_ERR_SUCCESSFUL, "arge")

print(STATUS_NO_ERR_SUCCESSFUL)