import tkinter as tk

# Total Damage Formula
# (Base Damage + (Condition Damage * Scale Factor)) * (Base Duration * (1 + trait multiplier) * (1 + Bonus Duration + (Expertise / 1500)))

class Character():
    def __init__(self, condition_damage:int, expertise:int, base_damage:float, base_duration: float, bonus_duration_multiplier: float, scale_factor: float, bonus_damage_multiplier: float, lingering_curse:bool = True, scepter: bool = True):
        '''condition_damage:    - value for your characters condition damage\n
        expertise:              - value for your characters expertise\n
        base_damage             - The base damage of the condition at level 80\n
        scale_factor            - Additional damage gained per point of condition damage\n
        bonus_damage_modifier   - Multipliers to outgoing to condition damage from runes/sigils/traits excluding lingering curse\n
        source                  - The weapon the condition was applied by\n
        base_duration           - The base duration of the condition (see: wiki for ability cast)\n
        bonus_duration_modifier - Multipliers to outgoing condition duration from runes/sigils/traits excluding lingering curse\n
        lingering_curse:        - True if you have lingering curse traited, False otherwise.
        scepter:                - True if ability was cast from a scepter, False otherwise.
        ''' 

            # Assigning variables
        self.condition_damage = condition_damage
        self.expertise = expertise
        self.base_damage = base_damage
        self.base_duration = base_duration
        self.bonus_duration_multiplier = bonus_duration_multiplier
        self.scale_factor = scale_factor
        self.bonus_damage_multiplier = bonus_damage_multiplier
        self.lingering_curse = lingering_curse
        self.scepter = scepter
            # each 15 point increase of expertise is a 1% increase in condition duration
        self.condition_duration_increase = self.expertise / 1500


    def condi_duration(self) -> float:
        '''Returns the condition duration of an instance of a condition given the attributes of the duration_dict'''
        lingering_curse_modifier = 0.5 if self.lingering_curse == True and self.scepter == True else 0          # Linering curse increases the base duration of outbound scepter conditions by 50%
        condition_duration = self.base_duration * (1 + lingering_curse_modifier) * (1 + min(1, (self.bonus_duration_multiplier + self.condition_duration_increase)))
        return round(condition_duration, 3)


    def condi_damage(self) -> float:
        '''Returns the per tick condition damage of an instance of a condition given the attributes of the damage_dict'''
        condition_damage = (self.base_damage + (self.condition_damage * self.scale_factor)) * (1 + self.bonus_damage_multiplier)
        return round(condition_damage, 3)


