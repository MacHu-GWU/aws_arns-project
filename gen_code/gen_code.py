# -*- coding: utf-8 -*-

import typing as T
import importlib
import dataclasses
from pathlib import Path

from aws_arns.model import BaseArn
from jinja2 import Template

dir_here = Path(__file__).absolute().parent
dir_project_root = dir_here.parent
dir_srv = dir_project_root / "aws_arns" / "srv"


def list_all_service_module() -> T.List[str]:
    module_name_list = list()
    for path in dir_srv.glob("*.py"):
        if path.name == "__init__.py":
            continue
        module_name = path.stem
        module_name_list.append(module_name)
    return module_name_list


@dataclasses.dataclass
class Service:
    pass


@dataclasses.dataclass
class Resource:
    module_name: str
    class_name: str

    @property
    def sort_key(self) -> str:
        return f"{self.module_name}.{self.class_name}"


def import_all_service_module(
    module_name_list: T.List[str],
) -> T.List[Resource]:
    resource_list = list()
    for module_name in module_name_list:
        imported_module = importlib.import_module(f"aws_arns.srv.{module_name}")
        for k, v in imported_module.__dict__.items():
            try:
                if issubclass(v, BaseArn) and len(v.__subclasses__()) == 0:
                    if not k.startswith("_"):
                        resource = Resource(
                            module_name=module_name,
                            class_name=k,
                        )
                        resource_list.append(resource)
            except TypeError:
                pass

    resource_list = list(
        sorted(
            resource_list,
            key=lambda x: x.sort_key,
        )
    )
    return resource_list


module_name_list = list_all_service_module()
resource_list = import_all_service_module(module_name_list)

path_resource_py = dir_project_root / "aws_arns" / "resource.py"
path_resource_py_tpl = dir_here / "resource.py.tpl"

template = Template(path_resource_py_tpl.read_text())
path_resource_py.write_text(template.render(resource_list=resource_list))

path_test_api_py = dir_project_root / "tests" / "test_api.py"
path_test_api_py_tpl = dir_here / "test_api.py.tpl"

template = Template(path_test_api_py_tpl.read_text())
path_test_api_py.write_text(template.render(resource_list=resource_list))
