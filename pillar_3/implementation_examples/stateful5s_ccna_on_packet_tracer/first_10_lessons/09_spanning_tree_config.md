### 🔹 Lesson #09 | [Beginner] | Networking

### Concept: Configure Rapid PVST+ and Root Bridge Election

Greetings, future network engineers! As your Enterprise Spanning-Tree Topology & Rapid Convergence Optimization Architect, I welcome you back to the network engine room. Up to this point, we have built a robust Layer 2 structure across our main office switch (`HQ-S1`) and branch switch (`Branch-S2`) by assigning access ports (Lessons 6 & 7) and defining 802.1Q trunk paths (Lesson 8).

Today, we focus on switching stability and performance. Left to their defaults, Cisco switches run standard Per-VLAN Spanning Tree Plus (PVST+), which can take up to 50 seconds to recover if a link fails. This lesson guides you through migrating your switches to **Rapid PVST+ (802.1w)** to achieve sub-second convergence times. We will also learn how to manually modify bridge priorities to choose our network's **Root Bridge**, ensuring that data flows along the most efficient and predictable paths possible.

---

### 💡 Analogy

Think of your Layer 2 network as a city's road infrastructure. If there are multiple open roads connecting your buildings, delivery trucks might get stuck driving in endless circles, creating a traffic jam that completely shuts down the city (a Layer 2 broadcast storm).

Spanning Tree Protocol acts like an **intelligent traffic control center** that strategically places barriers on redundant paths to keep traffic moving in a clean, loop-free tree pattern. The **Root Bridge** is the central logistics hub at the base of this tree. Upgrading from standard PVST+ to **Rapid PVST+** is like replacing slow, manual traffic barriers with automated, high-speed electronic gates that reopen alternate routes instantly if a main road is blocked.

---

### Step 1️⃣: Access the HQ-S1 Switch and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: To update our spanning-tree operating protocol, we must first connect to the headquarters core switch (`HQ-S1`). We will navigate past the login banners designed in Lesson 5, authenticate using the local administrative credentials configured in Lesson 3, and enter global configuration mode.
* **Commands to execute**:
```bash
HQ-S1> enable
Password: class
HQ-S1# configure terminal
HQ-S1(config)#

```


* **Verification commands**: Monitor the command prompt transition to confirm you have entered the global configuration context.
```bash
# The prompt must read exactly:
HQ-S1(config)#

```


* **🚨 Common error note or Troubleshooting tip**: If you cannot access the device, check that you are logged into `HQ-S1` and not one of the upstream routers, and verify that your caps-lock key is disabled.
* **🎯 Mini challenge**: What keyboard shortcut returns you instantly to privileged EXEC mode from deep within sub-configuration menus? *(Answer: `Ctrl+Z` or typing `end`)*

---

### Step 2️⃣: Transition the Spanning-Tree Operating Mode to Rapid PVST+ on HQ-S1

* **Mini-Lesson / Explanation**: Standard PVST+ relies on slow, timer-based transition states (Listening and Learning). By executing the `spanning-tree mode rapid-pvst` command, we upgrade the switch to use the IEEE 802.1w standard, which introduces a fast handshake mechanism that safely brings ports to a forwarding state almost instantly.
* **Commands to execute**:
```bash
HQ-S1(config)# spanning-tree mode rapid-pvst

```


* **Verification commands**: Check the global configuration file to ensure the spanning-tree mode has updated successfully.
```bash
HQ-S1(config)# do show running-config | include spanning-tree mode
# Expected output:
spanning-tree mode rapid-pvst

```


* **🚨 Common error note or Troubleshooting tip**: When you change the spanning-tree mode globally, your terminal may briefly output port transition messages. This is normal behavior as the switch rebuilds its topology database using the faster protocol.
* **🎯 Mini challenge**: What are the three active port states used by Rapid PVST+? *(Answer: Discarding, Learning, and Forwarding)*

---

### Step 3️⃣: Force HQ-S1 to Become the Definitive Root Bridge

* **Mini-Lesson / Explanation**: If we do not manually choose a Root Bridge, switches will automatically elect one based on whichever device has the lowest physical MAC address. This default behavior can result in an older, slower switch being elected as the center of your network. We use the macro command `spanning-tree vlan [ids] root primary` to automatically lower `HQ-S1`'s priority value, ensuring it wins the election for our active production networks: **VLANs 10, 20, and 99**.
* **Commands to execute**:
```bash
HQ-S1(config)# spanning-tree vlan 10,20,99 root primary

```


* **Verification commands**: Exit configuration mode to verify how the root bridge parameters are applied to the switch database.
```bash
HQ-S1(config)# exit
HQ-S1#

```


* **🚨 Common error note or Troubleshooting tip**: Always ensure your VLAN IDs match your network design exactly. Misspelling your VLAN numbers or including extra spaces (like `10, 20`) will result in a syntax parsing error.
* **🎯 Mini challenge**: What specific priority value does the `root primary` command assign to a switch if the other devices are running at defaults? *(Answer: It automatically drops the priority value down to 24,576)*

---

### Step 4️⃣: Verify Spanning-Tree State and Root Election on HQ-S1

* **Mini-Lesson / Explanation**: Verification is an essential habit for managing reliable corporate networks. We use the `show spanning-tree` command to confirm that our spanning-tree mode is operating under the rapid profile and that `HQ-S1` successfully recognizes itself as the root system for our configured VLANs.
* **Commands to execute**:
```bash
HQ-S1# show spanning-tree

```


