# Network test and validation with pyATS - Crawl / Walk / Run

Network testing and validation tools is a massively growing area within network and infrastructure engineering, engineers and architects are looking for tools that answer questions 

- What has changed on the network config?
- Is my dataplane operating the way that I would expect?
- Can I compare my control plane and dataplane against a known good baseline?
- Can I automate this process across my entire estate

Originally developed for internal Cisco engineering use, pyATS / Genie is at the core of Cisco's Test Automation Solution. Some interesting numbers on pyATS current use within Cisco:

- Used by 3000+ internal Cisco developers
- Over 2,000,000 test runs on a monthly basis

![](https://pubhub.devnetcloud.com/media/pyats-genie-docs/docs/imgs/layers.png#developer.cisco.com)

Before we get hands on theres a couple of core concepts we need to explain

### pyATS

pyATS is the test framework foundation for this ecosystem. It specializes in data-driven and reusable testing, and is engineered for Agile, rapid development iterations.
This powerful, highly-pluggable Python framework is designed to enable developers start with small, simple and linear test cases, then scale towards large, complex and asynchronous test suites.

### Genie

The simplest way to use pyATS
Genie redefines how network engineers perform testing and scripting. It comes out of the box with all the bits needed for Network Test Automation. Meaning that network engineers and NetDevOps can be productive day one with Genie's readily available, holistic and model-driven libraries.
Genie builds on pyATS to provide
a simple command line interface (no Python knowledge needed)
a pool of reusable testcases
a Pythonic library for more complex scripting

### Agnostic Infrastructure

pyATS | Genie is built from the ground up to be an agnostic infrastructure. All OS/Platform and management protocol support is defined and injected through plugins, library implementations & extensions.
Out of the box, it comes with libraries that support:
Cisco IOS
Cisco IOXE
Cisco IOSXR
Cisco NXOS
Cisco ASA
... etc
and allows the device connections via CLI, NETCONF, or RESTCONF.
Additional support for 3rd-party platforms and other management protocols can be easily achieved through plugins and library extensions.

