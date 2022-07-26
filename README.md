# Juju Introspect Operator

This simple operator is used to manage the `juju-introspect` tool using systemd.

The charm installs a systemd unit that starts `juju-introspect`, listening on port 6000. It
provides a relation that allows it to be scraped by the [Parca operator](https://charmhub.io/parca).

## Usage

This operator is designed to be deployed to existing controller machines such that the Juju
controller can be profiled/monitored by external observability tools.

You can deploy the operator as such:

```shell
# Bootstrap a new Juju controller on LXD
$ juju bootstrap localhost lxd
# Switch to the controller model
$ juju switch controller
# Deploy the charm to the controller machine
$ juju deploy --to=0 juju-introspect --channel edge
```
