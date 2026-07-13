### 🔹 Lesson #10 | [Beginner] | Networking

### Concept: Configure PortFast and BPDU Guard on Access Ports

Greetings, future network engineers! As your Enterprise Edge Port Convergence & BPDU Protection Architect, I welcome you back to the Cisco IOS command line. In our previous lessons, we segmented our network using VLANs (Lessons 6 & 7), established high-speed 802.1Q trunk paths (Lesson 8), and optimized our Layer 2 topology by deploying Rapid PVST+ (Lesson 9).

Today, we focus on the network's access layer edge. When an end device like a computer connects to a switch port, Spanning Tree Protocol checks the port to ensure it won't cause a network loop. Even with Rapid PVST+, this check causes a slight delay before data can flow. This lesson will show you how to use **PortFast** to bypass this wait time for safe user ports. We will also implement **BPDU Guard** to protect our network from unauthorized or accidental switches being plugged into these user ports.

---

### 💡 Analogy

Imagine an access port is a **secure security checkpoint gate** at the entrance of a corporate building.

* By default, every time an employee arrives at the gate, the guard runs a full background check that takes up to 30 seconds before letting them inside. Implementing **PortFast** is like issuing an **Express Badge** to trusted regular employees (`HQ-PC1`, `BR-PC3`, etc.). The moment they scan their badge, the gate opens instantly, avoiding any line.
* However, giving out Express Badges introduces a security risk: what if an employee brings a rogue turnstile gate from home and connects it to the company's security system? **BPDU Guard** acts like an **automated sensor alarm**. If the gate detects an unauthorized network device trying to send management messages (**BPDUs**), it instantly shuts down and locks the gate (**error-disabled**), setting off an alarm for the administrator.

---

### Step 1️⃣: Access the HQ-S1 Switch via the CLI and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: To apply edge port optimization and port security across our headquarters infrastructure, we must start by logging into `HQ-S1`. We will pass through the login banners configured in Lesson 5, authenticate using the local administrative credentials from Lesson 3, and elevate our permissions to enter global configuration mode.
* **Commands to execute**:
```bash
HQ-S1> enable
Password: class
HQ-S1# configure terminal
HQ-S1(config)#

```


* **Verification commands**: Observe the terminal prompt transition to confirm you have entered global configuration mode.
```bash
# The prompt must read exactly:
HQ-S1(config)#

```


* **🚨 Common error note or Troubleshooting tip**: If the switch rejects your credentials, verify that you are connected to the switch console prompt of `HQ-S1` and not one of the upstream routers (`HQ-R1`).
* **🎯 Mini challenge**: What command allows you to view the currently configured hostname to ensure you are on the right device? *(Answer: Look at the prompt name or run `show running-config | include hostname`)*

---

### Step 2️⃣: Select the Access Ports Using Interface Range on HQ-S1

* **Mini-Lesson / Explanation**: Based on our accumulated topology context from Lesson 1 and Lesson 6, `HQ-S1` connects to user workstations via ports `FastEthernet0/1` (VLAN 10 Engineering) and `FastEthernet0/6` (VLAN 20 Sales). Instead of configuring each port one by one, we use the `interface range` command to select and configure both interfaces at the same time.
* **Commands to execute**:
```bash
HQ-S1(config)# interface range FastEthernet0/1, FastEthernet0/6
HQ-S1(config-if-range)#

```


* **Verification commands**: Verify that your prompt changes to reflect the interface range mode context.
```bash
# The prompt must update to:
HQ-S1(config-if-range)#

```


* **🚨 Common error note or Troubleshooting tip**: When listing separate ports with a comma, you must include a space after the comma on older Cisco IOS versions. Typing `FastEthernet0/1,FastEthernet0/6` without the space may result in an interface parsing error.
* **🎯 Mini challenge**: If you wanted to select a consecutive range of interfaces from 1 through 5, how would you write the command? *(Answer: `interface range FastEthernet0/1 - 5`)*

---

### Step 3️⃣: Enable Spanning-Tree PortFast on HQ-S1

