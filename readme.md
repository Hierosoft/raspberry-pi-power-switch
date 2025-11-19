# raspberry-pi-power-switch
The missing power switch. Why isn't there a power off convention for the Raspberry Pi?? This fixes that.

This is not your silly toggle switch which on & off behave differently:
- With the typical power switch, toggle off does UNSAFE shutdown, toggle on powers on using a convention (disrupt power to boot the device).
- A two-state button may not be in the same state as the device! Using a safe shutdown means you have to press the button twice to turn it on. That is counter-intuitive.
- There **is no** convention to turn off a Raspberry Pi! This is silly. PCs have a power button and it can be configured either to sleep (a common default) or shut down the OS (a better default, especially for Raspberry Pi. No one wants to type or click shutdown, it is just extra steps to do something meta not computery...).
  - Raspberry Pi probably doesn't have an off button because a typical use case is to run 24/7 being the center of the IoT fad, but lets get past that. The Pi, a Pi-compatible, or another Single-Board Computer (SBC) is a great replacement for a computer in many cases, especially a single-use computer for commercial uses (lightweight custom software).

The solution:
- An OFF switch: A service to watch an IO pin for a button press (momentary switch) which will then power off the device using "shutdown 0" (safe immediate shutdown in GNU/Linux).
- An ON/RESET switch: disrupts power as per Raspberry Pi convention (There is a convention to turn it on but not off...)

Requires:
- NO momentary switch (for software-based OFF button)
- NC momentary switch (for ON/RESET)
- Ethernet cable
  - For tidy wiring to the switch box only! Orange and green are used similarly to IEEE 802.3af (PoE) / IEEE 802.3at (PoE+) mode A, IEEE 802.3bt Type 3 (4PPoE), and Type 4 (PoE++), but only as a means of mitigating misuse, not to indicate compatibility.
- (2) Female Dupont wires (Raspberry Pi end)
- Soldering iron or dupont crimper to attach far end of dupont wires to the ethernet cable, and connect DC power to the ethernet cable.
- 2-wire USB cable (You can get a standard Raspberry Pi toggle switch then cut the wire at each side of the toggle)

What this project includes:
- The shutdown button service
- Wiring diagram
- 3D printable housing for DMWD (generic Amazon) "2PCS 22MM Momentary Push Button Switch Start Stop Switch Metal Head XB2 1NO1NC Red + 1NO1NC Green"
  - These buttons are very large, but I like them because they are sturdy.
  - Mountable using wood screws.
  - Any other pair of NC & NO momentary switches can be used.
    - NC for ON/RESET button.
    - NO for OFF button.
  - You'll have to **switch the colors** of the buttons vs wires to use them for this project if you get the NC green and NO red buttons,
