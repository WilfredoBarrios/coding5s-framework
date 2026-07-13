### 🔹 Lesson #07 | [Beginner] | Networking

### Concept: Configure Basic VLANs and Assign Ports on Branch-S2

Greetings, network engineers! As your Remote Branch Layer 2 Segmentation & Switchport Provisioning Architect, I welcome you back to the deployment terminal. In Lesson 6, we successfully established a foundational Layer 2 architectural blueprint at our headquarters by configuring Virtual Local Area Networks (VLANs) on `HQ-S1` to separate corporate departments.

Today, we will actively use our accumulated topology context to replicate that identical security matrix at our remote branch office. Our target is the `Branch-S2` switch. By creating Engineering, Sales, and Management VLANs and assigning ports for `BR-PC3` and `BR-PC4`, we ensure that traffic segmentation and security policies remain consistent across the entire enterprise infrastructure.

---

### 💡 Analogy

Think of an unconfigured switch out of the box as a massive open-plan office floor where everyone can hear everyone else talking (a single broadcast domain). Implementing VLANs is like constructing permanent soundproof drywall partitions to create distinct rooms: an **Engineering Room (VLAN 10)**, a **Sales Room (VLAN 20)**, and a **Management Room (VLAN 99)**. Assigning an interface to a VLAN is the equivalent of moving an employee's desk into their respective department's room. Even though they share the same physical building floor, they can no longer overhear or interfere with each other's conversations.

---

### Step 1️⃣: Access Branch-S2 via the CLI and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: To modify the switch database and configure broadcast domains, we must log into the device and move up to the global configuration prompt. We will use the security credentials established in Lesson 3 and bypass the login banner configured in Lesson 5.
* **Commands to execute**:
```bash
Branch-S2> enable
Password: class
Branch-S2# configure terminal
Branch-S2(config)#

```


* **Verification commands**: Verify that the CLI prompt transitions successfully to indicate global configuration mode.
```bash
# The prompt must read exactly:
Branch-S2(config)#

```


* **🚨 Common error note or Troubleshooting tip**: If you are prompted for a username and password before reaching the `enable` prompt, remember that Lesson 3 applied `login local` to the console line; use the admin credentials (`admin` / `admin123!`) created previously.
* **🎯 Mini challenge**: What command can you run to instantly view your current privilege level while in the execution prompt? *(Answer: `show privilege`)*

---

### Step 2️⃣: Create the Remote Engineering VLAN 10

* **Mini-Lesson / Explanation**: To isolate engineering network traffic at the branch site, we initialize the VLAN within the switch configuration database using the `vlan [id]` syntax. Once initialized, we immediately name it to ensure it matches the naming standard used on `HQ-S1`.
* **Commands to execute**:
```bash
Branch-S2(config)# vlan 10
Branch-S2(config-vlan)# name Engineering

```


* **Verification commands**: Move back one level to see that the configuration has been accepted by the switch.
```bash
Branch-S2(config-vlan)# exit
Branch-S2(config)#

```


* **🚨 Common error note or Troubleshooting tip**: Cisco IOS VLAN names are case-sensitive. Naming this "engineering" with a lowercase "e" can cause confusion during automated monitoring audits. Always match your enterprise standard exactly.
* **🎯 Mini challenge**: What is the valid range of standard VLAN IDs that can be configured on an enterprise switch? *(Answer: 1 to 1005)*

---

### Step 3️⃣: Create the Remote Sales VLAN 20

* **Mini-Lesson / Explanation**: Next, we create the logical broadcast domain for the branch sales team. This mirrors our headquarters segmentation and separates sales traffic entirely from engineering systems at Layer 2.
* **Commands to execute**:
```bash
Branch-S2(config)# vlan 20
Branch-S2(config-vlan)# name Sales

```


* **Verification commands**: Exit the VLAN sub-mode context safely to return to the global configuration prompt.
```bash
Branch-S2(config-vlan)# exit
Branch-S2(config)#

```


