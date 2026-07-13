### 🔹 Lesson #6 | Beginner | Networking

**Configure Basic VLANs and Assign Ports on HQ-S1: Implementing Layer 2 Segmentation**

Welcome to Lesson 6! In our previous sessions, we built a physically and logically secure foundation. We established device identities (Lesson 2), secured local and remote access with SSH and strong passwords (Lessons 3 and 4), and applied security banners and timeouts (Lesson 5). Today, we shift our focus to Layer 2 of the OSI model. Our objective is to introduce network segmentation by configuring Virtual Local Area Networks (VLANs) to systematically isolate departmental broadcast traffic. You will implement real-world Layer 2 boundary containment by creating specific Engineering, Sales, and Management VLANs, and statically assigning user access ports to these isolated networks on the headquarters switch.

### 💡 Analogy
Imagine a large, open-plan office where everyone shouts to communicate. If the Engineering team shouts, the Sales team hears it too, causing unnecessary noise and distraction. This is what a broadcast domain looks like in a network without VLANs. By configuring VLANs, we are essentially building soundproof glass walls between these departments. Engineering can shout all they want, and only Engineering will hear it. Sales and Management remain in their own quiet, isolated spaces. This improves security, reduces unnecessary traffic, and organizes the network logically, regardless of physical location.

---

### Step 1️⃣: Accessing HQ-S1 and Creating the Engineering VLAN

**Mini-Lesson / Explanation**
To segment our network, we must first define the logical boundaries on our switch. We will start with the Headquarters switch, `HQ-S1`. We need to create a dedicated space for the Engineering department. In Cisco IOS, we do this by creating a VLAN database entry and assigning it a human-readable name. We will use VLAN ID 10 for Engineering. This logical separation is the first step in containing broadcast traffic.

**Commands to execute**
1. Click on the `HQ-S1` device in your workspace and navigate to the **CLI** tab.
2. Enter privileged EXEC and global configuration modes, then create the first VLAN:

```bash
enable
configure terminal
vlan 10
name Engineering
exit
```

**Verification commands**
Verify that the VLAN has been successfully added to the local database:

```bash
show vlan brief
```

*Observation:* You should see VLAN 10 listed with the name "Engineering" and the status "active". This confirms the logical boundary has been created in the switch's memory.

**🚨 Common error note or Troubleshooting tip**
A frequent beginner mistake is forgetting to exit VLAN configuration mode. While IOS allows you to type `vlan 20` directly from VLAN config mode, it is a strict best practice to explicitly `exit` back to global configuration to maintain a clean configuration hierarchy and avoid accidental misconfigurations.

**🎯 Mini challenge**
By default, all switch ports belong to VLAN 1. What happens to the ports that are currently in VLAN 1 when we create VLAN 10? Do they automatically move?

---

### Step 2️⃣: Creating the Sales and Management VLANs

**Mini-Lesson / Explanation**
With Engineering established, we must create the remaining logical boundaries for our enterprise. We will create VLAN 20 for the Sales department. Additionally, we will create VLAN 99 for Management. In enterprise networks, it is a strict security best practice to move switch management traffic (like the SSH access we configured in Lesson 4) out of the default VLAN 1 and into a dedicated, isolated Management VLAN.

**Commands to execute**
While still in global configuration mode on `HQ-S1`, create the remaining two VLANs:

```bash
vlan 20
name Sales
exit
vlan 99
name Management
exit
```

**Verification commands**
Verify that all three user-defined VLANs are now present in the database:

```bash
show vlan brief
```

*Observation:* The output should now display three distinct user-defined VLANs: 10 (Engineering), 20 (Sales), and 99 (Management), all with an "active" status. The switch is now logically prepared to segment traffic.

**🚨 Common error note or Troubleshooting tip**
Using spaces in VLAN names can cause parsing errors in the CLI. While `name Engineering` works perfectly, trying to use `name Engineering Dept` would result in the name being truncated or causing a syntax error depending on the IOS version. Always use single-word names or camelCase (e.g., `EngineeringDept`) for consistency.

**🎯 Mini challenge**
Why is it considered a critical security risk to leave the switch's management IP address in the default VLAN 1, especially in a corporate environment?

---

### Step 3️⃣: Configuring the HQ-PC1 Access Port for Engineering

**Mini-Lesson / Explanation**
Creating VLANs in the database does not automatically move traffic. We must explicitly tell the switch ports which VLAN they belong to. Recall from Lesson 1 that we connected `HQ-PC1` to port `FastEthernet0/1`. Since a PC is an end device that does not understand 802.1Q VLAN tags, we must configure this port as an "access port" and statically assign it to the Engineering VLAN (VLAN 10).

**Commands to execute**
Enter the interface configuration mode for `HQ-PC1` and apply the access settings:

