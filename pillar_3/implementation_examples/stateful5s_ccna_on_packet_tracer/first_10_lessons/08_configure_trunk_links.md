### 🔹 Lesson #08 | [Beginner] | Networking

### Concept: Configure Trunk Links Between Switching Segments

Greetings, future network engineers! As your Enterprise Layer 2 Trunking & 802.1Q Encapsulation Authority, I welcome you back to the staging console. In Lessons 6 and 7, we engineered a segmented Layer 2 broadcast architecture by establishing specific departmental boundaries (VLAN 10 for Engineering, VLAN 20 for Sales, and VLAN 99 for Management) across both `HQ-S1` and `Branch-S2`.

Currently, our switches isolate this traffic locally. However, to pass data between our switches and upstream routing engines (`HQ-R1` and `Branch-R2`), we need a way for a single physical connection to carry multiple VLANs simultaneously. Today, we will deploy IEEE 802.1Q trunk links to establish that critical baseline capability.

---

### 💡 Analogy

Think of access ports as single-lane suburban roads built exclusively for one type of vehicle (like a standard passenger car). A trunk link, on the other hand, is like a massive multi-lane commercial highway. To ensure cargo does not get lost or delivered to the wrong corporate site, every vehicle entering this highway receives a color-coded shipping manifest sticker (**an 802.1Q tag**) indicating its department. The **Native VLAN** acts like an emergency lane on this highway where unmarked utility vehicles (untagged traffic) can travel safely without any stickers at all.

---

### Step 1️⃣: Access the HQ-S1 Switch and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: To establish trunk lines on our headquarters switching segment, we begin by connecting to `HQ-S1`. We will pass through the security banners we built in Lesson 5, authenticate using the local administrative credentials configured in Lesson 3, and elevate our privilege level to global configuration mode.
* **Commands to execute**:
```bash
HQ-S1> enable
Password: class
HQ-S1# configure terminal
HQ-S1(config)#

```


* **Verification commands**: Monitor the terminal prompt state to verify successful entry into global configuration mode.
```bash
# The prompt must display exactly:
HQ-S1(config)#

```


* **🚨 Common error note or Troubleshooting tip**: If the terminal rejects the password `class`, verify that you are configuring `HQ-S1` and not one of the routers, and ensure your caps lock is off.
* **🎯 Mini challenge**: What command lets you review all previously executed commands in this session buffer? *(Answer: `show history`)*

---

### Step 2️⃣: Select Interface GigabitEthernet0/1 on HQ-S1

* **Mini-Lesson / Explanation**: Based on our accumulated topology context from Lesson 1, the physical connection heading upstream from `HQ-S1` to our enterprise router `HQ-R1` uses the high-speed interface `GigabitEthernet0/1`. We must change our configuration focus directly to this specific port.
* **Commands to execute**:
```bash
HQ-S1(config)# interface GigabitEthernet0/1
HQ-S1(config-if)#

```


* **Verification commands**: Confirm that the prompt context changes to interface configuration mode.
```bash
# The prompt must read:
HQ-S1(config-if)#

```


* **🚨 Common error note or Troubleshooting tip**: Be careful not to select a FastEthernet port by mistake. Our upstream links to the core routers use Gigabit interfaces to ensure adequate bandwidth for handling multiplexed trunk traffic.
* **🎯 Mini challenge**: What is the shorthand string to enter this exact interface context? *(Answer: `int g0/1`)*

---

### Step 3️⃣: Force the Port to Become an 802.1Q Trunk Link on HQ-S1

* **Mini-Lesson / Explanation**: By default, switch interfaces are designed to act as standard host connection lines. We use the `switchport mode trunk` command to change this port's behavior, configuring it to use IEEE 802.1Q encapsulation to tag and transport multiple broadcast domains across a single physical cable.
* **Commands to execute**:
```bash
HQ-S1(config-if)# switchport mode trunk

```


* **Verification commands**: Check for the system log notification confirming the port state transition.
```bash
# The CLI will generate a syslog message similar to:
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

```


* **🚨 Common error note or Troubleshooting tip**: On some physical hardware platforms, you must explicitly type `switchport trunk encapsulation dot1q` before the switch will accept the `switchport mode trunk` command. Packet Tracer Catalyst 2960 switches use 802.1Q by default.
* **🎯 Mini challenge**: What command reverses a port configuration back to its factory default state? *(Answer: `default interface GigabitEthernet0/1`)*

---

### Step 4️⃣: Configure the Native VLAN on the HQ-S1 Trunk

* **Mini-Lesson / Explanation**: The native VLAN handles any frames that cross an 802.1Q trunk link without an explicit VLAN tag. Leaving the native VLAN at its default value (VLAN 1) poses a serious security vulnerability. To mitigate this risk, we shift our native traffic to our dedicated Management network (**VLAN 99**), matching our baseline strategy.
* **Commands to execute**:
```bash
HQ-S1(config-if)# switchport trunk native vlan 99

```


