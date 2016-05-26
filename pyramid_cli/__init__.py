from typing import Union
import zope.interface
import click
import functools

from pyramid.config import Configurator
from pyramid.registry import Registry


class ICli(zope.interface.Interface):
    pass


@zope.interface.implementer(ICli)
class Cli(click.Group):

    def __init__(self, registry: Registry, **kwargs):
        super().__init__(**kwargs)
        self._registry = registry

    @property
    def registry(self) -> Registry:
        return self._registry


def add_command(config: Configurator, command: Union[str, click.Command]):
    """
    Add command.

    :param config: Configurator
    :param command: Command dotted path or Command object
    :param name:  Command name
    """
    command = config.maybe_dotted(command)

    cli = config.registry.getUtility(ICli)  # type: Cli
    cli.add_command(command)


def includeme(config: Configurator):

    registry = config.registry  # type: Registry

    cli = Cli(registry=registry)

    # Add `add_command` directive
    config.add_directive('add_command', add_command)

    # Register CLI component
    registry.registerUtility(cli, ICli)
    commands = registry.settings.get('cli.commands', [])

    # Register commands from settings
    for command in commands:
        config.add_command(command)


def pass_registry(func):
    """
    Pass registry into command.

    :param func: Command function
    :return: Wrapped command
    """

    @click.pass_context
    def decorator(ctx, *args, **kwargs):
        registry = ctx.parent.command.registry
        return ctx.invoke(func, registry, *args, **kwargs)
    return functools.update_wrapper(decorator, func)
