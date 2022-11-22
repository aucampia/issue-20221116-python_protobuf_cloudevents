#!/usr/bin/env python3
import argparse
import logging
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Union

import rope.base.libutils as rlibutils
import rope.base.pyobjectsdef as rpyobjectsdef
import rope.base.resources as rresources
import rope.contrib.generate as rgenerate
from rope.base.project import Project
from rope.refactor.move import MoveModule
from rope.refactor.rename import Rename
from rope.refactor.restructure import Restructure

logger = logging.getLogger(__name__)

__all__ = ["Application", "main"]


@dataclass
class Application:
    parser: argparse.ArgumentParser = field(
        default_factory=lambda: argparse.ArgumentParser(add_help=True)
    )

    def __post_init__(self) -> None:
        parser = self.parser
        parser.add_argument(
            "-v",
            "--verbose",
            action="count",
            dest="verbosity",
            help="increase verbosity level",
        )
        parser.add_argument(
            "--prefix", action="store", type=str, required=True, dest="prefix"
        )
        parser.add_argument("target", nargs="+", type=str)
        parser.set_defaults(handler=self.handle)

    def run(self, args: List[str]) -> None:
        parse_result = self.parser.parse_args(args)

        verbosity = parse_result.verbosity
        if verbosity is not None:
            root_logger = logging.getLogger("")
            root_logger.propagate = True
            new_level = (
                root_logger.getEffectiveLevel()
                - (min(1, verbosity)) * 10
                - min(max(0, verbosity - 1), 9) * 1
            )
            root_logger.setLevel(new_level)

        logger.debug(
            "sys.executable = %s, args = %s, parse_result = %s, logging.level = %s",
            sys.executable,
            args,
            parse_result,
            logging.getLogger("").getEffectiveLevel(),
        )

        parse_result.handler(parse_result)

    def handle(self, parse_result: argparse.Namespace) -> None:
        logger.debug("entry ...")

        targets: List[str] = parse_result.target
        logger.info("targets  = %s", targets)

        prefix: str = parse_result.prefix

        target = targets[0]
        project_path = Path(target).absolute()
        project = Project(target)
        logger.info("project_path = %s, project  = %s", project_path, project)

        python_files: List[rresources.File] = [
            *project.get_python_files(),
        ]
        resources: List[rresources.Resource] = [
            *project.get_python_files(),
            *project.get_source_folders(),
        ]

        logger.info("resources = %s", resources)

        for old_python_file in python_files:
            logger.info(
                "old_python_file = %s, old_python_file.path = %s, old_python_file.real_path = %s, old_python_file.pathlib = %s",
                old_python_file,
                old_python_file.path,
                old_python_file.real_path,
                old_python_file.pathlib,
            )

            old_path = old_python_file.pathlib
            old_path_relative = old_path.relative_to(project_path)
            logger.info("old_path = %s", old_path)
            logger.info("old_path_relative = %s", old_path_relative)
            new_path_relative = Path(*prefix.split(".")) / old_path_relative
            new_path = project_path / new_path_relative
            logger.info("new_path = %s", new_path)
            logger.info("new_path_relative = %s", new_path_relative)

            old_package_path = old_path.parent
            old_package_path_relative = old_path_relative.parent
            old_package_name = ".".join(old_package_path_relative.parts)
            logger.info("old_package_path = %s", old_package_path)
            logger.info("old_package_path_relative = %s", old_package_path_relative)
            logger.info("old_package_name = %s", old_package_name)

            if old_package_name.startswith(prefix):
                logging.info(
                    "skipping %s as it already starts with %s",
                    old_package_name,
                    prefix,
                )
                continue

            new_package_path = new_path.parent
            new_package_path.mkdir(parents=True, exist_ok=True)
            new_package_path_relative = new_path_relative.parent
            new_package_name = ".".join(new_package_path_relative.parts)
            logger.info("new_package_name = %s", new_package_name)
            # new_package = project.find_module(new_package_name)
            # logger.info("new_package = %s", new_package)

            # new_package = rgenerate.create_package(project, new_package_name)
            # logger.info(
            #     "new_package = %s, new_package_name = %s", new_package, new_package_name
            # )

            python_module: Union[
                rpyobjectsdef.PyModule, rpyobjectsdef.PyPackage
            ] = project.get_pymodule(old_python_file)
            if not isinstance(python_module, rpyobjectsdef.PyModule):
                raise RuntimeError(
                    f"python_file.real_path = {old_python_file.real_path} must be a python module"
                )
            logger.info(
                "python_module = %s, python_module.get_name() = %s, python_module.absolute_name = %s",
                python_module,
                python_module.get_name(),
                python_module.absolute_name,
            )

            python_file_modname = rlibutils.modname(old_python_file)
            logger.info("python_file_modname = %s", python_file_modname)

            # generate.create_package(project, 'pkg')

            new_package_resource = rresources.Folder(
                project, f"{new_package_path_relative}"
            )
            logger.info("new_package_resource = %s", new_package_resource)

            # change = MoveModule(project, old_python_file).get_changes(
            #     new_package_resource
            # )
            # project.do(change)

            # change = Restructure(
            #     project, old_package_name + "${name}", new_package_name + "${name}"
            # ).get_changes()
            # logger.info("change = %s", change)
            # project.do(change)

            Rename(
                project,
            )

            # logger.info("x = %s", python_module.absolute_name)

            # new_path_relative = Path(*prefix.split(".")) / old_path_relative
            # new_path = project_path / new_path_relative
            # logger.info("moving %s to %s", old_path, new_path)
            # new_path.parent.mkdir(parents=True, exist_ok=True)
            # # change = MoveResource(python_file, f"{new_path_relative}")
            # # project.do(change)

            # python_module = project.get_pymodule(python_file)
            # logger.info("python_module  = %s", python_module)

        # Rename(project)

        # logger.info("project.get_python_files()  = %s", project.get_python_files())
        # logger.info("project.get_source_folders()  = %s", project.get_source_folders())
        # # logger.info(
        # #     "project.get_python_path_folders()  = %s", project.get_python_path_folders()
        # # )

        # python_file: roperesources.File
        # for python_file in project.get_python_files():
        #     logger.info("python_file  = %s", python_file)
        #     python_module = project.get_pymodule(python_file)
        #     logger.info("python_module  = %s", python_module)


def main() -> None:
    setup_logging()
    Application().run(sys.argv[1:])


def setup_logging() -> None:
    logging.basicConfig(
        level=os.environ.get("PYLOGGING_LEVEL", logging.INFO),
        stream=sys.stderr,
        datefmt="%Y-%m-%dT%H:%M:%S",
        format=(
            "%(asctime)s.%(msecs)03d %(process)d %(thread)d %(levelno)03d:%(levelname)-8s "
            "%(name)-12s %(module)s:%(lineno)s:%(funcName)s %(message)s"
        ),
    )


if __name__ == "__main__":
    main()
