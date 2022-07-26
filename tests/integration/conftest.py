# Copyright 2021 Canonical Ltd.
# See LICENSE file for licensing details.
import logging

from pytest import fixture
from pytest_operator.plugin import OpsTest

logger = logging.getLogger(__name__)


@fixture(scope="module")
async def juju_introspect_charm(ops_test: OpsTest):
    """Juju introspect charm used for integration testing."""
    charm = await ops_test.build_charm(".")
    return charm