* **Verification commands**: Scan the command output for each active VLAN to verify the root bridge status.
```bash
# For VLAN 10, VLAN 20, and VLAN 99, you must observe this specific phrase:
Root ID    Priority    24586 (or similar calculated value)
           Address     0001.XXXX.XXXX
           This bridge is the root

```


* **🚨 Common error note or Troubleshooting tip**: Spanning-Tree adds the specific VLAN ID number to the base priority value (e.g., $24576 + 10 = 24586$). Do not panic if your priority number does not look like a perfect round number; this is normal system behavior known as the System ID Extension.
* **🎯 Mini challenge**: What specialized command filter reduces this verbose output to show only a quick summary table? *(Answer: `show spanning-tree summary`)*

---

### Step 5️⃣: Access the Branch-S2 Switch and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: To maintain stability across our entire network, we must ensure our remote branch matches our core configuration. We will connect to `Branch-S2`, bypass the secure login banner, and elevate our permissions to enter global configuration mode.
* **Commands to execute**:
```bash
Branch-S2> enable
Password: class
Branch-S2# configure terminal
Branch-S2(config)#

```


* **Verification commands**: Confirm that the device prompt updates correctly to indicate configuration mode.
```bash
# The prompt must read:
Branch-S2(config)#

```


* **🚨 Common error note or Troubleshooting tip**: Always verify your terminal prompt's hostname before entering commands to prevent accidentally changing settings on the wrong switch.
* **🎯 Mini challenge**: Write the absolute minimum abbreviated command syntax needed to enter global configuration mode. *(Answer: `conf t`)*

---

### Step 6️⃣: Upgrade the Remote Branch Switch to Rapid PVST+

* **Mini-Lesson / Explanation**: For Rapid Spanning Tree to function correctly across the entire network, every switch in your topology must run the same protocol version. We will configure `Branch-S2` to run Rapid PVST+, allowing it to coordinate seamlessly with `HQ-S1`.
* **Commands to execute**:
```bash
Branch-S2(config)# spanning-tree mode rapid-pvst

```


* **Verification commands**: Run a check to confirm the spanning-tree mode has been updated on the branch switch.
```bash
Branch-S2(config)# do show running-config | include spanning-tree mode
# Must display: spanning-tree mode rapid-pvst

```


* **🚨 Common error note or Troubleshooting tip**: If you connect a switch running Rapid PVST+ to an older switch running standard PVST+, the ports will automatically drop back to the slower standard speeds to maintain compatibility.
* **🎯 Mini challenge**: What command allows you to view the real-time status of a single specific VLAN's spanning-tree parameters? *(Answer: `show spanning-tree vlan [id]`)*

---

### Step 7️⃣: Manually Set the Bridge Priority for Branch-S2

* **Mini-Lesson / Explanation**: Instead of using the generic macro command we used on the primary switch, we can also manually control the root bridge election by explicitly defining numerical priority values. Spanning-tree priorities must be configured in precise increments of **4096**. We will explicitly set `Branch-S2`'s priority to **24576** for VLANs 10, 20, and 99. This establishes a predictable priority hierarchy across our branch infrastructure.
* **Commands to execute**:
```bash
Branch-S2(config)# spanning-tree vlan 10,20,99 priority 24576

```


* **Verification commands**: Save your changes and return to privileged EXEC mode to verify that the priority value has been accepted.
```bash
Branch-S2(config)# end
Branch-S2#

```


* **🚨 Common error note or Troubleshooting tip**: If you enter a random priority value like `25000`, the switch will reject the command with an error message stating that values must be applied in multiples of 4096.
* **🎯 Mini challenge**: What is the default factory spanning-tree priority value applied to all Cisco switches before manual configuration? *(Answer: 32768)*

---

### Step 8️⃣: Verify Branch Spanning-Tree Configuration and Summary Status

* **Mini-Lesson / Explanation**: To complete our deployment, we run a final verification step on `Branch-S2`. Using the `show spanning-tree summary` command gives us a concise overview of our configuration, allowing us to confirm that the switch is operating in Rapid PVST+ mode and verify its active port states.
* **Commands to execute**:
```bash
Branch-S2# show spanning-tree summary

```


* **Verification commands**: Carefully inspect the output summary block to verify your configuration details match the expected layout.
```bash
# The output text must display the following operational indicators:
Switch is in rapid-pvst mode
Root bridge for: (Should list none if HQ-S1 is the primary core root, or list localized segments if disconnected)

# Check that your ports show active statistics under the RSTP columns.

```


* **🚨 Common error note or Troubleshooting tip**: If your summary status shows ports stuck in a blocking or discarding state unexpectedly, check your trunk links (configured in Lesson 8) to ensure they are forwarding traffic properly.
* **🎯 Mini challenge**: Save your running configuration across all switches to ensure these spanning-tree settings survive a power cycle. *(Answer: Run `copy running-config startup-config` or `write`)*

---

### 📌 Key Takeaway

* **Rapid Convergence**: Upgrading your network to Rapid PVST+ reduces Spanning-Tree topology recovery times from 50 seconds down to less than one second, keeping network interruptions to a minimum.
* **Deterministic Root Control**: Never leave root bridge elections to chance defaults. Manually defining your root bridge layout ensures that data traffic always follows the most efficient paths through your hardware.
* **Priority Math**: Spanning-tree priority values must always be configured in multiples of **4096**, and lower values always win the election to become the root bridge.

---

Powered by Coding5s System