* **Verification commands**: View the running interface settings to ensure the native VLAN statement is active.
```bash
HQ-S1(config-if)# do show running-config interface GigabitEthernet0/1
# Check for the line: switchport trunk native vlan 99

```


* **🚨 Common error note or Troubleshooting tip**: Once you change the native VLAN on `HQ-S1`, you may see periodic `%CDP-4-NATIVE_VLAN_MISMATCH` syslog errors until the upstream device on the other side of the link is configured with the exact same native VLAN ID.
* **🎯 Mini challenge**: Why must the native VLAN match perfectly on both ends of a trunk link? *(Answer: To prevent traffic leakage and loops between different VLANs)*

---

### Step 5️⃣: Restrict Allowed VLANs on the HQ-S1 Trunk

* **Mini-Lesson / Explanation**: By default, a Cisco trunk link allows all VLANs (from 1 to 4094) to cross it. To optimize bandwidth and secure our network, we use the `switchport trunk allowed vlan` command to restrict the trunk, permitting only our active production environments: **VLANs 10, 20, and 99**.
* **Commands to execute**:
```bash
HQ-S1(config-if)# switchport trunk allowed vlan 10,20,99

```


* **Verification commands**: Verify that the explicit list is correctly applied to the interface's active database profile.
```bash
HQ-S1(config-if)# do show running-config interface GigabitEthernet0/1
# Look for: switchport trunk allowed vlan 10,20,99

```


* **🚨 Common error note or Troubleshooting tip**: Never include spaces between the comma-separated numbers in your VLAN list (e.g., typing `10, 20` instead of `10,20`). Doing so will result in a syntax error in Cisco IOS.
* **🎯 Mini challenge**: If you want to add an extra VLAN later without wiping out this list, what keyword must you append? *(Answer: The `add` keyword, like `switchport trunk allowed vlan add 30`)*

---

### Step 6️⃣: Verify Operational Trunk Status on HQ-S1

* **Mini-Lesson / Explanation**: Before configuring our branch site, we need to verify that our trunk configuration is working properly. The `show interfaces trunk` command provides a clear view of our active trunk ports, operational modes, encapsulation types, and allowed VLAN matrices.
* **Commands to execute**:
```bash
HQ-S1(config-if)# end
HQ-S1# show interfaces trunk

```


* **Verification commands**: Carefully check the status table on your terminal display to ensure your configuration matches the expected layout.
```bash
# The output summary table must match these parameters:
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      on           802.1q         trunking      99

Port        Vlans allowed on trunk
Gig0/1      10,20,99

```


* **🚨 Common error note or Troubleshooting tip**: If `GigabitEthernet0/1` is not showing up in the output of this command, check that the interface is physically up and that the cable to `HQ-R1` is properly connected.
* **🎯 Mini challenge**: Save the running configuration to NVRAM so these settings persist through a device reload. *(Answer: `copy running-config startup-config`)*

---

### Step 7️⃣: Access the Branch-S2 Switch and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: Now that the headquarters side is secure, we turn our attention to our remote branch environment. We will log into the `Branch-S2` switch, clear the login banner, and move into global configuration mode to replicate our trunking configuration.
* **Commands to execute**:
```bash
Branch-S2> enable
Password: class
Branch-S2# configure terminal
Branch-S2(config)#

```


* **Verification commands**: Confirm that the terminal prompt transitions properly into configuration mode.
```bash
# Ensure the prompt states:
Branch-S2(config)#

```


* **🚨 Common error note or Troubleshooting tip**: Always verify your hostname prompt before typing configuration commands to ensure you do not accidentally overwrite settings on the wrong switch.
* **🎯 Mini challenge**: What terminal command can you run from privileged EXEC mode to completely clear the screen? *(Answer: `clear screen` or Ctrl+L in some terminals)*

---

### Step 8️⃣: Select Interface GigabitEthernet0/1 on Branch-S2

* **Mini-Lesson / Explanation**: Reviewing our Lesson 1 connection architecture, the branch office switch uses interface `GigabitEthernet0/1` as its core link to connect upstream to the branch router, `Branch-R2`. We will enter this interface mode now.
* **Commands to execute**:
```bash
Branch-S2(config)# interface GigabitEthernet0/1
Branch-S2(config-if)#

```


* **Verification commands**: Verify that your prompt updates to reflect the interface configuration context.
```bash
# The prompt must read:
Branch-S2(config-if)#

```


* **🚨 Common error note or Troubleshooting tip**: If you see an error indicating that the interface does not exist, use `show ip interface brief` to check the exact slot and port numbering scheme for this specific switch hardware.
* **🎯 Mini challenge**: What command lets you add a helpful text label to an interface to document its purpose for other technicians? *(Answer: The `description` command, e.g., `description Link to Branch-R2`)*