```bash
interface FastEthernet0/1
switchport mode access
switchport access vlan 10
exit
```

**Verification commands**
Verify the operational status and VLAN assignment of the specific interface:

```bash
show interfaces FastEthernet0/1 switchport
```

*Observation:* Look for "Administrative Mode: static access" and "Access Mode VLAN: 10 (Engineering)". This confirms the port is strictly operating as an access port in the correct logical boundary.

**🚨 Common error note or Troubleshooting tip**
Omitting the `switchport mode access` command is a common oversight. While some switches will automatically force a port into access mode when you assign an access VLAN, it is a mandatory best practice to explicitly define the mode first. This prevents unexpected trunking behavior if the port is later connected to another switch.

**🎯 Mini challenge**
If `HQ-PC1` sends a Layer 2 broadcast frame, which specific ports on `HQ-S1` will receive and process that broadcast now that it is in VLAN 10?

---

### Step 4️⃣: Configuring the HQ-PC2 Access Port for Sales

**Mini-Lesson / Explanation**
We now apply the exact same access port configuration to the second end device. From our Lesson 1 topology, `HQ-PC2` is connected to port `FastEthernet0/6`. We will configure this port as an access port and assign it to the Sales department's isolated boundary, VLAN 20. This ensures that `HQ-PC2` is logically separated from `HQ-PC1`, even though they are plugged into the exact same physical switch hardware.

**Commands to execute**
Enter the interface configuration mode for `HQ-PC2` and apply the access settings:

```bash
interface FastEthernet0/6
switchport mode access
switchport access vlan 20
exit
```

**Verification commands**
Verify the operational status and VLAN assignment for the second host:

```bash
show interfaces FastEthernet0/6 switchport
```

*Observation:* The output must confirm "Administrative Mode: static access" and "Access Mode VLAN: 20 (Sales)". This guarantees that `HQ-PC2` is now strictly contained within the Sales broadcast domain, completely isolated from Engineering.

**🚨 Common error note or Troubleshooting tip**
Accidentally assigning the port to the wrong VLAN ID (e.g., typing `switchport access vlan 10` instead of `20`) is a frequent error. Always double-check the department mapping and the physical connection from Lesson 1 before applying the configuration to avoid cross-departmental data leakage.

**🎯 Mini challenge**
Given that `HQ-PC1` is in VLAN 10 and `HQ-PC2` is in VLAN 20, can they successfully ping each other at Layer 2 right now? Why or why not?

---

### Step 5️⃣: Verifying VLAN Creation and Port Assignments Globally

**Mini-Lesson / Explanation**
The final step in any Layer 2 provisioning task is a comprehensive global verification. We must ensure that our VLAN database is correctly populated and that the physical ports are accurately mapped to their respective logical boundaries. This global check is crucial before we move on to Layer 3 routing in future lessons, as inter-VLAN routing will rely entirely on the accuracy of this Layer 2 foundation.

**Commands to execute**
Return to privileged EXEC mode and perform a final global verification of the switch's Layer 2 state:

```bash
end
show vlan brief
```

**Verification commands**
Analyze the output table carefully to ensure all configurations match our enterprise design:

*Observation:* 
1. Verify that VLANs 10, 20, and 99 are listed with their correct names (Engineering, Sales, Management).
2. Look at the "Ports" column. You should see `Fa0/1` listed under VLAN 10, and `Fa0/6` listed under VLAN 20. 
3. Notice that VLAN 99 currently has no ports assigned. This is expected, as we haven't configured the Switch Virtual Interface (SVI) for management yet.

**🚨 Common error note or Troubleshooting tip**
A major misconception is assuming that because a VLAN is created, the ports are automatically added to it. VLAN creation and port assignment are two distinct steps. If a port is missing from the VLAN column in your output, it is still sitting in the default VLAN 1, which means it is not segmented.

**🎯 Mini challenge**
Look at the ports listed under the default VLAN 1 in your `show vlan brief` output. Which specific ports are still unassigned, and what would happen if you plugged a new PC into one of those ports without configuring it?

---

### 📌 Key Takeaway
In this lesson, you successfully implemented Layer 2 network segmentation on the headquarters switch. You learned how to create a local VLAN database using `vlan [id]` and `name [name]`, establishing isolated broadcast domains for Engineering, Sales, and Management. You then mastered switchport provisioning by explicitly configuring end-device ports as `switchport mode access` and statically assigning them to their respective VLANs using `switchport access vlan [id]`. Finally, you verified the entire Layer 2 topology using `show vlan brief`, ensuring that physical connections perfectly align with logical network boundaries. This segmentation is the foundational step for improving network security, optimizing traffic flow, and preparing for inter-VLAN routing.

Powered by Coding5s System