### Condition Calculator

**Python Version:** 3.9  

**Libraries Used:** Tkinter, Pyinstaller (for exe compilation)

This was built with condi scourge in mind however, should do a good enough job estimating condition damage of other classes.

Each damaging condition has it's own set of attributes that can be found [on the Wiki](https://wiki.guildwars2.com/wiki/Condition_Damage#Conditions)

Lingering Curse is the only trait I considered and manifests in the checkboxes, the +200 condition damage is applied on trait selection however the increased condition duration is applied to the *base* duration of a condition applied by a scepter. The two checkboxes only serve to apply the bonus base duration when both are selected

<img src="https://user-images.githubusercontent.com/68555817/145286661-d2b3c0e0-a5d5-4ccb-af89-55a338b2f930.png" width=60% height=60%>

#### 1 & 2:
  - Condition Damage: Take from character sheet
  - Expertise:        Take from character sheet

  ![image](https://user-images.githubusercontent.com/68555817/145290899-b6934a3f-3139-4d35-9ad8-84226a9e2aee.png)

#### 3 & 5:
  - Base Damage:      Take from condition damage [on the Wiki](https://wiki.guildwars2.com/wiki/Condition_Damage#Conditions)
  - Scale Factor:     Take from condition damage [on the Wiki](https://wiki.guildwars2.com/wiki/Condition_Damage#Conditions)

#### 4:
  - Base Duration:    Check the wiki page for the ability [for example](https://wiki.guildwars2.com/wiki/Blood_Curse)

#### 6 & 7:
  - Bonus duration modifier:    Sum the bonus duration multiplier you get for the condition from traits/sigils/runes excluding the bonus from lingering curse
  - Bonus damage modifier:    Sum the bonus damage multiplier you get for the condition from traits/sigils/runes excluding the bonus from lingering curse

Note: Do not use the following values as your multipliers, This is the total amount of increased duration of conditions you apply including expertise

![image](https://user-images.githubusercontent.com/68555817/145291184-5d8340e6-ab78-4b14-a0d7-2086d6ffc30e.png)

The correct way to find the modifier is to look at your selected traits, equiped runes and sigils then total up the modifiers
See the example below

#### 8:
  - Lingering Curse: Check if you have the trait lingering curse selected
  - Scepter Ability: Check if the condition you are calculating was applied by a scepter ability

#### 9:
  - Calculate: Calculates the condition DPS and duration based on the prior inputs and prints them to the areas marked 10

#### 10:
  - Output

## Example:
### Scourge: [Blood Curse](https://wiki.guildwars2.com/wiki/Blood_Curse)

I have 1783 condition damage and 727 expertise without using food/utility buffs.

Blood curse applies 4.5 seconds of bleeding

Bleeding has a base damage of 22 at level 80 and a scale factor of 0.06 dps per point of condition damage

My total duration multiplier is 0.3: 0.2 (20%) coming from [barbed precision](https://wiki.guildwars2.com/wiki/Barbed_Precision) and 0.1 (10%) coming from[a superior sigil of malice](https://wiki.guildwars2.com/wiki/Superior_Sigil_of_Malice)

My total damage multiplier is 0.05 coming from a [superior sigil of bursting](https://wiki.guildwars2.com/wiki/Superior_Sigil_of_Bursting)

I have lingering curse selected and the condition is inflicted by a scepter, so both boxes are checked.

This results in the entry boxes looking like:

![image](https://user-images.githubusercontent.com/68555817/145307074-6d459bec-fdee-4043-9508-e830b24d08d8.png)

The tooltip suggests the following:

![image](https://user-images.githubusercontent.com/68555817/145307506-cf268def-80c1-4c4b-9f43-de4ccad7e123.png)

1554 damage over 12 seconds => 129.5 dps which falls short of the calculated damage

If you increase the tooltip damage by 5% => 1554 to 1631 then spread it over 12 seconds => 135.9 dps which is much closer to the calculated amount

I suspect that the in-game tooltip does not reflect the increased outgoing condition damage applied by the sigil of bursting.

The bleed tick seems to indicate the same:

![image](https://user-images.githubusercontent.com/68555817/145308459-106869b7-a1d7-4e60-aa47-3b584a90a510.png)

Similarly with the output of ARCdps, with an average bleed tick of 137, higher likely due to barbed precision stacking extra bleeds on the same instance of attack

![image](https://user-images.githubusercontent.com/68555817/145309819-511cbb07-bebe-4e3d-90b1-7022bb77a536.png)