---

### Step 9️⃣: Configure the Port as an 802.1Q Trunk Link on Branch-S2

* **Mini-Lesson / Explanation**: We will now configure this port as a trunk line to mirror the configuration at our headquarters site. This changes the port from a standard access connection to an 802.1Q trunk link, allowing it to transport traffic for all our branch office VLANs.
* **Commands to execute**:
```bash
Branch-S2(config-if)# switchport mode trunk

```


* **Verification commands**: Verify that the interface updates its status successfully.
```bash
# Look for the interface change notification:
%LINK-5-CHANGED: Interface GigabitEthernet0/1, changed state to up

```


* **🚨 Common error note or Troubleshooting tip**: If the link stays down (indicated by a red link light in Packet Tracer), make sure the interface on the connecting device (`Branch-R2`) has been enabled using the `no shutdown` command.
* **🎯 Mini challenge**: What default operational mode does an unconfigured Cisco switch port use to negotiate trunking automatically? *(Answer: Dynamic Auto or Dynamic Desirable, via Dynamic Trunking Protocol)*

---

### Step 1️⃣0️⃣: Set the Native VLAN on the Branch-S2 Trunk

* **Mini-Lesson / Explanation**: To maintain consistency across our network enterprise structure and prevent native VLAN mismatch errors, we must assign **VLAN 99** as the native VLAN on this trunk link, mirroring our configuration on `HQ-S1`.
* **Commands to execute**:
```bash
Branch-S2(config-if)# switchport trunk native vlan 99

```


* **Verification commands**: Confirm that the native VLAN statement is saved to the interface configuration profile.
```bash
Branch-S2(config-if)# do show running-config interface GigabitEthernet0/1
# Verify line present: switchport trunk native vlan 99

```


* **🚨 Common error note or Troubleshooting tip**: If you see native VLAN mismatch errors pop up after this step, verify that the native VLAN settings match perfectly on both sides of the link.
* **🎯 Mini challenge**: What command can you use to disable Dynamic Trunking Protocol (DTP) negotiations on this interface? *(Answer: `switchport nonegotiate`)*

---

### Step 1️⃣1️⃣: Explicitly Permit Required VLANs on the Branch-S2 Trunk

* **Mini-Lesson / Explanation**: To complete our security policy deployment, we restrict the allowed VLAN list on our branch trunk link. This ensures that only traffic from **VLANs 10, 20, and 99** is permitted to cross the link to `Branch-R2`.
* **Commands to execute**:
```bash
Branch-S2(config-if)# switchport trunk allowed vlan 10,20,99

```


* **Verification commands**: Review the running interface configuration to confirm the allowed VLAN list is applied correctly.
```bash
Branch-S2(config-if)# do show running-config interface GigabitEthernet0/1
# Confirm configuration: switchport trunk allowed vlan 10,20,99

```


* **🚨 Common error note or Troubleshooting tip**: If you run this command and accidentally mistype a VLAN ID (like typing `9` instead of `99`), you will lose management access across that trunk link. Always double-check your values before pressing Enter.
* **🎯 Mini challenge**: How can you reset the trunk link to allow all standard default VLANs across it again? *(Answer: `no switchport trunk allowed vlan`)*

---

### Step 1️⃣2️⃣: Verify Trunk Link Establishment on Branch-S2

* **Mini-Lesson / Explanation**: To finalize our deployment, we run a final verification check on `Branch-S2`. Using the `show interfaces trunk` command allows us to confirm that our trunk link is operating correctly, our native VLAN is secured, and our allowed VLAN parameters match our enterprise network standards.
* **Commands to execute**:
```bash
Branch-S2(config-if)# end
Branch-S2# show interfaces trunk

```


* **Verification commands**: Review the operational table output on your screen to verify the configuration details.
```bash
# The output table must display these active records:
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      on           802.1q         trunking      99

Port        Vlans allowed on trunk
Gig0/1      10,20,99

```


* **🚨 Common error note or Troubleshooting tip**: If your allowed VLAN list shows entries you did not intend to include, rerun the `switchport trunk allowed vlan 10,20,99` command while in interface mode to overwrite the existing list.
* **🎯 Mini challenge**: Save your work on `Branch-S2` to ensure your trunking configurations survive a device reboot.

---

### 📌 Key Takeaway

* **Multiplexed Data Streams**: An 802.1Q trunk link allows a single physical cable to transport traffic for multiple VLANs simultaneously, keeping the networks isolated with identity tags.
* **Native VLAN Alignment**: The native VLAN configuration must match perfectly across all connected trunk ports to prevent data leakage and ensure proper network communication.
* **Pruning and Traffic Control**: Restricting allowed VLAN lists on your trunk links is an effective way to optimize bandwidth and improve security by keeping unnecessary broadcast traffic off your core network links.

---

Powered by Coding5s System