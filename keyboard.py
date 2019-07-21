import os 
cmd = 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
os.system(cmd)

# ========== Configurations ====================
BUTTON_BACKGROUND   = "black"
MAIN_FRAME_BACKGROUND  = "cornflowerblue"
BUTTON_LOOK    = "flat" #flat, groove, raised, ridge, solid, or sunken
TOP_BAR_TITLE    = "Python Virtual KeyBoard."
TOPBAR_BACKGROUND   = "skyblue"
TRANSPARENCY    = 0.7
FONT_COLOR     = "white"

# ==============================================

# import modules
try:
    import Tkinter
except:
    import tkinter as Tkinter

import tkinter as tk
import pyautogui

# Creating Main Window
def main():
 root = Tkinter.Tk(className=" Python Virtual KeyBoard")

 root.mainloop()
 return

# Confifuration
 root.overrideredirect(True)
 root.wait_visibility(root)
 root.wm_attributes('-alpha',TRANSPARENCY)
 # Custom
 f = Tkinter.Frame(root)
 t_bar=Tkinter.Label(f, text=TOP_BAR_TITLE, bg=TOPBAR_BACKGROUND)
 t_bar.pack(side='left',expand="yes", fill="both")
 mechanism = top_moving_mechanism(root, t_bar)
 t_bar.bind("<B1-Motion>", mechanism.motion_activate)
 Tkinter.Button(f, text="[X]", command= root.destroy).pack(side='right')
 f.pack(side='top', expand='yes',fill='both')
 k.pack(side='top')
 root.mainloop()
 return

# Function Trigger
if __name__=='__main__':
 main()

keys =[

# =========================================
# ===== Keyboard Configurations ===========
# =========================================

 [
  # Layout Name
  ("Function_Keys"),

  # Layout Frame Pack arguments
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   # list of Keys in one row
   ('esc'," ", 'F1', 'F2','F3','F4',"",'F5','F6','F7','F8',"",'F9','F10','F11','F12')
  ]
 ],

 [
  ("Character_Keys"),
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   ('~\n`','!\n1','@\n2','#\n3','$\n4','%\n5','^\n6','&\n7','*\n8','(\n9',')\n0','_\n-','+\n=','|\n\\','backspace'),
   ('tab','q','w','e','r','t','y','u','i','o','p','{\n[','}\n]','   '),
   ('capslock','a','s','d','f','g','h','j','k','l',':\n;',"\"\n'","enter"),
   ("shift",'z','x','c','v','b','n','m','<\n,','>\n.','?\n/',"shift"),
   ("ctrl", "[+]",'alt','\t\tspace\t\t','alt','[+]','[=]','ctrl')
  ]
 ]
],
[
 [
  ("System_Keys"),
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   (
    "print\nscreen\nsys",
    "scroll\nlock",
    "pause\nbreak"
   )
  ]
 ],
 [
   ("Editing_Keys"),
   ({'side':'top','expand':'yes','fill':'both'}),
   [
    (
     "insert",
     "home",
     "page\nup"
     ),
    ( "delete",
    "end",
    "page\ndown"
    ),
  ]
 ],

 [
  ("Navigation_Keys"),
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   (
    "up",
    ),
   ( "right",
    "down",
    "left"
    ),
  ]
 ],

],
[

 [
  ("Numeric_Keys"),
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   ("num\nlock","/","*","-"),
   ("7","8","9","+"),
   ("4","5","6"," "),
   ("0","1","2","3"),
   ("0",".","enter")
  ]
 ],

]

##  Frame Class
class Keyboard(Tkinter.Frame):
 def __init__(self, *args, **kwargs):
  Tkinter.Frame.__init__(self, *args, **kwargs)

  # Function For Creating Buttons
  self.create_frames_and_buttons()

 # Function For Extracting Data From KeyBoard Table
 # and then provide us a well looking
 # keyboard gui
 def create_frames_and_buttons(self):
  for key_section in keys:
   # create Separate Frame For Every Section
   store_section = Tkinter.Frame(self)
   store_section.pack(side='left',expand='yes',fill='both',padx=10,pady=10,ipadx=10,ipady=10)

  for _layername, layer_properties, layer_keys in key_section:
    store_layer = Tkinter.LabelFrame(store_section)#, text=layer_name)
    #store_layer.pack(side='top',expand='yes',fill='both')
    store_layer.pack(layer_properties)
    for key_bunch in layer_keys:
     store_key_frame = Tkinter.Frame(store_layer)
     store_key_frame.pack(side='top',expand='yes',fill='both')
     for k in key_bunch:
      k=k.capitalize()
      if len(k)<=3:
       store_button = Tkinter.Button(store_key_frame, text=k, width=2, height=2)
      else:
       store_button = Tkinter.Button(store_key_frame, text=k.center(5,' '), height=2)
      if " " in k:
       store_button['state']='disable'
      #flat, groove, raised, ridge, solid, or sunken
      store_button['relief']=BUTTON_LOOK
      store_button['bg']=BUTTON_BACKGROUND
      store_button['command']=lambda q=k: self.button_command(q)
      store_button.pack(side='left',fill='both',expand='yes')
  return

  # Function For Detecting Pressed Keyword.
 def button_command(self, event):
    pyautogui.press('event')
    return

class top_moving_mechanism:
 def __init__(self, root, label):
  self.root = root
  self.label = label

 def motion_activate(self, kwargs):
  w,h = (self.root.winfo_reqwidth(), self.root.winfo_reqheight())
  (x,y) = (kwargs.x_root, kwargs.y_root)
  self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))
  return

   