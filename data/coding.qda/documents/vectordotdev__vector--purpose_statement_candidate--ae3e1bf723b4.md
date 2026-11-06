[![Nightly](https://github.com/vectordotdev/vector/actions/workflows/nightly.yml/badge.svg)](https://github.com/vectordotdev/vector/actions/workflows/nightly.yml) [![Integration/E2E Test Suite](https://github.com/vectordotdev/vector/actions/workflows/integration.yml/badge.svg)](https://github.com/vectordotdev/vector/actions/workflows/integration.yml) [![Component Features](https://github.com/vectordotdev/vector/actions/workflows/component_features.yml/badge.svg)](https://github.com/vectordotdev/vector/actions/workflows/component_features.yml)

![Vector](website/static/img/diagram.svg)

**[Quickstart](https://vector.dev/docs/setup/quickstart/)  •   [Docs](https://vector.dev/docs/)  •   [Guides](https://vector.dev/guides/)  •   [Integrations](https://vector.dev/components/)  •   [Chat](https://chat.vector.dev)  •   [Download](https://vector.dev/releases/latest/download/)  •   [Rust Crate Docs](https://rust-doc.vector.dev/)**

## What is Vector?

Vector is a high-performance, end-to-end (agent & aggregator) observability data pipeline that puts you in control of your observability data. [Collect](https://vector.dev/docs/reference/configuration/sources/), [transform](https://vector.dev/docs/reference/configuration/transforms/), and [route](https://vector.dev/docs/reference/configuration/sinks/) all your logs and metrics to any vendors you want today and any other vendors you may want tomorrow. Vector enables dramatic cost reduction, novel data enrichment, and data security where you need it, not where it is most convenient for your vendors. Additionally, it is open source and up to 10x faster than every alternative in the space.

To get started, follow our [**quickstart guide**](https://vector.dev/docs/setup/quickstart/) or [**install Vector**](https://vector.dev/docs/setup/installation/).

Vector is maintained by Datadog's [Community Open Source Engineering team](https://opensource.datadoghq.com/about/#the-community-open-source-engineering-team).

### Principles

- **Reliable** - Built in [Rust](https://www.rust-lang.org/), Vector's primary design goal is reliability.
- **End-to-end** - Deploys as an [agent](https://vector.dev/docs/setup/deployment/roles/#agent) or [aggregator](https://vector.dev/docs/setup/deployment/roles/#aggregator). Vector is a complete platform.
- **Unified** - [Logs](https://vector.dev/docs/architecture/data-model/log/), [metrics](https://vector.dev/docs/architecture/data-model/metric/) (beta), and traces (coming soon). One tool for all of your data.

### Use cases

- Reduce total observability costs.
- Transition vendors without disrupting workflows.
- Enhance data quality and improve insights.
- Consolidate agents and eliminate agent fatigue.
- Improve overall observability performance and reliability.

### Community

- Vector is relied on by startups and enterprises like **Atlassian**, **T-Mobile**, **Comcast**, **Zendesk**, **Discord**, **Fastly**, **CVS**, **Trivago**, **Tuple**, **Douban**, **Visa**, **Mambu**, **Blockfi**, **Claranet**, **Instacart**, **Forcepoint**, and [many more](https://github.com/vectordotdev/vector/issues/790).
- Vector is **downloaded over 100,000 times per day**.
- Vector's largest user **processes over 500TB daily**.
- Vector has **over 500 contributors** and growing.

## Documentation

All user documentation is available at **[vector.dev/docs](https://vector.dev/docs)**.

Other Resources:

- [**Vector Calendar**](https://calendar.vector.dev)
- **Policies**:
  - [**Code of Conduct**](https://github.com/vectordotdev/vector/blob/master/CODE_OF_CONDUCT.md)
  - [**Contributing**](https://github.com/vectordotdev/vector/blob/master/CONTRIBUTING.md)
  - [**Privacy**](https://github.com/vectordotdev/vector/blob/master/PRIVACY.md)
  - [**Releases**](https://github.com/vectordotdev/vector/blob/master/RELEASES.md)
  - [**Versioning**](https://github.com/vectordotdev/vector/blob/master/VERSIONING.md)
  - [**Security**](https://github.com/vectordotdev/vector/security/policy)

## Comparisons

### Performance

The following performance tests demonstrate baseline performance between common protocols with the exception of the Regex Parsing test.

| Test | Vector | Filebeat | FluentBit | FluentD | Logstash | SplunkUF | SplunkHF |
|----|----|----|----|----|----|----|----|
| [TCP to Blackhole](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/tcp_to_blackhole_performance) | ***86mib/s*** | n/a | 64.4mib/s | 27.7mib/s | 40.6mib/s | n/a | n/a |
| [File to TCP](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_to_tcp_performance) | ***76.7mib/s*** | 7.8mib/s | 35mib/s | 26.1mib/s | 3.1mib/s | 40.1mib/s | 39mib/s |
| [Regex Parsing](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/regex_parsing_performance) | 13.2mib/s | n/a | ***20.5mib/s*** | 2.6mib/s | 4.6mib/s | n/a | 7.8mib/s |
| [TCP to HTTP](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/tcp_to_http_performance) | ***26.7mib/s*** | n/a | 19.6mib/s | \<1mib/s | 2.7mib/s | n/a | n/a |
| [TCP to TCP](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/tcp_to_tcp_performance) | 69.9mib/s | 5mib/s | 67.1mib/s | 3.9mib/s | 10mib/s | ***70.4mib/s*** | 7.6mib/s |

To learn more about our performance tests, please see the [Vector test harness](https://github.com/vectordotdev/vector-test-harness/).

### Correctness

The following correctness tests are not exhaustive, but they demonstrate fundamental differences in quality and attention to detail:

| Test | Vector | Filebeat | FluentBit | FluentD | Logstash | Splunk UF | Splunk HF |
|----|----|----|----|----|----|----|----|
| [Disk Buffer Persistence](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/disk_buffer_persistence_correctness) | **✓** | ✓ |  |  | ⚠ | ✓ | ✓ |
| [File Rotate (create)](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_rotate_create_correctness) | **✓** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [File Rotate (copytruncate)](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_rotate_truncate_correctness) | **✓** |  |  |  |  | ✓ | ✓ |
| [File Truncation](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_truncate_correctness) | **✓** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [Process (SIGHUP)](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/sighup_correctness) | **✓** |  |  |  | ⚠ | ✓ | ✓ |
| [JSON (wrapped)](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/wrapped_json_correctness) | **✓** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

To learn more about our correctness tests, please see the [Vector test harness](https://github.com/vectordotdev/vector-test-harness/).

### Features

Vector is an end-to-end, unified, open data platform.

|  | **Vector** | Beats | Fluentbit | Fluentd | Logstash | Splunk UF | Splunk HF | Telegraf |
|----|----|----|----|----|----|----|----|----|
| **End-to-end** | **✓** |  |  |  |  |  |  | ✓ |
| Agent | **✓** | ✓ | ✓ |  |  | ✓ |  | ✓ |
| Aggregator | **✓** |  |  | ✓ | ✓ |  | ✓ | ✓ |
| **Unified** | **✓** |  |  |  |  |  |  | ✓ |
| Logs | **✓** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrics | **✓** | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ✓ |
| Traces | 🚧 |  |  |  |  |  |  |  |
| **Open** | **✓** |  | ✓ | ✓ |  |  |  | ✓ |
| Open-source | **✓** | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |
| Vendor-neutral | **✓** |  | ✓ | ✓ |  |  |  | ✓ |
| **Reliability** | **✓** |  |  |  |  |  |  |  |
| Memory-safe | **✓** |  |  |  |  |  |  | ✓ |
| Delivery guarantees | **✓** |  |  |  |  | ✓ | ✓ |  |
| Multi-core | **✓** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

⚠ = Not interoperable, metrics are represented as structured logs

------------------------------------------------------------------------

Developed with ❤️ by **[Datadog](https://datadoghq.com)** - [Security Policy](https://github.com/vectordotdev/vector/security/policy) - [Privacy Policy](https://github.com/vectordotdev/vector/blob/master/PRIVACY.md)