* **Mini-Lesson / Explanation**: The `spanning-tree portfast` command instructs the switch that these interfaces are explicitly connected to end host devices rather than other switches. This allows the ports to bypass the listening and learning states, transitioning immediately to the forwarding state so users can connect to the network without waiting.
* **Commands to execute**:
```bash
HQ-S1(config-if-range)# spanning-tree portfast

```


* **Verification commands**: Look for the informational warning text printed across the console window.
```bash
# The switch will display an output message:
%Warning: portfast should only be enabled on ports connected to a single host.
Connecting hubs, concentrators, switches, bridges, etc... to this interface
when portfast is enabled can cause temporary bridging loops.

```


* **🚨 Common error note or Troubleshooting tip**: Never enable PortFast on switch-to-switch trunk ports, like `GigabitEthernet0/1` configured in Lesson 8. Doing so bypasses loop-prevention checks and can cause a network loop that crashes your connectivity.
* **🎯 Mini challenge**: What command can you run in global configuration mode to enable PortFast automatically on all current and future access ports? *(Answer: `spanning-tree portfast default`)*

---

### Step 4️⃣: Enable Spanning-Tree BPDU Guard on HQ-S1

* **Mini-Lesson / Explanation**: Because PortFast bypasses traditional loop-prevention checks, we need a security mechanism to protect the edge of our network. We use the `spanning-tree bpduguard enable` command to monitor the interface. If an unauthorized switch is plugged into this port and sends a Bridge Protocol Data Unit (BPDU), `HQ-S1` will instantly shut the port down to protect the network.
* **Commands to execute**:
```bash
HQ-S1(config-if-range)# spanning-tree bpduguard enable

```


* **Verification commands**: Run a check on the running interface configuration configuration to confirm both commands are applied.
```bash
HQ-S1(config-if-range)# do show running-config interface FastEthernet0/1
# Expected output:
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable

```


* **🚨 Common error note or Troubleshooting tip**: If a port gets shut down by BPDU Guard, it enters an `err-disabled` state. To turn the port back on after removing the unauthorized device, you must enter the interface mode and manually type `shutdown` followed by `no shutdown`.
* **🎯 Mini challenge**: What global command enables BPDU Guard automatically on all PortFast-enabled ports? *(Answer: `spanning-tree portfast bpduguard default`)*

---

### Step 5️⃣: Verify PortFast and BPDU Guard Configuration Details on HQ-S1

* **Mini-Lesson / Explanation**: To confirm our settings are working properly, we use the `show spanning-tree interface [type/number] detail` command. This detailed check allows us to verify that PortFast is active and BPDU Guard is monitoring the interface.
* **Commands to execute**:
```bash
HQ-S1(config-if-range)# end
HQ-S1# show spanning-tree interface FastEthernet0/1 detail

```


* **Verification commands**: Scan the detailed terminal output block to confirm the feature status flags.
```bash
# Verify that the output text contains these specific parameters:
Port 1 (FastEthernet0/1) of VLAN0010 is forwarding
Port info             VLAN status designated
Link type is point-to-point, The port is in the portfast mode
Bpdu guard is enabled

```


* **🚨 Common error note or Troubleshooting tip**: If the output shows "PortFast mode is disabled," re-enter interface mode and double-check that the port is explicitly set to access mode with `switchport mode access` (configured in Lesson 6). PortFast will not run on ports operating in trunk mode.
* **🎯 Mini challenge**: Save the running configuration file to NVRAM so these edge security settings are preserved through a device reboot. *(Answer: `copy running-config startup-config` or `write`)*

---

### Step 6️⃣: Access the Branch-S2 Switch and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: To ensure consistent security across our entire enterprise network, we must mirror our headquarters edge security profile at our remote office. We will log into the `Branch-S2` switch, pass the security banner, and enter global configuration mode.
* **Commands to execute**:
```bash
Branch-S2> enable
Password: class
Branch-S2# configure terminal
Branch-S2(config)#

```


* **Verification commands**: Verify that the command prompt updates to indicate global configuration mode.
```bash
# The prompt must read:
Branch-S2(config)#

```


* **🚨 Common error note or Troubleshooting tip**: Always check the hostname prompt before typing configuration commands to avoid making accidental modifications to the wrong device.
* **🎯 Mini challenge**: What command can you use to check the status of all active terminal timeout values configured back in Lesson 5? *(Answer: `show terminal` or `show running-config | section line`)*