* **🚨 Common error note or Troubleshooting tip**: If you make a mistake with the name, simply type the `name` command again with the correct string while inside the `config-vlan` prompt to overwrite the previous entry.
* **🎯 Mini challenge**: How would you completely remove a mistakenly created VLAN from the database? *(Answer: Prepend the command with `no`, such as `no vlan 20`)*

---

### Step 4️⃣: Create the Remote Management VLAN 99

* **Mini-Lesson / Explanation**: Keeping management traffic separate from regular user data is a core security best practice. We create VLAN 99 specifically to handle administrative remote access for our switch, keeping it isolated from standard user traffic.
* **Commands to execute**:
```bash
Branch-S2(config)# vlan 99
Branch-S2(config-vlan)# name Management

```


* **Verification commands**: Exit the VLAN configuration mode back to global configuration to prepare for port provisioning.
```bash
Branch-S2(config-vlan)# exit
Branch-S2(config)#

```


* **🚨 Common error note or Troubleshooting tip**: Forgetting to exit the `config-vlan` prompt before executing general interface commands can lead to input syntax errors on older Cisco IOS software releases.
* **🎯 Mini challenge**: Can data devices assigned to VLAN 10 communicate directly with devices in VLAN 20 or 99 without a Layer 3 device like a router? *(Answer: No, devices in different VLANs require a Layer 3 router or multilayer switch to communicate)*

---

### Step 5️⃣: Select Interface FastEthernet0/1

* **Mini-Lesson / Explanation**: According to our accumulated topology context from Lesson 1, the branch host workstation `BR-PC3` is physically patched into the switch port `FastEthernet0/1`. We must select this specific interface to change its operational settings.
* **Commands to execute**:
```bash
Branch-S2(config)# interface FastEthernet0/1
Branch-S2(config-if)#

```


* **Verification commands**: Confirm that the command prompt updates to reflect the interface context.
```bash
# The prompt must update to:
Branch-S2(config-if)#

```


* **🚨 Common error note or Troubleshooting tip**: Make sure you type the interface identifier correctly. Typing `FastEthernet01` without the forward slash (`/`) will result in an "Invalid input detected" error message.
* **🎯 Mini challenge**: What shorthand abbreviation can you use to quickly access this interface instead of typing out the full name? *(Answer: `int f0/1`)*

---

### Step 6️⃣: Configure FastEthernet0/1 as an Access Port

* **Mini-Lesson / Explanation**: Switch ports can function as access ports (connecting to a single end device like a PC) or trunk ports (carrying traffic for multiple VLANs between switches). We will explicitly configure this port as an access port using the `switchport mode access` command.
* **Commands to execute**:
```bash
Branch-S2(config-if)# switchport mode access

```


* **Verification commands**: Use the `do show` shortcut to verify the administrative mode of the switch port.
```bash
Branch-S2(config-if)# do show interfaces FastEthernet0/1 switchport | include Administrative Mode
# Expected output:
Administrative Mode: static access

```


* **🚨 Common error note or Troubleshooting tip**: While modern switches may default to access mode, leaving ports on dynamic default settings poses a security risk. Explicitly defining access ports prevents unauthorized trunking attempts.
* **🎯 Mini challenge**: What is the opposite operational mode of an access port used to connect two switches together? *(Answer: Trunk mode)*

---

### Step 7️⃣: Assign FastEthernet0/1 to Engineering VLAN 10

* **Mini-Lesson / Explanation**: Now that the interface is set to access mode, we map it directly to the Engineering network domain using the `switchport access vlan 10` command. This ensures all incoming traffic from host `BR-PC3` is tagged under VLAN 10.
* **Commands to execute**:
```bash
Branch-S2(config-if)# switchport access vlan 10

```


* **Verification commands**: Run a targeted configuration check to confirm that the port assignment is active.
```bash
Branch-S2(config-if)# do show running-config interface FastEthernet0/1
# Expected output:
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access

```


