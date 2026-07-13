### 🔹 Lesson #1 | Beginner | Networking

**Physical Topology Baseline: Building the Enterprise Foundation**

Welcome to Lesson 1! Today, we are going to build the physical foundation of a multi-site enterprise network. Our objective is to deploy a core topology consisting of two routers, two switches, and four end devices. By the end of this lesson, you will understand how to select the correct devices, identify their physical ports, and apply the proper cabling standards for both LAN and WAN segments in Cisco Packet Tracer.

### 💡 Analogy
Think of building a network like designing a city's transportation system. The **routers** are the major highway interchanges that connect different cities (networks). The **switches** are the local street intersections that manage traffic within a single neighborhood (LAN). The **cables** are the physical roads, and the **end devices (PCs)** are the houses. If you use a dirt road (wrong cable type) to connect a highway to a local street, traffic won't flow properly. You must lay the right roads between the right intersections to ensure the city functions.

---

### Step 1️⃣: Deploying the Core Network Devices

**Mini-Lesson / Explanation**
The core of our enterprise topology relies on routers for inter-network routing and switches for local network connectivity. We will use the Cisco 4331 Integrated Services Router (ISR) for our routing needs and the Cisco 2960-24TT Switch for our LAN switching. In Packet Tracer, selecting the correct device model is crucial as it dictates the available interfaces and processing power.

**Commands to execute**
1. Open the **Routers** category in the bottom-left device palette and drag two **4331** routers to the workspace.
2. Open the **Switches** category and drag two **2960** switches to the workspace.
3. Click on each device, go to the **Config** tab, and rename them to match our baseline: `HQ-R1`, `Branch-R2`, `HQ-S1`, and `Branch-S2`.
4. Access the CLI for each router to set the hostname officially:

```bash
enable
configure terminal
hostname HQ-R1
exit
exit
```
*(Repeat the CLI commands for `Branch-R2` with its respective hostname).*

**Verification commands**
To verify that the devices are correctly named and booted, use the following command on the routers:
```bash
show running-config | include hostname
```
*Observation:* You should see `hostname HQ-R1` and `hostname Branch-R2` in the output.

**🚨 Common error note or Troubleshooting tip**
Beginners often forget to press `Enter` after typing the hostname, or they forget to exit global configuration mode. Always ensure you see the `Router#` prompt before moving to the next device.

**🎯 Mini challenge**
Look closely at the physical front panel of the 4331 router. How many physical Gigabit Ethernet ports do you count, and what is the highest port number label you see?

---

### Step 2️⃣: Deploying the End Devices

**Mini-Lesson / Explanation**
End devices are the source and destination of our network traffic. In this baseline, we are deploying four Personal Computers (PCs) to simulate user workstations across our two sites (Headquarters and Branch). Properly naming these devices from the start is a critical habit that prevents confusion when troubleshooting later.

**Commands to execute**
1. Open the **End Devices** category in the device palette.
2. Drag four **PC** devices to the workspace.
3. Click on each PC, navigate to the **Config** tab, and change the display name in the top left corner to: `HQ-PC1`, `HQ-PC2`, `BR-PC3`, and `BR-PC4`.
4. *(Note: PCs in Packet Tracer do not use an IOS CLI for naming, so we configure their identity purely via the GUI).*

**Verification commands**
Since PCs do not have a CLI for this step, we verify visually. 
```bash
# Visual Verification:
# Ensure the workspace displays the exact names: HQ-PC1, HQ-PC2, BR-PC3, BR-PC4.
```
*Observation:* The labels under the PC icons should perfectly match the designated site prefixes (HQ for Headquarters, BR for Branch).

**🚨 Common error note or Troubleshooting tip**
A common mistake is naming the devices `PC1`, `PC2`, etc., without the site prefix. Always use the standardized naming convention (`HQ-PC1`) to maintain consistency in multi-site topologies.

**🎯 Mini challenge**
Click on `HQ-PC1`, go to the **Physical** tab, and turn the device on. What is the MAC address displayed on the physical label of the PC?

---

### Step 3️⃣: Establishing the WAN Link (Router-to-Router)

**Mini-Lesson / Explanation**
The Wide Area Network (WAN) link connects our two distinct geographical sites. We are connecting `HQ-R1` to `Branch-R2`. Because we are connecting two similar devices (Router to Router) at the same network layer, we must use a **Copper Cross-Over** cable. This cable crosses the transmit and receive pairs so the devices can communicate. We will use the Gigabit Ethernet ports `G0/0/0` on both routers.

**Commands to execute**
1. Select the **Connections** category (the lightning bolt icon) in the device palette.
2. Choose the **Copper Cross-Over** cable (dashed black line).
3. Click on `HQ-R1` and select port **G0/0/0**.
4. Click on `Branch-R2` and select port **G0/0/0**.

**Verification commands**
Once connected, we can verify the physical layer status. While IP addresses aren't configured yet, we can check the interface status:
```bash
show ip interface brief
```
*Observation:* The `G0/0/0` interface should show the physical status as `up` (indicated by the link light turning green on the workspace), even if the protocol status is `down` due to missing IP configuration.

**🚨 Common error note or Troubleshooting tip**
If you accidentally use a Straight-Through cable here, Packet Tracer's Auto-MDIX feature might still make the link light turn green. However, in the real world and for CCNA exams, using the wrong cable type for router-to-router connections is a critical failure. Always use Cross-Over for similar devices.

**🎯 Mini challenge**
Hover your mouse cursor over the newly created cable between `HQ-R1` and `Branch-R2`. What exact cable type and bandwidth does the tooltip display?

---

