from pyscript import document
from pyodide.ffi import create_proxy

panel = document.getElementById("panel")
hair_layer = document.getElementById("hair-layer")
outfit_layer = document.getElementById("outfit-layer")
hair_options = document.getElementById("hair-options")
outfit_options = document.getElementById("outfit-options")
HAIR_BLONDE = "assets/blonde_hair.png"
HAIR_BRUNETTE = "assets/brunette_hair.png"
OUTFIT_CASUAL = "assets/casual_outfit.png"
OUTFIT_DRESS = "assets/dress_outfit.png"

undo_stack = []
redo_stack = []


def get_current_state():
    return {"hair": hair_layer.getAttribute("src"), "outfit": outfit_layer.getAttribute("src")}

def apply_state(state):
    set_layer(hair_layer, state["hair"])
    set_layer(outfit_layer, state["outfit"])

def set_layer(layer, path):
    if path:
        layer.src = path
    else:
        layer.removeAttribute("src")

def save_state():
    undo_stack.append(get_current_state())
    redo_stack.clear()

def undo(event):
    if len(undo_stack) > 0:
        redo_stack.append(get_current_state())
        previous_state = undo_stack.pop()
        apply_state(previous_state)

def redo(event):
    if len(redo_stack) > 0:
        undo_stack.append(get_current_state())
        next_state = redo_stack.pop()
        apply_state(next_state)


def open_hair_panel(event):
    if hair_options.hasAttribute("hidden"):
        panel.removeAttribute("hidden")
        hair_options.removeAttribute("hidden")
        outfit_options.setAttribute("hidden", "true")
    else:
        panel.setAttribute("hidden", "true")
        hair_options.setAttribute("hidden", "true")

def open_outfit_panel(event):
    if outfit_options.hasAttribute("hidden"):
        panel.removeAttribute("hidden")
        outfit_options.removeAttribute("hidden")
        hair_options.setAttribute("hidden", "true")
    else:
        panel.setAttribute("hidden", "true")
        outfit_options.setAttribute("hidden", "true")

def close_panel(event):
    panel.setAttribute("hidden", "true")

def toggle_layer(layer, path):
    if layer.getAttribute("src") == path:
        layer.removeAttribute("src")
    else: 
        layer.src = path


def choose_hair_blonde(event):
    save_state()
    toggle_layer(hair_layer, HAIR_BLONDE)

def choose_hair_brunette(event):
    save_state()
    toggle_layer(hair_layer, HAIR_BRUNETTE)

def choose_outfit_casual(event):
    save_state()
    toggle_layer(outfit_layer, OUTFIT_CASUAL)

def choose_outfit_dress(event):
    save_state()
    toggle_layer(outfit_layer, OUTFIT_DRESS)

document.getElementById("hair-menu-btn").addEventListener("click", create_proxy(open_hair_panel))
document.getElementById("outfit-menu-btn").addEventListener("click", create_proxy(open_outfit_panel))
document.getElementById("close-btn").addEventListener("click", create_proxy(close_panel))

document.getElementById("hair-blonde-btn").addEventListener("click", create_proxy(choose_hair_blonde))
document.getElementById("hair-brunette-btn").addEventListener("click", create_proxy(choose_hair_brunette))
document.getElementById("outfit-casual-btn").addEventListener("click", create_proxy(choose_outfit_casual))
document.getElementById("outfit-dress-btn").addEventListener("click", create_proxy(choose_outfit_dress))

document.getElementById("undo-btn").addEventListener("click", create_proxy(undo))
document.getElementById("redo-btn").addEventListener("click", create_proxy(redo))