---

### Step 7️⃣: Select the Remote Branch Access Ports on Branch-S2

* **Mini-Lesson / Explanation**: Reviewing our Lesson 1 topology and Lesson 7 configuration settings, the branch host devices `BR-PC3` and `BR-PC4` connect to `Branch-S2` through ports `FastEthernet0/1` and `FastEthernet0/6`. We will select both of these ports using the `interface range` tool.
* **Commands to execute**:
```bash
Branch-S2(config)# interface range FastEthernet0/1, FastEthernet0/6
Branch-S2(config-if-range)#

```


* **Verification commands**: Confirm that the command prompt context changes to interface range mode.
```bash
# The prompt must update to:
Branch-S2(config-if-range)#

```


* **🚨 Common error note or Troubleshooting tip**: If you misinterpret the interface layout and use a hyphen instead of a comma (e.g., `0/1 - 6`), you will accidentally alter interfaces 2, 3, 4, and 5 as well. Always use commas for non-consecutive ports.
* **🎯 Mini challenge**: What command can you run from this prompt to verify the descriptions of the selected interfaces? *(Answer: `do show interface description`)*

---

### Step 8️⃣: Apply PortFast and BPDU Guard to Branch-S2 Interfaces

* **Mini-Lesson / Explanation**: We will now configure our branch access ports to use PortFast, allowing user devices to connect to the network instantly. We will also enable BPDU Guard to secure the branch perimeter against unauthorized switches or accidental loops.
* **Commands to execute**:
```bash
Branch-S2(config-if-range)# spanning-tree portfast
Branch-S2(config-if-range)# spanning-tree bpduguard enable

```


* **Verification commands**: Review the warning messages on the console and inspect the running configuration for the interface range.
```bash
Branch-S2(config-if-range)# do show running-config interface FastEthernet0/6
# Look for these lines in the output configuration block:
spanning-tree portfast
spanning-tree bpduguard enable

```


* **🚨 Common error note or Troubleshooting tip**: If a port connected to a computer unexpectedly shuts down after this step, check if the host device is running network bridging or virtualization software that transmits unauthorized BPDU management frames.
* **🎯 Mini challenge**: How can you remove both PortFast and BPDU Guard from an interface if its purpose changes in the future? *(Answer: Prepend the commands with `no`, such as `no spanning-tree portfast` and `no spanning-tree bpduguard enable`)*

---

### Step 9️⃣: Validate the Branch Switch Port Protection State

* **Mini-Lesson / Explanation**: To complete our deployment, we run a final verification check on `Branch-S2`. Using the `show spanning-tree interface [type/number] detail` command allows us to confirm that our branch ports are operating with PortFast enabled and that BPDU Guard is active, ensuring our entire network edge is optimized and secure.
* **Commands to execute**:
```bash
Branch-S2(config-if-range)# end
Branch-S2# show spanning-tree interface FastEthernet0/1 detail

```


* **Verification commands**: Review the operational output on your screen to verify the configuration details.
```bash
# The output text must display these active records:
Port 1 (FastEthernet0/1) of VLAN0010 is forwarding
Link type is point-to-point, The port is in the portfast mode
Bpdu guard is enabled

```


* **🚨 Common error note or Troubleshooting tip**: If your changes do not show up in the output, re-run the interface range configuration steps and make sure to save your work before logging out of the switch.
* **🎯 Mini challenge**: Save the final running configuration on `Branch-S2` so these settings survive a power cycle. *(Answer: Run `copy running-config startup-config` or `write`)*

---

### 📌 Key Takeaway

* **Instant Access**: Enabling `spanning-tree portfast` allows host-facing ports to bypass slow spanning-tree transition states and start forwarding data traffic immediately upon link connection.
* **Edge Security**: Enabling `spanning-tree bpduguard enable` protects your access ports by automatically shutting them down if an unauthorized switch is connected to the network edge.
* **Safe Optimization**: Only enable PortFast and BPDU Guard on access ports connected to end host devices. Never use these features on trunk ports or links that connect switches together.

---

Powered by Coding5s System