### Step 4️⃣: Establishing the LAN Links (Router-to-Switch)

**Mini-Lesson / Explanation**
Now we connect our routers to their respective local switches to form the LAN distribution layer. We are connecting `HQ-R1` to `HQ-S1` and `Branch-R2` to `Branch-S2`. Because we are connecting different device types (Router to Switch), we must use a **Copper Straight-Through** cable. We will utilize the `G0/0/1` ports on the routers and connect them to the `G0/1` Gigabit uplink ports on the 2960 switches for maximum throughput.

**Commands to execute**
1. Select the **Copper Straight-Through** cable (solid black line) from the Connections palette.
2. Click on `HQ-R1` and select port **G0/0/1**.
3. Click on `HQ-S1` and select port **G0/1**.
4. Repeat the process for the branch site: Click `Branch-R2` port **G0/0/1** and connect it to `Branch-S2` port **G0/1**.

**Verification commands**
Verify the physical connectivity on the switches using the following command:
```bash
show interfaces status
```
*Observation:* Look for ports `Gi0/1` on both switches. The "Status" column should read `connected`, and the "Duplex" column should ideally show `a-full` (auto-negotiated full duplex).

**🚨 Common error note or Troubleshooting tip**
Ensure you are plugging into the Gigabit port (`G0/1`) on the switch, not a FastEthernet port (`F0/1`). While FastEthernet would technically work, using Gigabit ports for router-to-switch links prevents bandwidth bottlenecks in an enterprise baseline.

**🎯 Mini challenge**
Why do we use the `G0/0/1` port on the router instead of `G0/0/0` for the switch connection? (Hint: Think about the port we used in Step 3).

---

### Step 5️⃣: Connecting End Devices to the LAN

**Mini-Lesson / Explanation**
The final physical connections involve linking our end devices to the access layer switches. We are connecting `HQ-PC1` and `HQ-PC2` to `HQ-S1`, and `BR-PC3` and `BR-PC4` to `Branch-S2`. Since PCs and switches are different device types, we continue to use **Copper Straight-Through** cables. We will distribute the PCs across the switch ports, specifically using `F0/1` and `F0/6` to simulate a realistic, spaced-out physical patch panel layout.

**Commands to execute**
1. Ensure you are still using the **Copper Straight-Through** cable.
2. Connect `HQ-PC1` to `HQ-S1` port **F0/1**.
3. Connect `HQ-PC2` to `HQ-S1` port **F0/6**.
4. Connect `BR-PC3` to `Branch-S2` port **F0/1**.
5. Connect `BR-PC4` to `Branch-S2` port **F0/6**.

**Verification commands**
To verify that the switches have detected the physical connections and can see the PCs' MAC addresses, use:
```bash
show mac address-table
```
*Observation:* You should see entries for ports `Fa0/1` and `Fa0/6` on both switches. The MAC addresses listed will dynamically match the physical MAC addresses of the connected PCs.

**🚨 Common error note or Troubleshooting tip**
A frequent error is crossing the cables, such as connecting `HQ-PC1` to `Branch-S2`. Always double-check the device names and the specific port numbers (F0/1 vs F0/6) before clicking to finalize the connection.

**🎯 Mini challenge**
If you were to connect a server instead of a PC to port `F0/6`, would you change the cable type? Why or why not?

---

### Step 6️⃣: Verifying Physical Connectivity and Link Lights

**Mini-Lesson / Explanation**
The final step in building a physical baseline is a comprehensive visual and logical inspection of all link lights. In Packet Tracer, link lights provide immediate feedback on the physical layer status. A **Green** light indicates a successful physical connection (Layer 1 is up). An **Amber** light on a switch port often indicates that Spanning Tree Protocol (STP) is blocking the port to prevent loops, or it indicates a 100Mbps negotiation. A **Red** light means the cable is disconnected, the device is powered off, or there is a physical mismatch.

**Commands to execute**
1. Visually inspect every single cable in your workspace.
2. Ensure all devices are powered on (click them and check the power button in the Physical tab if any light is red).
3. Verify that the WAN link (Cross-Over) and all LAN links (Straight-Through) are showing the correct colors.

**Verification commands**
Perform a final global verification on both routers and switches to ensure all physical interfaces are active:
```bash
show interfaces status
show ip interface brief
```
*Observation:* 
- On `HQ-R1` and `Branch-R2`, `G0/0/0` and `G0/0/1` should show physical status `up`.
- On `HQ-S1` and `Branch-S2`, `Gi0/1`, `Fa0/1`, and `Fa0/6` should show status `connected`.

**🚨 Common error note or Troubleshooting tip**
If you see an Amber link light on a switch port connected to a PC, do not panic. This is normal behavior for STP listening/learning states. However, if the light is Red, check that the PC is powered on and that you didn't accidentally use a Cross-Over cable for the PC-to-Switch connection.

**🎯 Mini challenge**
Look at the link light between `HQ-R1` and `Branch-R2`. Hover over it. Does it show a bandwidth of 1000 Mbps or 100 Mbps? What does this tell you about the negotiation between the two 4331 routers?

---

### 📌 Key Takeaway
In this lesson, you successfully built the physical foundation of a multi-site enterprise network. You learned to differentiate between device types (Routers vs. Switches vs. PCs), correctly identify physical ports (Gigabit vs. FastEthernet), and apply the fundamental cabling rules: **Cross-Over cables** for similar devices (Router-to-Router) and **Straight-Through cables** for different devices (Router-to-Switch, PC-to-Switch). A solid physical baseline is the mandatory first step before any logical IP configuration can take place.

Powered by Coding5s System