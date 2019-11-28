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

First thing to do is to make sure your system has a supported version of Python for pyATS, you can find out your installed version of python by running the `python --version`

Current versions of Python with support for pyATS on Linux & MacOS systems. Windows platforms are currently not supported:

- Python 3.5.x
- Python 3.6.x
- Python 3.7.x

Installing the pyATS library couldn't be simpiler, all you need to do is run the command `pip install pyats[library]` which should carry out the needed installation process.

Verify the installation:

> $ pip list | grep pyats
> $ pip list | grep genie 

When running pyATS its strongly recommended that it is done so from a virtual environment, a Virtual Environment, acts as isolated working copy of Python which allows you to work on a specific project without worry of affecting other projects. You can run pyATS outside one but its recommended that you use this method, as its super easy. To built your own virtual environment do the following:

> $ mkdir test && cd test

> $ python3 -m venv .

> $ source bin/activate .

Congratulations, you've sucessfully installed pyATS and set up your virtual environment. You're good to get started!

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

## Exercise 1 (Crawl) - Simple device test and validation with GenieCLI

As touched upon earlier, the simpliest way to get started with the pyATS tools is by using the Genie CLI command line tools.

### Step 1 - Builing your testbed file

The first thing anyone using pyATS needs to do is define a testbed file to outline what the topology is and how pyATS can connect to it. I've included an example testbed file with just one device to connect to the sandbox environment outlined. You can find it within the `testbed` folder. I've also included a few extra ones in there so you can get the hang of the yaml format. If you're wishing to run this on another environment feel free to tweak the files included to suit your environment.

IMPORTANT:

### Step 2 - Creating a baseline of a device

Now we have our testbed file all thats left to do is run our test. When you you use the command `genie help` you'll notice that genie has a couple of different operating modes, in this lab we'll primarily focus on the `learn` and `diff` modes. 

To take a baseline of our test environment use the below command which specifies we're looking to learn all features from the device, the testbed-file we need to use and where the test report will be outputed to.

`genie learn all --testbed-file testbed-sandbox.yaml --output baseline/test-sandbox`

![](https://github.com/sttrayno/pyATS-Lab-Guide/blob/master/images/pyats-baseline.gif)

Lets log onto our router and make some changes, in this instance we have configured OSPF to advertise the network 1.1.1.0/24. As we did last time we're going to run the test again, learning all features of the router, the only difference this tims is specifying a different output path for our latest test. 

![](https://github.com/sttrayno/pyATS-Lab-Guide/blob/master/images/pyats-config.gif)

`genie learn all --testbed-file testbed-sandbox.yaml --output latest/test-sandbox`

![](https://github.com/sttrayno/pyATS-Lab-Guide/blob/master/images/pyats-latest.gif)

Now we've captured both reports 

`genie diff baseline/test-sandbox test-sandbox --output diff_dir`

![](https://github.com/sttrayno/pyATS-Lab-Guide/blob/master/images/pyats-diff.gif)

### Step 3 - Examine your output

As we can see from the bash output above, the Genie diff command takes all the outputs from our various tests (approx 30 at the time of writing) and compares the outputs. As would be expected most of these are identical except from the config (which we changed back in step 2 and the OSPF config, which is to be expected considering we configured OSPF. 

The genie tool also creates a file in which we can see what the exact differences are from the files, therefore making it easy for us to understand that OSPF has been configured on the device since our last known baseline.

![](https://github.com/sttrayno/pyATS-Lab-Guide/blob/master/images/pyats-diff-explore.gif)


## Exercise 2 (Walk) - Automated test plans with the Robot framework

TBC

## Exercise 3 (Run) - Building your own test plans with raw Python

TBC

