# 📋 Prompt: CCNA Packet Tracer Curriculum Generation (Phase 1)

This prompt is designed for the **Phase 1: Domain Blueprint Generation** of the CCNA Packet Tracer curriculum. Copy and paste the content below into your LLM to generate the analytical blueprint required to populate the Stateful5s Creator Kit.

---

```text
[TECHNOLOGY/SKILL]: Cisco CCNA with Cisco Packet Tracer
[INCLUDE OOP]: NO
[EXCLUSIONS]: (e.g., Advanced CCNP enterprise topics, SDN controllers and orchestration, Network automation with Python/Ansible, SD-WAN, Advanced wireless features, Data center technologies)
[MANDATORY_BRIDGES]: (e.g., OSI Model Layers and Functions, TCP/IP Protocol Stack, Binary/Hexadecimal/Decimal Conversions, IPv4 Addressing Fundamentals, Subnetting Concepts and Calculations, Ethernet Switching Basics, VLANs and Trunking, Static Routing and RIP, Packet Tracer Workspace Navigation and Device Placement)
[ADDITIONAL TOPICS]: (e.g., Packet Tracer Simulation Mode and PDU Tracing, Building and Verifying Topologies in Packet Tracer, CLI Configuration and Verification Workflows, Multi-Device Connectivity Testing)
[OUTPUT LANGUAGE]: English
 
---
Act as a Senior Technical Curriculum Architect. This is PHASE 1 of a curriculum generation process. Your ONLY job is to analyze the technology exhaustively, map the subdomains, and calculate the EXACT number of topics required based on strict grouping logic. DO NOT generate the final curriculum table.
 
Please follow these STRICT rules:
 
1. **EXHAUSTIVE SCOPE & ANTI-OVER-PRUNING (CRITICAL):**
   * Focus ONLY on native features of [TECHNOLOGY/SKILL]. You MUST be exhaustive. Do not skip or hide core language features, operators, or common standard library modules just to save space.
   * STRICTLY BAN anything listed in [EXCLUSIONS].
   * **ANTI-OVER-PRUNING RULE:** When excluding advanced domains, do NOT prune their fundamental prerequisites.
   * **MANDATORY BRIDGES:** You MUST integrate every concept listed in [MANDATORY_BRIDGES] as dedicated topics and subdomains. These act as the ultimate preparation layer.
   * Include [ADDITIONAL TOPICS] if provided.
   * If [INCLUDE OOP] is 'NO', strictly ban all Object-Oriented Programming concepts. If 'YES', include them.
 
2. **THE "TOOLBOX" GROUPING RULE (CRITICAL):**
   * Group functions, methods, or operators into a SINGLE topic ONLY IF they share the exact same mental model and syntactic footprint (e.g., "Basic show Commands", "Interface Configuration Commands", "VLAN Management Commands").
   * BANNED: Do NOT separate sibling methods into individual topics (e.g., Do NOT make one topic for `show running-config` and another for `show startup-config`).
   * BANNED: Do NOT condense concepts from different syntactic families (e.g., Do NOT group topology building in Packet Tracer with entering global configuration mode commands).
 
3. **THE OVERSPILL RULE (MAX 5 VARIANTS PER TOPIC):**
   * A single topic can hold a MAXIMUM of 5 methods, functions, or variants.
   * If a conceptual family has more than 5 common tools (e.g., 10 common show commands or 12 different verification methods), you MUST split it into sequential topics (e.g., "Verification Commands Part 1 (show ip interface brief, show interfaces, ping, traceroute, show ip route)", and "Verification Commands Part 2 (...)").
   * This forces balanced granularity. Do not cheat by omitting important methods just to avoid creating more topics.
 
4. **NO PROJECTS RULE (CRITICAL):**
   * DO NOT include any 'Project' or 'Capstone' topics in this ledger. Your output must consist STRICTLY of standard theoretical and mechanical topics. Projects will be dynamically injected by a separate engine in Phase 2.
 
5. **OUTPUT STRUCTURE:**
   Format your response EXACTLY with these three sections using clean markdown lists (NO markdown tables):
 
   ### 🗺️ 1. Domain Blueprint
   List the major conceptual subdomains that will be covered exhaustively (e.g., Networking Models, IP Addressing & Subnetting, Switching Technologies, Routing Fundamentals, Packet Tracer Operations, etc.), ensuring [MANDATORY_BRIDGES] are included.
 
   ### 🧮 2. Topic Calculation Ledger
   Break down each subdomain from section 1 and list the theoretical topics inside it, showing the grouped methods in parentheses to prove they respect the Toolbox and Overspill rules (Max 5 per topic).
   *Example Format:*
   - **Subdomain: Switching Technologies**
     - Topic: VLAN Configuration Fundamentals
     - Topic: VLAN and Trunking Commands Part 1 (vlan, name, switchport mode access, switchport mode trunk, switchport access vlan)
     - Topic: VLAN and Trunking Commands Part 2 (show vlan brief, show interfaces trunk, show running-config | section interface)
 
   ### 📐 3. Final Metric Contract
   Provide the final calculated numbers based on the Ledger. You MUST output exactly this list:
   * Total Topics (Standard): [Number]
   * GRAND TOTAL ROWS: [Number]
 
Remember: DO NOT generate the curriculum table. Only provide the analytical blueprint.
```