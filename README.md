### Condition Calculator

**Python Version:** 3.9  

**Libraries Used:** Tkinter, Pyinstaller (for exe compilation)

This was built with condi scourge in mind however, should do a good enough job estimating condition damage of other classes.

Lingering Curse is the only trait I considered and manifests in the checkboxes, the +200 condition damage is applied on trait selection however the increased condition duration is applied to the *base* duration of a condition applied by a scepter. The two checkboxes only serve to apply the bonus *base* duration when both are selected

<img src="https://user-images.githubusercontent.com/68555817/145436506-da5dda32-76be-477f-8e0e-c8da8ad1a0fa.png" width=50% height=50%>

#### Condition Damage:
  - Condition Damage stat found on character sheet
#### Duration Multiplier:
  - Found to the right of your expertise value. Hovering over it shows duration multiplier for spesific conditions, if no conditions are listed then the shown value is an increase to all condition duration. This value ranges from 0-1. 
  - From below:
    - Bleed = 0.7846, Torment= 1, Any other condition = 0.5846
  
  ![image](https://user-images.githubusercontent.com/68555817/145437576-c9ba55aa-058a-4040-afcc-751e2c098355.png)

#### Bonus Damage Modifier:
  - This exist mainly to capture the damage increase of [superior sigils of bursting](https://wiki.guildwars2.com/wiki/Superior_Sigil_of_Bursting). I couldn't find any traits Scourge has access to that permanently increase outgoing instances of condition damage outside of the sigil.

#### Base Duration:
  - The base duration of the condition applied by an ability, To find this, check the wiki for the ability that applies the condition, the base duration is listed there.

#### Condition Dropdown Menu:
  - Choose a condition. This serves to set appropriate values for lvl80 base damage and the scale factor of the condition

#### Scepter Ability & Lingering Curse:
  - Tick if the condition is applied by a scepter
  - Tick if you use Lingering Curse
    - These serve to apply the bonus base duration of scepter conditions when both are True 

#### Calculate:
  - Press to calculate the DPS and duration

## Example:
### Scourge: [Blood Curse](https://wiki.guildwars2.com/wiki/Blood_Curse)

I have 1783 condition damage without food/utility buffs
The duration multiplier for my outgoing bleeds is 0.7846 coming from my expertise(727), [barbed precision](https://wiki.guildwars2.com/wiki/Barbed_Precision) and a [superior sigil of malice](https://wiki.guildwars2.com/wiki/Superior_Sigil_of_Malice)

Blood curse applies 4.5 seconds of bleeding

Bleeding has a base damage of 22 at level 80 and a scale factor of 0.06 dps per point of condition damage

I use a [superior sigil of bursting](https://wiki.guildwars2.com/wiki/Superior_Sigil_of_Bursting) so my bonus damage multiplier is 0.05

I have lingering curse selected and the condition is inflicted by a scepter, so both boxes are checked.

This results in the entry boxes looking like:

![image](https://user-images.githubusercontent.com/68555817/145439818-8b23bad9-65d6-40b1-a086-19e3ec73ba5d.png)


The tooltip suggests the following:

![image](https://user-images.githubusercontent.com/68555817/145307506-cf268def-80c1-4c4b-9f43-de4ccad7e123.png)

1554 damage over 12 seconds => 129.5 dps which falls short of the calculated damage

If you increase the tooltip damage by 5% => 1554 to 1631 then spread it over 12 seconds => 135.9 dps which is much closer to the calculated amount

I suspect that the in-game tooltip does not reflect the increased outgoing condition damage applied by the sigil of bursting.

The bleed tick seems to indicate the same:

![image](https://user-images.githubusercontent.com/68555817/145308459-106869b7-a1d7-4e60-aa47-3b584a90a510.png)

Similarly with the output of ARCdps, with an average bleed tick of 137, higher likely due to barbed precision stacking extra bleeds on the same instance of attack

![image](https://user-images.githubusercontent.com/68555817/145309819-511cbb07-bebe-4e3d-90b1-7022bb77a536.png)
