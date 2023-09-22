# -*- coding: utf-8 -*-

import dataclasses
from . import resource
from .model import Arn


class ParseArn:
    def __init__(self):
        self._mapper = None

    def _load(self):
        _mapper = dict()
        for k, v in resource.__dict__.items():
            try:
                fields = {field.name: field for field in dataclasses.fields(v)}
                service = fields["service"].default
                resource_type = fields["resource_type"].default
                key = f"{service}.{resource_type}"
                if "Nothing" in key:  # pragma: no cover
                    raise ValueError
                _mapper[key] = v
            except TypeError:
                pass
        self._mapper = _mapper

    def __call__(self, arn: str):
        if self._mapper is None:
            self._load()
        obj = Arn.from_arn(arn)
        key = f"{obj.service}.{obj.resource_type}"
        if key in self._mapper:
            return self._mapper[key].from_arn(arn)
        else:
            return obj


parse_arn = ParseArn()
