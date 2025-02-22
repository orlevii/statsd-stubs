from datetime import timedelta

from statsd import StatsClient, UnixSocketStatsClient


def test_client_types() -> None:
    client = StatsClient(
        host="my-host",
        port=1234,
        prefix="my_prefix",
    )
    client.incr(stat="incr", count=10, rate=0.1)
    client.decr(stat="incr", count=2, rate=1.0)
    client.timing(stat="timing", delta=10.5, rate=0.2)
    client.timing(stat="timing", delta=timedelta(seconds=2))
    client.set("set", 2, 1)


def test_timer_types() -> None:
    client = StatsClient()
    with client.timer("timer") as t:

        @t
        def test_timer_decorator() -> None:
            pass


def test_pipeline_types() -> None:
    client = StatsClient()
    with client.pipeline() as pipeline:
        pipeline.incr("stats")


def test_unix_socket_client_types() -> None:
    statsd = UnixSocketStatsClient(socket_path="/var/run/stats.sock")
    statsd.incr("stat")
