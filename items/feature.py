﻿from typing import Mapping, Optional


def features() -> Mapping[str, Optional[str]]:
    if not hasattr(features, 'features'):
        setattr(features, 'features', {
            'bingo': 'Bingo Card',
            })
    return getattr(features, 'features')