class GUI(tk.Frame, Character):


    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.validate_num = (self.register(self.onValidate), '%d', '%S', '%P', '%i')

        self.lc = tk.BooleanVar(self)
        self.sct = tk.BooleanVar(self)
        
        self.create_widgets()
            # Selecting both tick boxes sets them to be True by default (Optimal DPS Scourge build => these two should be true)
        self.lc_tick.select()
        self.sct_tick.select()
            # These variables don't exist until a the <KeyRelease> bound event creates them, this causes errors if calculate_stats is run without interacting with the entry box.
        self.cd = 0
        self.e = 0
        self.bda = 0
        self.bdu = 0
        self.bdum = 0
        self.sf = 0
        self.bdam = 0
            # binds the conversion of strings to floats to <KeyRelease> for each entry box
        self.bind_events()


    def create_widgets(self):
            # Creating and positioning the GUI elements
        self.cd_l = tk.Label(self, text= 'Condition Damage')
        self.cd_l.grid(column=0, row= 0)
        self.cd_entry = tk.Entry(self, validate= 'key', validatecommand= self.validate_num)
        self.cd_entry.grid(column=0, row= 1, padx= 5, pady= 2)

        self.e_l = tk.Label(self, text= 'Expertise')
        self.e_l.grid(column=1, row= 0)
        self.e_entry = tk.Entry(self, validate= 'key', validatecommand= self.validate_num)
        self.e_entry.grid(column=1, row= 1, padx= 5, pady= 2)

        self.l1 = tk.Label(self, text= 'Base Duration')
        self.l1.grid(column= 1, row = 2)
        self.base_duration_entry = tk.Entry(self, validate= 'key', validatecommand= self.validate_num)
        self.base_duration_entry.grid(column= 1, row = 3, padx= 5, pady= 2)

        self.l2 = tk.Label(self, text= 'Bonus Duration Modifier')
        self.l2.grid(column= 1, row = 4)
        self.bonus_duration_modifier_entry = tk.Entry(self, validate= 'key', validatecommand= self.validate_num)
        self.bonus_duration_modifier_entry.grid(column= 1, row = 5, padx= 5, pady= 2)

        self.l3 = tk.Label(self, text= 'Base Damage')
        self.l3.grid(column= 0, row = 2)
        self.base_damage_entry = tk.Entry(self, validate= 'key', validatecommand= self.validate_num)
        self.base_damage_entry.grid(column= 0, row = 3, padx= 5, pady= 2)

        self.l4 = tk.Label(self, text= 'Scale Factor')
        self.l4.grid(column= 0, row = 4)
        self.scale_factor_entry = tk.Entry(self, validate= 'key', validatecommand= self.validate_num)
        self.scale_factor_entry.grid(column= 0, row = 5, padx= 5, pady= 2)

        self.l5 = tk.Label(self, text= 'Bonus Damage Modifier')
        self.l5.grid(column= 0, row = 6)
        self.bonus_damage_modifier_entry = tk.Entry(self, validate= 'key', validatecommand= self.validate_num)
        self.bonus_damage_modifier_entry.grid(column= 0, row = 7, padx= 5, pady= 2)

        self.lc_tick = tk.Checkbutton(self, text= 'Lingering Curse', onvalue= True, offvalue= False, variable = self.lc)
        self.lc_tick.grid(column= 1, row= 6)

        self.sct_tick = tk.Checkbutton(self, text= 'Scepter Ability', onvalue= True, offvalue= False, variable = self.sct)
        self.sct_tick.grid(column= 1, row= 7)

        self.condidps = tk.Label(self, text= 'Condition DPS:')
        self.condidps.grid(column= 2, row=3, padx= 40)

        self.condiduration = tk.Label(self, text= 'Condition Duration:')
        self.condiduration.grid(column= 2, row=5, padx= 40)

        self.button = tk.Button(self, text= 'Calculate', command= self.calculate_stats)
        self.button.grid(column= 0, row= 8, columnspan= 2, pady= 5)


    def bind_events(self):
        self.cd_entry.bind('<KeyRelease>', self.get_cd)
        self.e_entry.bind('<KeyRelease>', self.get_e)
        self.base_duration_entry.bind('<KeyRelease>', self.get_bdu)
        self.bonus_duration_modifier_entry.bind('<KeyRelease>', self.get_bdum)
        self.base_damage_entry.bind('<KeyRelease>', self.get_bda)
        self.scale_factor_entry.bind('<KeyRelease>', self.get_sf)
        self.bonus_damage_modifier_entry.bind('<KeyRelease>', self.get_bdam)

        # Converting strings to floats
    def get_cd(self, event = None):     # condition damage
        self.cd = 0 if self.cd_entry.get() == '' else float(self.cd_entry.get())
    def get_e(self, event = None):      # expertise
        self.e = 0 if self.e_entry.get() == '' else float(self.e_entry.get())
    def get_bda(self, event = None):    # base damage
        self.bda = 0 if self.base_damage_entry.get() == '' else float(self.base_damage_entry.get())
    def get_bdu(self, event = None):    # base duration
        self.bdu = 0 if self.base_duration_entry.get() == '' else float(self.base_duration_entry.get())
    def get_bdum(self, event = None):   # bonus duration modifier
        self.bdum = 0 if self.bonus_duration_modifier_entry.get() == '' else float(self.bonus_duration_modifier_entry.get())
    def get_sf(self, event= None):      # scale factor
        self.sf = 0 if self.scale_factor_entry.get() == '' else float(self.scale_factor_entry.get())
    def get_bdam(self, event = None):   # bonus damage modifier
        self.bdam = 0 if self.bonus_damage_modifier_entry.get() == '' else float(self.bonus_damage_modifier_entry.get())

        # Creating instance of Character class using converted entry box data & the two tick boxes
    def calculate_stats(self):
        self.player = Character(self.cd, self.e, self.bda, self.bdu, self.bdum, self.sf, self.bdam, self.lc.get(), self.sct.get())
            # debug print
        # print(self.lc.get(), self.sct.get())
            # calling the calculation methods of the instance of the Character class
        self.condition_damage = self.player.condi_damage()
        self.condition_duration = self.player.condi_duration()
            # debug print
        # print(self.condition_damage, self.condition_duration)
            # Updating the right of the GUI to show the calculated damage per second and and duration of an instance of a condition
        self.condidps.configure(text= 'Condition DPS: {}'.format(self.condition_damage))
        self.condiduration.configure(text= 'Condition Duration: {}'.format(self.condition_duration) + 's')
            # debug print
        # print(self.cd, self.e, self.bda, self.bdu, self.sf, self.bdum, self.bdam)


    def count_occurance(self, to_search: str, to_find:str) -> int:
        return to_search.count(to_find)


        # Limiting entries to numbers 0-9 including . to allow for decimals >> For some reason this function prevents use of Ctrl+A + Backspace.
    def onValidate(self, action, key, value, index):
                # is the key a number / decimal point    or   a deletion / selection       and     no more than 1 decimal point    and     the first character is not a decimal point
        if (key in ('1','2','3','4','5','6','7','8','9','0','.', '') or action != '1') and (self.count_occurance(value, '.') <= 1) and not(int(index) == 0 and key == '.'):
            return True
        else:
            self.bell()
            return False

    # Creating instance of the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(parent= root)
    app.parent.title('CondiCalc')
    app.pack(fill="both", expand=True)
    app.mainloop()
