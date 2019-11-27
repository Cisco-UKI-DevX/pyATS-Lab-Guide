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

Before we get hands on theres a couple of core concepts we need to explain as you might have noticed we've been using pyATS and Genie almost interchangably, we need to explain these tools clearly

### pyATS

pyATS is the test framework foundation for this ecosystem. It specializes in data-driven and reusable testing, and is engineered for Agile, rapid development iterations.

This powerful, highly-pluggable Python framework is designed to enable developers start with small, simple and linear test cases, then scale towards large, complex and asynchronous test suites.

### Genie

The simplest way to use pyATS

Genie redefines how network engineers perform testing and scripting. It comes out of the box with all the bits needed for Network Test Automation. Meaning that network engineers and NetDevOps can be productive day one with Genie's readily available, holistic and model-driven libraries.
Genie builds on pyATS to provide
- a simple command line interface (no Python knowledge needed)
- a pool of reusable testcases
- a Pythonic library for more complex scripting

For this lab we'll start using with using Genie and getting comfortable then move onto the flexibility that the pyATS framework offers.

### Agnostic Infrastructure

pyATS | Genie is built from the ground up to be an agnostic infrastructure. All OS/Platform and management protocol support is defined and injected through plugins, library implementations & extensions.
Out of the box, it comes with libraries that support:

- Cisco IOS
- Cisco IOXE
- Cisco IOSXR
- Cisco NXOS
- Cisco ASA
... etc
and allows the device connections via CLI, NETCONF, or RESTCONF.
Additional support for 3rd-party platforms and other management protocols can be easily achieved through plugins and library extensions.

As you go deeper and deeper into pyATS and Genie you'll begin to realise how powerful a tool it can be, if you'd like to go further than this guide please see the DevNet microsite on pyATS which is a fantastic resource and should be anyone who's trying to get hands on first port of call. https://developer.cisco.com/docs/pyats/#!pyats-genie-on-devnet/pyats-genie-on-devnet

## Exercise 0 - Installing pyATS and Genie



### Prequisites

Before we get started with network testing and validation we'll need a to run our tests on. One of the easiest test environments you'll find is on the Cisco DevNet Sandbox which has multiple options. These are completely free and can in some cases be accessed within seconds. https://developer.cisco.com/docs/sandbox/#!overview/all-networking-sandboxes

Most popular sandboxes include:

- IOS-XE (CSR) - Always-On
- IOS-CR - Always-On
- Multi IOS test environment (VIRL based) - Reservation required
- Cisco SD-WAN environment - Always-On
- Cisco DNA-C environment - Always-On

Please note you are free to use this with your own hardware or test environment. However the commands in this lab guide have been tested for the sandboxes they correspond to. For this lab guide we will be using the reservable IOS XE on CSR Recommended Code Sandbox which can be found on the Sandbox catalogue https://devnetsandbox.cisco.com/RM/Topology

![](https://github.com/sttrayno/Ansible-Lab-Guide/blob/master/images/sandbox-screen.png)