* **🚨 Common error note or Troubleshooting tip**: If you assign a port to a VLAN number that does not exist in the switch database, Cisco IOS will automatically create that VLAN for you. However, it will not have a descriptive name, which can lead to layout clutter.
* **🎯 Mini challenge**: If you need to reassign this interface back to the default native VLAN, what command would you run? *(Answer: `no switchport access vlan`)*

---

### Step 8️⃣: Select Interface FastEthernet0/6

* **Mini-Lesson / Explanation**: Reviewing our Lesson 1 connection logs shows that our second branch host workstation, `BR-PC4`, is physically wired into port `FastEthernet0/6`. We must exit the first interface and move into the configuration context for this port.
* **Commands to execute**:
```bash
Branch-S2(config-if)# exit
Branch-S2(config)# interface FastEthernet0/6
Branch-S2(config-if)#

```


* **Verification commands**: Verify the contextual state modification in the command line interface.
```bash
# The prompt must display:
Branch-S2(config-if)#

```


* **🚨 Common error note or Troubleshooting tip**: If you forget to modify the specific interface number and continue typing configuration commands, you will accidentally alter the settings on `FastEthernet0/1` instead of `FastEthernet0/6`.
* **🎯 Mini challenge**: If you needed to select interfaces 1 through 5 all at once to apply a configuration, what command would you use? *(Answer: `interface range FastEthernet0/1 - 5`)*

---

### Step 9️⃣: Configure FastEthernet0/6 as an Access Port and Assign to Sales VLAN 20

* **Mini-Lesson / Explanation**: To mirror our headquarters layout, the branch host `BR-PC4` needs to be mapped to the Sales department. We will explicitly configure the port to access mode and assign it to the newly built **Sales VLAN 20**.
* **Commands to execute**:
```bash
Branch-S2(config-if)# switchport mode access
Branch-S2(config-if)# switchport access vlan 20

```


* **Verification commands**: Run a validation check on this interface to confirm both lines are applied.
```bash
Branch-S2(config-if)# do show running-config interface FastEthernet0/6
# Expected output:
interface FastEthernet0/6
 switchport access vlan 20
 switchport mode access

```


* **🚨 Common error note or Troubleshooting tip**: When you change a port's VLAN assignment, the link may temporarily go down and come back up (blinking amber to green in Packet Tracer) as Spanning Tree Protocol recalculates the state for the new VLAN topology.
* **🎯 Mini challenge**: What command can you use to quickly check the operational up or down status of all ports on the switch? *(Answer: `show ip interface brief`)*

---

### Step 🔟: Verify Remote VLAN Creation and Port Assignments

* **Mini-Lesson / Explanation**: To complete our deployment, we need to verify our work using a comprehensive check. The `show vlan brief` command displays the entire structural matrix of the switch, allowing us to confirm that our VLANs are active and our interfaces are correctly assigned.
* **Commands to execute**:
```bash
Branch-S2(config-if)# end
Branch-S2# show vlan brief

```


* **Verification commands**: Carefully inspect the output table on your terminal screen to verify the configuration matches the expected layout.
```bash
# The output table must display the following records:
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/2, Fa0/3, Fa0/4, Fa0/5,
                                                Fa0/7, ... [truncated]
10   Engineering                      active    Fa0/1
20   Sales                            active    Fa0/6
99   Management                       active

```


* **🚨 Common error note or Troubleshooting tip**: If you see your VLANs listed but no ports appear next to them under the "Ports" column, double-check that you entered the correct interface numbers during Steps 7 and 9.
* **🎯 Mini challenge**: Save the updated active configuration on `Branch-S2` so it remains intact if the switch loses power. *(Answer: Run `copy running-config startup-config` or `write`)*

---

### 📌 Key Takeaway

* **Broadcast Domain Separation**: Creating VLANs breaks a single physical switch into multiple distinct, isolated logical networks, reducing unnecessary broadcast traffic.
* **Access Layer Security**: Explicitly defining `switchport mode access` provides a secure configuration profile for host-facing connections.
* **Consistent Layouts**: Replicating identical VLAN structures across all your enterprise sites simplifies network management and ensures security policies are applied consistently throughout the organization.

---

Powered by Coding5s System