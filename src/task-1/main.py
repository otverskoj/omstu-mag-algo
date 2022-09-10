from pprint import pprint
from typing import Callable, Sequence, TypeVar, Optional

T = TypeVar("T")
Comparator = Callable[[T, T], bool]
Sorter = Callable[[Sequence[T], int, int, Comparator], Sequence[T]]


def partition(
    data: Sequence[T],
    start: int,
    end: int,
    comparator: Comparator
) -> int:
    pivot = data[start]
    low = start + 1
    high = end

    while True:
        while low <= high and comparator(data[high], pivot):
            high -= 1

        while low <= high and not comparator(data[low], pivot):
            low += 1

        if low <= high:
            data[low], data[high] = data[high], data[low]
        else:
            break

    data[start], data[high] = data[high], data[start]

    return high


def quick_sort(
    data: Sequence[T],
    start: int,
    end: int,
    comparator: Comparator,
) -> Optional[Sequence[T]]:
    if start >= end:
        return None

    p = partition(data, start, end, comparator)
    quick_sort(data, start, p - 1, comparator)
    quick_sort(data, p + 1, end, comparator)

    return data


def main(sorting_func: Sorter) -> None:
    names = [
        "Олег",
        "Илья",
        "Вова",
        "Катя",
        "Настя",
        "Таня",
        "Кристина"
    ]
    sorted_names = sorting_func(
        data=names[:],
        start=0,
        end=len(names) - 1,
        comparator=lambda s1, s2: s1 > s2
    )
    pprint(sorted_names)


if __name__ == '__main__':
    main(quick_sort)
