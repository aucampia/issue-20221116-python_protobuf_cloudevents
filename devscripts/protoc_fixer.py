#!/usr/bin/env python3
import argparse
import logging
import os
import sys
from dataclasses import dataclass, field
from typing import List

import rope.base.resources as roperesources
from rope.base.project import Project
from rope.refactor.move import MoveResource
from rope.refactor.rename import Rename

logger = logging.getLogger(__name__)


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
        project = Project(target)
        logger.info("project  = %s", project)

        python_files: List[roperesources.File] = [
            *project.get_python_files(),
        ]

        resources: List[roperesources.Resource] = [
            *project.get_python_files(),
            # *project.get_source_folders(),
        ]

        logger.info("resources = %s", resources)

        for python_file in python_files:
            logger.info("python_file  = %s", python_file)
            MoveResource(
                python_file,
                os.path.join(*prefix.split("."), python_file.name)
                # roperesources.File(
                #     project,
                #     os.path.join(*prefix.split("."), python_file.name),
                # ),
            )

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
