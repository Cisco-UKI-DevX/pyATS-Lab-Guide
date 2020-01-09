> This guide is based from the NetDevOps Live S2 episode 6 pyATS/Genie demos by Simon Hart, credit to Simon for his fantastic content
> https://www.youtube.com/watch?v=LbxfHWrujHc

*This lab is part of a series of guides from the [Network Automation and Tooling workshop series](https://github.com/sttrayno/Network-Automation-Tooling)*

# Network test and validation with pyATS - Crawl / Walk / Run

Network testing and validation tools is a massively growing area within network and infrastructure engineering. Engineers and architects are looking for tools that answer questions such as:

- What has changed on the network config?
- Is my data plane operating the way that I would expect?
- Can I compare my control plane and data plane against a known good baseline?
- Can I automate this process across my entire estate?

Originally developed for internal Cisco engineering use, pyATS/Genie is at the core of Cisco's Test Automation Solution. Some interesting numbers on pyATS current use within Cisco:

- Used by 3000+ internal Cisco developers
- Over 2,000,000 test runs on a monthly basis
 
![](https://pubhub.devnetcloud.com/media/pyats-genie-docs/docs/imgs/layers.png#developer.cisco.com)

Before we get hands on there are a couple of core concepts that we need to explain as you might have noticed we've been using pyATS and Genie almost interchangeably, we need to explain these tools clearly.

### pyATS

pyATS is the test framework foundation for this ecosystem. It specializes in data-driven and reusable testing, and is engineered for Agile, rapid development iterations.

This powerful, highly-pluggable Python framework is designed to enable developers start with small, simple and linear test cases, then scale towards large, complex and asynchronous test suites.

### Genie

The simplest way to use pyATS

Genie redefines how network engineers perform testing and scripting. It comes out of the box with all the bits needed for Network Test Automation, meaning that network engineers and NetDevOps can be productive day one with Genie's readily available, holistic and model-driven libraries.

Genie builds on pyATS to provide:

- a simple command line interface (no Python knowledge needed)
- a pool of reusable test cases
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

As you go deeper and deeper into pyATS and Genie you'll begin to realise how powerful a tool it can be. If you'd like to go further than this guide please see the DevNet webpage on pyATS which is a fantastic resource and should be anyone who's trying to get hands on first port of call. https://developer.cisco.com/docs/pyats/#!pyats-genie-on-devnet/pyats-genie-on-devnet

## Exercise 0 - Installing pyATS and Genie

First thing to do is to make sure your system has a supported version of Python for pyATS, you can find out your installed version by running the `python --version`

Current versions of Python with support for pyATS on Linux & MacOS systems. Windows platforms are currently not supported:

- Python 3.5.x
- Python 3.6.x
- Python 3.7.x

Installing the pyATS library couldn't be simpler, all you need to do is run the command `pip install pyats[library]` which should carry out the needed installation process.

Verify the installation:

```bash
pip list | grep pyats
```

```bash
pip list | grep genie
```

When running pyATS it is strongly recommended that it is done so from a virtual environment. A Virtual Environment acts as isolated working copy of Python which allows you to work on a specific project without worry of affecting other projects. While you can run pyATS outside a virtual environment, it is strongly recommended that you use this as it creates an isolated environment for our exercise and allows us to create it's can have its own dependencies, regardless of what other packages are installed on the system.

To get started with your own virtual environment, just do the following:

```bash
mkdir test && cd test
```

```bash
python3 -m venv .
```

```bash
source bin/activate .
```

Congratulations, you've successfully installed pyATS and set up your virtual environment. You're good to get started!

### Prerequisites

Before we get started with network testing and validation we'll need a network environment to run our tests on. One of the easiest test environments you'll find is on the Cisco DevNet Sandbox which has multiple options. These are completely free and can in some cases be accessed within seconds. https://developer.cisco.com/docs/sandbox/#!overview/all-networking-sandboxes

Most popular sandboxes include:

- IOS-XE (CSR) - Always-On
- IOS-CR - Always-On
- Multi IOS test environment (VIRL based) - Reservation required
- Cisco SD-WAN environment - Always-On
- Cisco DNA-C environment - Always-On

Please note you are free to use this with your own hardware or test environment. However the commands in this lab guide have been tested for the sandboxes they correspond to. For this lab guide we will be using the reservable IOS XE on CSR Recommended Code Sandbox which can be found on the Sandbox catalogue https://devnetsandbox.cisco.com/RM/Topology

![](https://github.com/sttrayno/Ansible-Lab-Guide/blob/master/images/sandbox-screen.png)

## Exercise 1 (Crawl) - Simple device test and validation with GenieCLI

As touched upon earlier, the simplest way to get started with the pyATS tools is by using the Genie CLI command line tools.

### Step 1 - Building your testbed file

The first thing anyone using pyATS needs to do is define a testbed file to outline what the topology is and how pyATS can connect to it. There is an example testbed file included with just one device to connect to the sandbox environment outlined. You can find it within the `testbed` folder. There are also a few extra ones in there so you can get the hang of the YAML format. If you want to run this on another environment feel free to tweak the files included to suit your environment.

IMPORTANT: When building your inventory file ensure the alias value and hostname of your device match exactly. Trust me that will save you hours of troubleshooting. :)

### Step 2 - Creating a baseline of a device

Now we have our testbed file all thats left to do is run our test. When you you use the command `genie help` you will notice that genie has a couple of different operating modes. In this lab we will primarily focus on the `learn` and `diff` modes.

To take a baseline of our test environment use the below command which specifies we're looking to learn all features from the device, the testbed-file we need to use and where the test report file will be saved.

```bash
genie learn all --testbed-file testbed-sandbox.yaml --output baseline/test-sandbox
```

![](./images/pyats-baseline.gif)

Lets log onto our router and make some changes, in this instance we have configured OSPF to advertise the network 1.1.1.0/24. As we did last time we are going to run the test again, learning all features of the router, the only difference this time is specifying a different output path for our latest test.

![](./images/pyats-config.gif)

```bash
genie learn all --testbed-file testbed-sandbox.yaml --output latest/test-sandbox
```

![](./images/pyats-latest.gif)

Now we have captured both reports

```bash
genie diff baseline/test-sandbox test-sandbox --output diff_dir
```

![](./images/pyats-diff.gif)

### Step 3 - Examine your output

As we can see from the bash output above, the Genie diff command takes all the outputs from our various tests (approx 30 at the time of writing) and compares the outputs. As would be expected most of these are identical except from the config (which we changed back in step 2) and the OSPF config, which is to be expected... considering we configured OSPF.

The genie tool also creates a file in which we can see what the exact differences are from the files, therefore making it easy for us to understand that OSPF has been configured on the device since our last known baseline.

![](./images/pyats-diff-explore.gif)

## Exercise 2 (Walk) - Automated test plans with the Robot framework

### Step 0 - Make sure Robot framework is installed

As you can see the diff functionality can save a large amount of manual work that would normally be required to compare configs and outputs from a device. What we'll explore in this exercise is how we can look to automate a complete test with the Robot framework of pyATS and produce an output that can viewed after the test to examine our scenario.

First we'll need to install the robot framework add-on, to do this simply enter the command `pip install pyats[robot]` which will go off an install the necessary components.

Verify the installation:

```bash
pip list | grep robot
```

### Step 1 - Running our initial testcase

The robot framework allows us to incorporate a bit more automation within our pyATS tests whilst abstracting away from some of the underlying Python which can be a barrier to entry for getting started with pyATS as we currently are. In this exercise we'll explore two Robot test plans which will automate the testing and reporting of our testbed environments.

Lets take a further look at the test cases now. First open up the file robot_initial_snapshot.robot and you should see something similar to the below.

![](./images/robot-test-initial.png)

The first section is our settings, leave this as is for now as we only need to import our libraries

The second section defines the variables, in this case we're only using the variable 'testbed' which is set as the path to our testbed file we used in Exercise 1.

The next section is where it begins to get interesting, as you can see we have 2 tests that are being run, the first being a simple connection to the device being established.

The second test is we're learning from the device with the profile, as we can see from the input we're looking to profile the config, interface, platform, OSPF, arp, routing, vrf and VLAN. These could be customized depending on what you're looking to learn. Finally you'll see this output of this profile being stored into the directory ./good_snapshot

```bash
Robot --outputdir run robot_initial_snapshot.robot
```

![](./images/robot-initial.gif)

Run the test by using the command above and observe, we can see from the image below that the robot framework runs the two tests defined within our test case first to connect to device then to profile the device for the items specified. You should see both tests pass successfully and the directory populated with a number of files. The ones we're most interested in here are the ones within the run folder as shown below. The most important file is the report.html which if you open will show a webpage report from the test we just ran.

```bash
Output: /Users/sttrayno/pyats/robot_initial_snapshot/run/output.xml
```

```bash
Log: /Users/sttrayno/pyats/robot_initial_snapshot/run/log.html
```

```bash
Report: /Users/sttrayno/pyats/robot_initial_snapshot/run/report.html
```

![](./images/robot-test-initial-gui.png)

### Step 2 - Running our comparison test case

Now we've ran our first basic test case we've got to grips with how the robot framework works and what kind of output it produces, now it's time to start using it in anger. First off lets take a look at the `robot_compare_snapshot.robot` file that's in our test case directory. As you you can see its remarkably similar to the initial test case, it imports the libraries, declares our variables, has a test outlined to connected to device and another to profile the device. However theres one slight difference, as you can see at the bottom of the test case we have another test outlined called 'Compare snapshots'.

Quite simply the purpose of this is to create a comparison of our existing snapshot and the most modern one and look for differences in the outputs collected, should no differences be found the test will pass and if a difference is found the test will fail. Simple enough!

As we're looking to compare from our baseline to our most recent snapshot it might be a good idea to change some config on the device, configure something on the device (OSPF is my normal go to).

![](./images/compare-test.png)

Now we understand what the test case is doing lets run the profile. Use the command below, this time passing the compare test case we just looked at.

```bash
Robot --outputdir run robot_compare_snapshot.robot`
```

![](./images/robot-compare.gif)

As you can see the robot framework runs the tests in order, first connecting to the device and profiling our device for the features specified. This time however we should see the test fail, Don't panic, this should be expected as when running the comparison test pyATS will encounter a difference in the configuration.

Once again, examine the "report.html" within the run directory. You should see an output similar to the below:

![](./images/robot-compare-gui.gif)

If you have not made any config changes on the device this test would run successfully and we'd get another output similar to the report in Step 1.

Congratulations, you should now have a grasp of the very basics of the Robot framework.

## Exercise 3 (Run) - Building your own test plans with raw Python

TBC
